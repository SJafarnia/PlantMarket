from django.db import models
from django_jalali.db import models as jmodels
from users.models import User
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="عنوان")
    img = models.ImageField(upload_to="media/product", null=True, verbose_name="تصویر اصلی")
    caption = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    quantity = models.IntegerField(null=True, blank=True, default=0, verbose_name="تعداد")
    is_avail = models.BooleanField(verbose_name="موجود", default=False)
    is_new = models.BooleanField(default=False, verbose_name="جدید")
    is_off = models.BooleanField(default=False, verbose_name="تخفیف خورده")
    price = models.IntegerField(null=True, blank=True, verbose_name="قیمت")
    size = models.CharField(max_length=10, null=True, blank=True, verbose_name="سایز")
    date = models.DateTimeField(auto_now=True, verbose_name="تاریخ میلادی")
    d = jmodels.jDateField(null=True, auto_now_add=True, auto_now=False, verbose_name="تاریخ")

    def save(self, *args, **kwargs):
        if self.quantity == 0 or self.quantity < 0:
            self.is_avail = False
            self.quantity = 0
        elif self.quantity > 0:
            self.is_avail = True
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        
        return reverse("detail_view_url", kwargs={"pk":self.id})


    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class Pot(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="عنوان")
    img = models.ImageField(upload_to="media/product", null=True, verbose_name="تصویر اصلی")
    caption = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    quantity = models.IntegerField(null=True, blank=True, default=0, verbose_name="تعداد")
    is_avail = models.BooleanField(verbose_name="موجود", default=False)
    is_new = models.BooleanField(default=False, verbose_name="جدید")
    is_off = models.BooleanField(default=False, verbose_name="تخفیف خورده")
    price = models.IntegerField(null=True, blank=True, verbose_name="قیمت")
    size = models.CharField(max_length=10, null=True, blank=True, verbose_name="سایز")
    date = models.DateTimeField(auto_now=True, verbose_name="تاریخ میلادی")
    d = jmodels.jDateField(null=True, auto_now_add=True, auto_now=False, verbose_name="تاریخ")

    def save(self, *args, **kwargs):
        if self.quantity == 0 or self.quantity < 0:
            self.is_avail = False
            self.quantity = 0
        elif self.quantity > 0:
            self.is_avail = True
        super(Pot, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "گلدان"
        verbose_name_plural = "گلدان ها"


class ProductPic(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=True, related_name="pic")
    img = models.ImageField(upload_to="media/product")

    class Meta:
        verbose_name = " عکس محصول"
        verbose_name_plural = "گالری محصولات"


class PotPic(models.Model):
    product = models.ForeignKey(to=Pot, on_delete=models.CASCADE, null=True, related_name="pic")
    img = models.ImageField(upload_to="media/product")

    class Meta:
        verbose_name = "عکس گلدان"
        verbose_name_plural = "گالری گلدان"


class ProductVisit(models.Model):

    product = models.ForeignKey(to=Product, null=True, blank=True, on_delete=models.CASCADE, related_name="product_visits", verbose_name="بازدید محصولات")
    pot = models.ForeignKey(to=Pot, blank=True, null=True, on_delete=models.CASCADE, related_name="pot_visits", verbose_name="بازدید گلدان ها")
    ip = models.CharField(max_length=15, verbose_name="آی پی کاربر")
    costumer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="visiting_costumer",
                                related_query_name="get_visiting_customers", verbose_name="کاربر بازدید کننده",
                                null=True, blank=True)
    

    def save(self, *args, **kwargs):
        if self.product == None and self.pot == None:
            raise ValueError("both F keys cannot be null")
        else:
            super(ProductVisit, self).save(*args, **kwargs)

    def __str__(self):
        if self.product == None and self.pot == None:
            raise ValueError("both F keys cannot be null")
        elif self.product != None:
            return f"{self.product.name} / {self.ip}" 
        elif self.pot != None:
            return f"{self.pot.name} / {self.ip}" 
        

    class Meta:
        verbose_name = "بازدید"
        verbose_name_plural = "بازدید ها"

        