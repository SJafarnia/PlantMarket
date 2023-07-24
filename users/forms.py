from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from .models import User, Address


class UserLoginForm(forms.Form):
    username = forms.CharField(label="نام کاربری", required=True, validators=[
        validators.MaxLengthValidator(50, "must be less than 50 characters"),
        validators.MinLengthValidator(4, "must be at least 4 characters")
    ],
                               widget=forms.TextInput
                               (attrs={'class': ''}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': ''}),
                               validators=[
                                   validators.MaxLengthValidator(50, "must be less than 16 characters"),
                                   validators.MinLengthValidator(8, "must be at least 8 characters")
                               ]
                               )


class UserSignUpForm(forms.Form):

    first_name = forms.CharField(label="نام", required=True, validators=[
        validators.MaxLengthValidator(30, "نام شما نمیتواند بیشتر از 30 کاراکتر باشد"),
        validators.MinLengthValidator(2, "نام شما باید حداقل شامل 2 حرف باشد")
    ],
                               widget=forms.TextInput
                               (attrs={'class': ''}))
    last_name = forms.CharField(label="نام خانوادگی", required=True, validators=[
        validators.MaxLengthValidator(30, "نام خانوادگی نمیتواند بیشتر از 30 کارکتر باشد"),
        validators.MinLengthValidator(2, "نام خانوادگی شما باید حداقل شامل 2 حرف باشد")
    ],
                                 widget=forms.TextInput
                                 (attrs={'class': ''}))

    phone = forms.IntegerField(label="تلفن همراه")
    email = forms.EmailField(label="امیل", required=False)
    password = forms.CharField(widget=forms.PasswordInput(),
                               validators=[
                                   validators.MaxLengthValidator(16, "رمز عبور بیشتر از 16 کاراکتر پشتیبانی نمیشود"),
                                   validators.MinLengthValidator(8, "رمز عبور باید حداقل شامل 8 کاراکتر باشد")
                               ])
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password == confirm_password:
            return confirm_password

        raise ValidationError("پسورد همخوانی ندارد")

    def clean_username(self):
        # username = self.cleaned_data.get("username")
        # email = self.cleaned_data.get("email")
        phone= self.cleaned_data.get("phone")
        qs = User.objects.filter(phone= phone)
        if qs.exists():
            raise forms.ValidationError("این شماره قبلا ثبت شده است!")
        return phone


class Profile(forms.Form):
    username = forms.CharField(max_length=50)
    phone = forms.NumberInput()
    email= forms.EmailField()


class SmsVerifyForm(forms.Form):
    code = forms.CharField(max_length=6)
    userId =  forms.IntegerField(widget=forms.HiddenInput)


class AddressForm(forms.ModelForm):
    postal_code = forms.CharField(max_length=10, label= "کد پستی",validators=[
        validators.MaxLengthValidator(10, message="کد پستی بیشتر از 10 رقم قابل قبول نیست"),
        validators.MinLengthValidator(10,message="کد پستی کمتر از 10 رقم مجاز نیست")])
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    # address = forms.Textarea()
    N = forms.CharField(max_length=5, required=True, label="واحد")
    block = forms.CharField(max_length=5, required=True, label="پلاک")

    class Meta:
        model = Address
        fields = "__all__"
        exclude = ["user_o"]