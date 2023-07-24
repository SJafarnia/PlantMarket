from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from orders.forms import Quantity
from orders.models import Factor, Order
from .forms import Profile, UserLoginForm, UserSignUpForm, AddressForm, SmsVerifyForm
from django.db.models import Q
from .models import Address, User
from django.views import View
import random
import string
from utils.kavengar import *
from django.urls import reverse
import json
import os


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


class UserMainView(LoginRequiredMixin, View):
    def get(self, req):
        return render(req, "users/main_profile.html")


class UserSignUp(View):
    def get(self, req):
        form = UserSignUpForm()
        return render(req, "users/signup.html", context={"form": form})

    def post(self, req):
        form = UserSignUpForm(req.POST)
        if form.is_valid():
            f_name = form.cleaned_data.get("first_name")
            l_name = form.cleaned_data.get("last_name")
            pw = form.cleaned_data.get("confirm_password")
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")
            # user = User.objects.filter(Q(phone=phone) | Q(email=email)).first()
            phone_e = User.objects.filter(Q(phone=phone) | Q(username=phone)).exists()
            mail_e = User.objects.filter(email__iexact=email).exists()
            if email == "":
                mail_e = False
            if not phone_e and not mail_e:
                new_obj = User(
                    is_active=False,
                    username=f"{phone}",
                    first_name=f_name,
                    last_name=l_name,
                    phone=phone,
                    email=email,
                )
                new_obj.set_password(pw)
                tok = random.randint(10 ** (6 - 1), (10**6) - 1)
                new_obj.email_active_code = tok
                new_obj.save()
                login(req, new_obj)
                try:
                    api = KavenegarAPI(
                        "61536C5277326564654653684459416632596459716C3068712B4C334832767839616C4768734F6237574D3D",
                        timeout=10,
                    )
                    params = {
                        "sender": "2000500666",  # optional
                        "receptor": f"98{phone}",  # multiple mobile number, split by comma
                        "message": f"{tok}",
                    }
                    # OTP service

                    # response = api.sms_send(params)
                    # print(response)
                except APIException as e:
                    print(e)
                except HTTPException as e:
                    print(e)

                # return render(req, "users/Verify.html", context={"form":form_s, "userid": new_obj.id})
                # return redirect(reverse("verify_url", args={new_obj.phone}))
                return JsonResponse(
                    {"fv": "formValidated", "id": new_obj.phone}, status=200
                )
            if phone_e:
                form.add_error("phone", "این شماره قبلا ثبت شده است!")
            if mail_e:
                form.add_error("email", "این ایمیل قبلا ثبت شده است!")

        return render(req, "users/signup.html", context={"form": form})


class UserVerify(View):
    def get(self, req, pk):
        form = SmsVerifyForm()
        return render(req, "users/Verify.html", context={"form": form, "userid": pk})

    def post(self, req, pk):
        form = SmsVerifyForm(req.POST)
        print(req.POST)
        user = User.objects.filter(phone=pk).first()
        if form.is_valid():
            print("form is valid")
            tkn = form.cleaned_data.get("code")
            print(tkn)
            print(user.email_active_code)
            if tkn == user.email_active_code:
                user.is_active = True
                # user.email_active_code = ""
                user.save()
                return JsonResponse({"fv": "formValidated"}, status=200)
            else:
                form.add_error("code", "کد مطابقت ندارد")
                return render(req, "users/Verify.html", context={"form": form})
        print("form rid")
        return render(req, "users/Verify.html", context={"form": form})


class SendSms(View):
    def get(self, req):
        user = User.objects.filter(id=id).first()
        try:
            api = KavenegarAPI(os.environ.get("KAVENEGAR") | "", timeout=10)
            params = {
                "sender": "2000500666",  # optional
                "receptor": f"98{user.phone}",  # multiple mobile number, split by comma
                "message": f"{user.email_active_code}",
            }
            # response = api.sms_send(params)
            # print(response)
            response = "dodododod"
        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)
        return JsonResponse(f"{response}", status=200)


class UserLogin(View):
    def get(self, req):
        form = UserLoginForm()
        return render(req, "users/login.html", context={"form": form})

    def post(self, req):
        form = UserLoginForm(req.POST)
        if form.is_valid():
            qw = form.cleaned_data.get("username")
            pw = form.cleaned_data.get("password")
            user = User.objects.filter(
                Q(phone__iexact=qw) | Q(email__iexact=qw)
            ).first()
            if user is not None:
                if user.is_active:
                    pw_check = user.check_password(pw)
                    if pw_check:
                        login(req, user)
                        return redirect(reverse("user_main_page_url"))
                    else:
                        form.add_error("password", "پسورد اشتباه است!")
                else:
                    form.add_error(
                        "username",
                        "حساب شما تایید نشده است! برای تایید آن به لینک زیر مراجعه فرمایید",
                    )
            else:
                form.add_error("username", "کاربر یافت نشد!")
        return render(req, "users/login.html", context={"form": form})


