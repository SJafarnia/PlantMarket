from django.contrib import admin
from .models import Product, ProductPic, PotPic, Pot, ProductVisit


class ProductPicInline(admin.TabularInline):
    model = ProductPic


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity", "is_avail", "price", "d", "is_off", "size", 'img', "date"]
    list_editable = ["quantity", "price", "is_off", 'img']
    list_filter = ('name', )
    inlines = [ProductPicInline]


admin.site.register(Product, ProductAdmin)


class ProductPicAdmin(admin.ModelAdmin):
    list_display = ["product", "img"]
    list_editable = ["img"]


admin.site.register(ProductPic, ProductPicAdmin)


class PotPicInline(admin.TabularInline):
    model = PotPic


class PotAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity", "is_avail", "price", "d", "is_off", "size", 'img', "date"]
    list_editable = ["quantity", "price", "is_off", 'img']
    inlines = [PotPicInline]


admin.site.register(Pot, PotAdmin)


class PotPicAdmin(admin.ModelAdmin):
    list_display = ["product", "img"]
    list_editable = ["img"]


admin.site.register(PotPic, PotPicAdmin)


class VisitAdmin(admin.ModelAdmin):
    # readonly_fields = ["product", "pot", "ip", "costumer"]
    readonly_fields =  [field.name for field in ProductVisit._meta.fields]
admin.site.register(ProductVisit, VisitAdmin)
