from django.db import models
from products.models import Product, Pot
from users.models import User, Address
from django_jalali.db import models as jmodels


class Order(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name="orders",
        related_query_name="get_orders",
        verbose_name="محصول",
        null=True,
        blank=True,
    )
    costumer = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="costumers",
        related_query_name="get_customers",
        verbose_name="کاربر",
    )
    pot = models.ForeignKey(
        to=Pot,
        on_delete=models.CASCADE,
        related_name="pot",
        related_query_name="get_pots",
        verbose_name="گلدان",
        null=True,
        blank=True,
    )
    quantity = models.IntegerField(default=1)
    d = jmodels.jDateField(
        null=True, auto_now_add=True, auto_now=False, verbose_name="تاریخ خرید"
    )
    final_price = models.IntegerField(
        null=True, blank=True, verbose_name="قیمت نهایی", default=0
    )
    order_date = models.DateTimeField(
        auto_now_add=True, auto_now=False, verbose_name="تاریخ سفارش"
    )
    is_seen = models.BooleanField(default=False, verbose_name="دیده شده")
    is_paid = models.BooleanField(default=False, verbose_name="پراداخت شده")
    is_sent = models.BooleanField(default=False, verbose_name="ارسال شده")
    shipped_date = None
    change_soil = models.BooleanField(default=False, verbose_name="تعویض خاک")
    change_pot = models.BooleanField(default=False, verbose_name="تعویض گلدان")
    service3 = models.BooleanField(default=False, verbose_name="سرویس 3")
    factor = models.ForeignKey(
        to="Factor",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="فاکتور",
        related_name="orders",
        related_query_name="get_orders",
    )

    def save(self, *args, **kwargs):
        if self.is_sent:
            self.shipped_date = jmodels.jDateField(
                null=False, auto_now=True, verbose_name="تاریخ ارسال"
            )
        if self.final_price is not None:
            if self.product and self.pot:
                if not self.change_soil and not self.change_pot:
                    self.final_price = int(self.product.price + self.pot.price) * int(
                        self.quantity
                    )

                if self.change_soil:
                    if self.change_pot:
                        self.final_price = int(
                            self.product.price + self.pot.price + 80000
                        ) * int(self.quantity)
                    elif not self.change_pot:
                        self.final_price = int(
                            self.product.price + self.pot.price + 50000
                        ) * int(self.quantity)

                if self.change_pot:
                    if self.change_soil:
                        self.final_price = int(
                            self.product.price + self.pot.price + 80000
                        ) * int(self.quantity)
                    elif not self.change_soil:
                        self.final_price = int(
                            self.product.price + self.pot.price + 30000
                        ) * int(self.quantity)
            elif self.product:
                if not self.change_soil and not self.change_pot:
                    self.final_price = int(self.product.price) * int(self.quantity)

                if self.change_soil:
                    if self.change_pot:
                        self.final_price = int(self.product.price + 80000) * int(
                            self.quantity
                        )
                    elif not self.change_pot:
                        self.final_price = int(self.product.price + 50000) * int(
                            self.quantity
                        )

                if self.change_pot:
                    if self.change_soil:
                        self.final_price = int(self.product.price + 80000) * int(
                            self.quantity
                        )
                    elif not self.change_soil:
                        self.final_price = int(self.product.price + 30000) * int(
                            self.quantity
                        )
            elif self.pot:
                self.final_price = int(self.pot.price) * int(self.quantity)

        return super(Order, self).save(*args, **kwargs)

    def __str__(self):
        if self.product:
            return f"{self.product.name} - {self.d}"
        if self.pot:
            return f"{self.pot.name}"

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش ها"


class Factor(models.Model):
    date = jmodels.jDateField(
        null=True, auto_now_add=True, auto_now=False, verbose_name="تاریخ فاکتور"
    )
    costumer = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="costumer",
        related_query_name="get_customer",
        verbose_name="کاربر",
    )
    factor_n = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="شماره فاکتور"
    )
    factor_final_price = models.IntegerField(default=0, verbose_name="قیمت نهایی")
    to = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        related_name="facotraddress",
        related_query_name="get_address",
        verbose_name="ادرس",
        null=True,
    )
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده")

    def save(self, *args, **kwargs):
        if self.order_set.all():
            for item in self.order_set.all():
                self.factor_final_price += item.final_price
        super(Factor, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "فاکتور"
        verbose_name_plural = "فاکتور ها"

    def __str__(self):
        return self.factor_n


class ShipmentMethods(models.Model):
    method = models.CharField(max_length=100, null=True, blank=True, verbose_name="روش")
    price = models.IntegerField(null=True, blank=True, verbose_name="بها", default=0)

    class Meta:
        verbose_name = "روش ارسال"
        verbose_name_plural = "روش های ارسال"

    def __str__(self):
        return f"روش ارسال : {self.method} - {self.price} تومان "


class Payment(models.Model):
    pay_id = models.CharField(max_length=50, verbose_name="ایدی رسید")
    verf_track_id = models.CharField(
        max_length=50, null=True, verbose_name="ایدی استعلام پرداخت"
    )
    track_id = models.CharField(max_length=50, null=True, verbose_name="ایدی پرداخت")
    pay_link = models.CharField(max_length=200, verbose_name="لینک پرداخت")
    status = models.CharField(max_length=10, null=True, verbose_name="وضعیت پرداخت")
    order_id = models.CharField(max_length=50, verbose_name="ایدی سفارش")
    is_verified = models.BooleanField(default=False, verbose_name="تایید شده")
    factor = models.OneToOneField(
        to=Factor, on_delete=models.SET_NULL, null=True, verbose_name="فاکتور"
    )

    class Meta:
        verbose_name = "رسید پرداخت"
        verbose_name_plural = "پرداخت ها"

    def save(self, *args, **kwargs):
        if self.status == "100":
            self.is_verified = True
        super(Payment, self).save(*args, **kwargs)


class Service(models.Model):
    name = models.CharField(max_length=50, verbose_name="عنوان")
    price = models.IntegerField(verbose_name="قیمت")
    is_avail = models.BooleanField(default=False, verbose_name="موجود")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "سرویس"
        verbose_name_plural = "خدمات"
