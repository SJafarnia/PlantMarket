from django.contrib import admin
from .models import Order, Service, Factor, ShipmentMethods, Payment
from django_jalali.admin.filters import JDateFieldListFilter

# you need import this for adding jalali calendar widget
import django_jalali.admin as jadmin




@admin.register(Factor)
class FactorManager(admin.ModelAdmin):
    list_display = ["costumer", "date", "factor_final_price", "factor_n"]
    readonly_fields =  [field.name for field in Factor._meta.fields]
    list_filter = (
        ('date', JDateFieldListFilter),
    )

@admin.register(Service)
class ServiceManager(admin.ModelAdmin):
    list_display = ["name", "price"]

@admin.register(ShipmentMethods)
class ShipManager(admin.ModelAdmin):
    list_display = ["method", "price"]

@admin.register(Payment)
class PayManager(admin.ModelAdmin):
    list_display = ["pay_id", "verf_track_id", "track_id", "pay_link", "order_id", "is_verified", 'factor']


@admin.register(Order)
class OrderManager(admin.ModelAdmin):
    list_display = ["product", "costumer","pot", "final_price", "change_soil", "change_pot", "d", "factor"]
    readonly_fields  =  [field.name for field in Order._meta.fields if field.name =="factor"]
    list_filter = (
        ('d', JDateFieldListFilter),
    )

