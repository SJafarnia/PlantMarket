from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from orders.models import Order, ShipmentMethods
from django.forms import ModelChoiceField
from users.models import Address
from products.models import Pot

CH = (
    # ('',''),
    ("change_soil", "تعویض خاک"),
    ("change_pot", "تعویض گلدان"),
    ("r_p", "سفارش گلدان مورد نظر پس از ثبت سفارش حذف شود؟"),
)


class Services(forms.Form):
    s = forms.MultipleChoiceField(
        choices=CH, label="خدمات", required=False, widget=forms.CheckboxSelectMultiple
    )
    quantity = forms.IntegerField(
        label="تعداد",
        initial=1,
        validators=[
            validators.MinValueValidator(
                limit_value=1, message="حداقل 1 محصول انتخاب کنید"
            )
        ],
    )

    def __init__(self, user, *args, **kwargs):
        super(Services, self).__init__(*args, **kwargs)
        if user.is_authenticated:
            self.fields["pot"] = forms.ModelChoiceField(
                queryset=Order.objects.select_related("pot")
                .filter(costumer=user, product=None, is_paid=False)
                .all(),
                required=False,
                label="گلدان",
            )


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        super(ModelChoiceField, self).__init__()
        return f"{obj.name}"


class PotOrderForm(forms.ModelForm):
    quantity = forms.IntegerField(
        label="تعداد",
        initial=1,
        validators=[
            validators.MinValueValidator(
                limit_value=1, message="حداقل 1 محصول انتخاب کنید"
            )
        ],
    )

    class Meta:
        model = Order
        fields = ["quantity"]


class Quantity(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["quantity"]


class ChosenAddress(forms.Form):
    postal_code = forms.CharField(max_length=10)


class PayMethodForm(forms.Form):
    method = forms.ModelChoiceField(
        queryset=ShipmentMethods.objects.all(), label="نحوه ارسال"
    )


class ChoseAddressForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(ChoseAddressForm, self).__init__(*args, **kwargs)
        self.fields["to"] = forms.ModelChoiceField(
            queryset=Address.objects.filter(user_o=user), required=False, label="آدرس"
        )
