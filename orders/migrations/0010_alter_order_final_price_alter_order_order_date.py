# Generated by Django 4.0.6 on 2023-01-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='final_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='قیمت نهایی'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now_add=True, verbose_name='تاریخ سفارش'),
        ),
    ]