class FactorHistory(LoginRequiredMixin, View):
    def get(self, req):
        qs = Factor.objects.filter(costumer=req.user).all()
        # print(qs[0])
        print(qs)
        return render(req, "users/factor.html", context={"factors": qs})


class FactorHistoryDetails(LoginRequiredMixin, View):
    def get(self, req):
        orders = Order.objects.select_related("factor").filter(costumer=req.user).all()
        # print(qs)
        qs = Factor.objects.filter(costumer=req.user).all()
        li = []

        # for factor in qs:
        #     ls = []

        #     for item in orders:
        #         if not item.factor:
        #             continue
        #         elif item.factor == factor:
        #             ls.append(item)
        #     if ls == []:
        #         continue
        #     else :
        #         li.append(ls)

        # print(li)
        return render(req, "users/factor_detail.html", context={"factors": qs})


class EditOrderQ(LoginRequiredMixin, View):
    def get(self, req):
        idd, quan, pot, soil = (
            req.GET.get("oid"),
            req.GET.get("qu"),
            req.GET.get("pot"),
            req.GET.get("soil"),
        )
        q = Order.objects.filter(id=idd).first()
        q.quantity = quan
        if pot == "True":
            q.change_pot = True
        elif pot == "False":
            q.change_pot = False
        if soil == "True":
            q.change_soil = True
        elif soil == "False":
            q.change_soil = False
        q.save()
        return redirect(reverse("factor_pay_url"))


class OrderListPay(LoginRequiredMixin, View):
    def get(self, req):
        form = Quantity()
        qs = (
            Order.objects.select_related("product")
            .filter(is_paid=False, costumer=req.user)
            .all()
        )
        total = 0
        for item in qs:
            # item.save()
            total += item.final_price
        return render(
            req,
            "users/factor_pay.html",
            context={"form": form, "factor": qs, "t": str(total)},
        )

    def post(self, req):
        # form = Quantity(req.POST)
        def random_string_generator(size, chars=string.ascii_lowercase + string.digits):
            return "".join(random.choice(chars) for _ in range(size))
        qs = Order.objects.filter(is_paid=False, costumer=req.user).all()
        d = json.dumps(req.POST)
        kb = json.loads(d)
        return redirect(reverse("main_page_url"))


class FactorStatus(LoginRequiredMixin, View):
    def get(self, req):
        pass


class EditProfile(LoginRequiredMixin, View):
    def get(self, req):
        form = Profile()
        return render(req, "users/user_profile.html", {"form": form})


class Profile(LoginRequiredMixin, View):
    def get(self, req):
        q = User.objects.filter(id=req.user.id).first()
        return render(req, "users/user_profile.html", {"u": q})


class UserAddresses(LoginRequiredMixin, View):
    def get(self, req):
        qs = Address.objects.filter(user_o=req.user).all()
        if not qs:
            form = AddressForm()
            return render(
                req, "users/addAddress.html", context={"form": form, "n": True}
            )
        else:
            return render(req, "users/addresses.html", context={"addresses": qs})

    def post(self, req):
        form = AddressForm(req.POST or None)
        if form.is_valid():
            x = form.save(commit=False)
            x.user_o = req.user
            x.save()
            return JsonResponse({"fv": "formValidated"}, status=200)
        else:
            form = AddressForm(req.POST)
            return render(
                req, "users/addAddress.html", context={"form": form, "n": True}
            )


class EditAddress(LoginRequiredMixin, View):
    def get(self, req, slug):
        a = Address.objects.filter(id=slug).first()
        form = AddressForm(instance=a)
        return render(
            req, "users/editA.html", context={"form": form, "obj": req.GET.get("id")}
        )

    def post(self, req, slug):
        a = Address.objects.filter(id=slug).first()
        print(req.POST)

        form = AddressForm(req.POST or None, instance=a)
        if form.is_valid():
            x = form.save(commit=False)
            x.save()
            return JsonResponse({"fv": "formValidated"}, status=200)
        else:
            return render(
                req,
                "users/editA.html",
                context={"form": form, "obj": req.POST.get("id")},
            )


class AddAddress(LoginRequiredMixin, View):
    def get(self, req):
        form = AddressForm()
        return render(req, "users/addAddress.html", context={"form": form, "n": True})

    def post(self, req):
        form = AddressForm(req.POST or None)
        if form.is_valid():
            x = form.save(commit=False)
            x.user_o = req.user
            x.save()
            return JsonResponse({"fv": "formvalidated"}, status=200)
        else:
            form = AddressForm(req.POST)
            print(form.errors.as_data())  # here you print errors to terminal
            return render(
                req, "users/addAddress.html", context={"form": form, "n": True}
            )
