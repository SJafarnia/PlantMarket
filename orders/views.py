from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from utils.factor_n_gen import random_string_generator
from users.forms import AddressForm
from users.models import Address
from .models import Order, Service, Factor, Payment
from products.models import Product
from .forms import Services, ChoseAddressForm, ChosenAddress, PayMethodForm
from utils.zarinPal_idPay import send_payment_request_idpay, send_verify_idpay
from django.views.decorators.csrf import csrf_exempt


class EditOrder(LoginRequiredMixin, View):
    def get(self, req, pk):
        q = Order.objects.filter(id=pk).first()
        data = {
            "services": [q.change_soil, q.change_pot],
            "quant": q.quantity,
            "pot": q.pot,
        }
        form = Services(initial=data)
        pot_q = Order.objects.select_related("product").filter(costumer=req.user).all()
        ches = []

        for item in q:
            vm = item

        if pot_q is not None:
            for order in pot_q:
                if order.pot:
                    ches.append((f"{order.pot}", f"{order.pot}"))
        form.fields["pot"].choices = ches

        return render(
            req, template_name="products/detail.html", context={"post": q, "form": form}
        )

    # def post(self, req, slug):
    #     form = Services(req.POST)
    #     if form.is_valid():
    #         q = Product.objects.filter(id=slug).first()
    #         order = Order(product=q, costumer=req.user, final_price=q.price)
    #         # fq = list(form.cleaned_data.get("service1"),form.cleaned_data.get("service2"),form.cleaned_data.get("service3"))
    #         fq = form.cleaned_data.get("services")
    #
    #         for item in fq:
    #             if item == "change_soil":
    #                 order.change_soil = 1
    #                 order.final_price += 10
    #                 order.save()
    #             elif  item == "change_pot":
    #                 order.change_pot = 1
    #                 order.final_price += 5
    #                 order.save()
    #         return HttpResponse("success")


class Card(View):
    def get(self, req):
        if req.user.is_authenticated:
            qs = (
                Order.objects.select_related("product")
                .filter(costumer=req.user, is_paid=False)
                .all()
            )

            if qs is not None:
                return render(req, "orders/card.html", context={"orders": qs})
            return render(req, "404notfound.html")
        else:
            return render(req, "404notfound.html")


class DeleteOrder(LoginRequiredMixin, View):
    def get(self, req, slug):
        q = Order.objects.filter(id=slug).delete()
        return redirect(reverse("factor_pay_url"))


class ChooseAdd(LoginRequiredMixin, View):
    def get(self, req):
        qs = Address.objects.filter(user_o=req.user).all()

        if not qs:
            form = AddressForm()
            return render(req, "orders/address.html", context={"form": form, "n": True})
        elif qs:
            return render(req, "orders/address.html", context={"data": qs})

    def post(self, req):
        qs = Address.objects.filter(user_o=req.user).all()

        if not qs:
            form = AddressForm(req.POST)

            if form.is_valid():
                x = form.save(commit=False)
                x.user_o = req.user
                x.save()
                return JsonResponse({"code": f"{x.postal_code}"}, status=200)

            return render(req, "orders/address.html", context={"form": form, "n": True})

        elif qs:
            code = req.POST.get("code")
            return redirect(reverse("paycheck_url", kwargs={"slug": code}))


