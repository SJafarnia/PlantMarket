from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from orders.forms import Services, PotOrderForm
from orders.models import Order
from .models import Product, ProductPic, Pot, PotPic, ProductVisit
from utils.sep import seperator
from utils.ip_getter import get_ip
from users.models import User

# @login_required
def main_page(req):
    new = Product.objects.order_by("id").filter(is_avail=True)[0:3]

    return render(req, "products/main.html", context={"news": new})


class ProductList(View):

    def get(self, req):
        qs = Product.objects.all()
        # x = seperator(qs, 3)
        for i in qs:
            x = i
        return render(req, template_name="products/s.html", context={"posts":qs})


class PotList(View):
    def get(self, req):
        qs = Pot.objects.all()
        # x = seperator(qs, 3)
        for i in qs:
            x = i
        return render(req, template_name="products/pot_list.html", context={"posts":qs})


class ProductDetail(View):

    def get(self, req, pk):
        form = Services(req.user)
        q = Product.objects.filter(id=pk).first()
        gallery = list(ProductPic.objects.filter(product=q).all())
        for i in gallery:
            x = i
            
        gallery.insert(0, q)
        user_ip = get_ip(req)
        user_id = None

        is_visited = ProductVisit.objects.filter(ip__iexact=user_ip).exists()
        if not is_visited:
            if req.user.is_authenticated:
                user_id = req.user
                new_visit = ProductVisit(ip=user_ip, costumer=user_id, product=q)
                new_visit.save()
                
            # else:
            #     new_visit = ProductVisit(ip=user_ip, costumer=user_id, product=q)
            #     new_visit.save()
    
        return render(req, template_name="products/detail.html", context={"post":q, "pics":gallery, "form":form})

    def post(self, req, pk):
        if req.user.is_authenticated:
            form = Services(req.user, req.POST)
            if form.is_valid():
                q = Product.objects.filter(id=pk).first()
                quant = form.cleaned_data.get("quantity")
                services = form.cleaned_data.get("s")
                pot = form.cleaned_data.get("pot")
                pot_q = Pot.objects.filter(name__iexact=pot).first()

                change_pot, change_soil  = False, False

                for item in services:
                    if item == "change_soil":
                        change_soil = True
                    if item == "change_pot":
                        change_pot = True
                if pot_q is not None:
                    order = Order(product=q, costumer=req.user, pot=pot_q,quantity=quant, change_pot=change_pot, change_soil=change_soil)
                    for item in services:
                        if item == "r_p":
                            Order.objects.filter(costumer=req.user, product=None, is_paid=False, pot=pot_q).delete()
                else:
                    order = Order(product=q, costumer=req.user, quantity=quant, change_pot=change_pot, change_soil=change_soil)

                order.save()
                return redirect(reverse("list_view_url"))
            else:

                q = Product.objects.filter(id=pk).first()
                gallery = list(ProductPic.objects.select_related("product").filter(product=q).all())
                gallery.insert(0, q)
                return render(req, template_name="products/detail.html", context={"post": q, "pics": gallery, "form": form})
        else:
            redirect(reverse("login_url"))


class PotDetail(View):

    def get(self, req, pk):
        form = PotOrderForm()
        q = Pot.objects.filter(id=pk).first()
        gallery = list(PotPic.objects.select_related("product").filter(product=q).all())
        for i in gallery:
            x = i
        gallery.insert(0, q)
        return render(req, template_name="products/pot_detail.html", context={"post":q, "pics":gallery, "form":form})

    def post(self, req, pk):
        if req.user.is_authenticated:
            form = PotOrderForm(req.POST)
            if form.is_valid():
                q = Pot.objects.filter(id=pk).first()
    
                order = form.save(commit=False)
                order.pot = q
                order.costumer = req.user

                form.save()
                return redirect(reverse("pot_list_view_url"))

            else:
                q = Pot.objects.filter(id=pk).first()
                gallery = list(PotPic.objects.select_related("product").filter(product=q).all())
                gallery.insert(0, q)
                return render(req, template_name="products/pot_detail.html",
                            context={"post": q, "pics": gallery, "form": form})
        else:
            redirect(reverse("login_url"))


