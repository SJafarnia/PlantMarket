from django.contrib import admin
from .models import User, Address
# Register your models here.
admin.site.register(Address)

class UserAdmin(admin.ModelAdmin):
    list_display = ["username","phone","email"]


admin.site.register(User, UserAdmin)