class NewAddr(LoginRequiredMixin, View):
    def get(self, req):
        form = AddressForm()
        return render(req, "orders/address.html", context={"form": form, "n": True})

    def post(self, req):
        form = AddressForm(req.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.user_o = req.user
            x.save()
            return JsonResponse({"code": f"{x.postal_code}"}, status=200)

        return render(req, "orders/address.html", context={"form": form, "n": True})


class PayCheck(LoginRequiredMixin, View):
    def get(self, req, slug):
        add = Address.objects.filter(postal_code=slug).first()
        orders = (
            Order.objects.select_related("product")
            .filter(costumer=req.user, is_paid=False)
            .all()
        )
        paymethod = PayMethodForm()
        t = 0
        for ord in orders:
            t += ord.final_price
        return render(
            req,
            "orders/payment_check.html",
            {"address": add, "orders": orders, "form": paymethod, "t": t},
        )

    def post(self, req, slug):
        paymethod = PayMethodForm(req.POST)
        if paymethod.is_valid():
            q = Address.objects.filter(postal_code=slug).first()
            method = paymethod.cleaned_data.get("method")
            new_fac = Factor(
                costumer=req.user, factor_n=random_string_generator(6), to=q
            )
            new_fac.save()
            new_fac.factor_final_price += method.price
            new_fac.save()
            orders = (
                Order.objects.select_related("product")
                .filter(costumer=req.user, is_paid=False)
                .all()
            )
            for order in orders:
                new_fac.factor_final_price += order.final_price
                new_fac.save()
                order.factor = new_fac
                order.save()

            terminal = send_payment_request_idpay(
                new_fac.id,
                new_fac.factor_final_price,
                req.user.first_name,
                "",
                "",
                f"پرداخت سفارش{new_fac.factor_n}",
                f"http://127.0.0.1:8000/orders/payverf/",
            )
            new_payment = Payment(
                pay_id=terminal[0],
                pay_link=terminal[1],
                order_id=new_fac.id,
                factor=new_fac,
            )
            new_payment.save()
            print(terminal[1])

            return JsonResponse({"link": f"{terminal[1]}"}, status=200)

        return JsonResponse({"fv": "fnotnavalid"}, status=200)


class verifyPay(View):
    def get(self, req):
        sts = req.GET.get("status")
        order = req.GET.get("order_id")
        pay_id = req.GET.get("id")
        payment_status = "false"
        if sts == 100:
            factor = Payment.objects.filter(pay_id=pay_id, order_id=order).first()
            terminal = send_verify_idpay(pay_id=pay_id, order_id=order)
            if terminal[0] == "100":
                factor.verf_track_id = terminal[2]
                is_paid_before = Payment.objects.filter(
                    track_id=terminal[3]["payment"], pay_id=terminal[1]
                ).exists()
                if is_paid_before:
                    payment_status = "payment used before"
                elif not is_paid_before:
                    factor.is_verified, factor.factor.is_paid = True
                    for item in factor.factor.orders.all():
                        item.is_paid = True
                        item.save()
                    # factor.factor.is_paid = True
                    factor.status = terminal[0]
                    factor.track_id = terminal[3]["payment"]
                    payment_status = "true"
            elif terminal[0] == "101":
                # factor.verf_track_id = terminal[2]
                # factor.save()
                payment_status = "alreadyverified"

        return render(req, "orders/payment_verify.html", {"sts": payment_status})

    def post(self, req):
        sts = req.POST.get("status")
        order = req.POST.get("order_id")
        pay_id = req.POST.get("id")
        payment_status = "false"
        if sts == 100:
            factor = Payment.objects.filter(pay_id=pay_id, order_id=order).first()
            terminal = send_verify_idpay(pay_id=pay_id, order_id=order)
            if terminal[0] == "100":
                factor.verf_track_id = terminal[2]
                is_paid_before = Payment.objects.filter(
                    track_id=terminal[3]["payment"], pay_id=terminal[1]
                ).exists()
                if is_paid_before:
                    payment_status = "payment used before"
                elif not is_paid_before:
                    factor.is_verified, factor.factor.is_paid = True
                    # factor.factor.is_paid = True
                    factor.status = terminal[0]
                    factor.track_id = terminal[3]["payment"]
                    payment_status = "true"
            elif terminal[0] == "101":
                # factor.verf_track_id = terminal[2]
                # factor.save()
                payment_status = "alreadyverified"

        return render(req, "orders/payment_verify.html", {"sts": payment_status})


verf = csrf_exempt(verifyPay.as_view())


class PaymentDoneCallBack(LoginRequiredMixin, View):
    def get(self, req, response):
        qs = (
            Order.objects.select_related("cosutmer")
            .filter(is_paid=False, costumer=req.user)
            .all()
        )
        paid_price = 0
        for item in qs:
            paid_price += item.final_price
        if paid_price == response.terminalfeedbackprice:
            factor = (
                Factor.objects.filter(is_paid=False, costumer=req.user)
                .order_by("-id")
                .first()
            )
            factor.is_paid = True
            factor.save()
            status = ""
            return render(req, "orders/payment_done.html", {"status": status})
