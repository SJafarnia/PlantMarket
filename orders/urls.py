from django.contrib import admin
from django.urls import path, include
from .views import EditOrder, Card, DeleteOrder, ChooseAdd, PayCheck, verf, NewAddr
urlpatterns = [
    path("order-edit/<slug>", EditOrder.as_view(), name="edit-order-url"),
    path("card/delete/<slug>", DeleteOrder.as_view(), name="delete_order_url"),
    path("card/address/", ChooseAdd.as_view(), name="ChooseAddress"),
    path("card/address/n/", NewAddr.as_view(), name="sss"),
    path("card/", Card.as_view(), name="card_url"),
    path("paycheck/<slug>", PayCheck.as_view(), name="paycheck_url"),
    path("payverf/", verf, name="payment_verify"),
    path("paydone/", PayCheck.as_view(), name="payment_done"),

]