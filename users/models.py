from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)
    email_active_code = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to="media/userprofiles", null=True, blank=True, validators=[validate_image_file_extension])
    # is_staff = False
    # add = models.ForeignKey(to="Address", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"


class Address(models.Model):
    user_o = models.ForeignKey(to="User", on_delete=models.CASCADE, null=True, verbose_name="کاربر")
    address = models.TextField(null=True, blank=True, verbose_name="ادرس")
    postal_code = models.CharField(max_length=10,null=True, blank=True, verbose_name="کد پستی")
    block = models.CharField(max_length=6,null=True, blank=True, verbose_name="پلاک")
    N = models.CharField(max_length=5, null=True, blank=True, verbose_name='واحد')


    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس ها"
