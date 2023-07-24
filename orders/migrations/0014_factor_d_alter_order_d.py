# Generated by Django 4.0.6 on 2023-01-03 15:05

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_alter_order_d'),
    ]

    operations = [
        migrations.AddField(
            model_name='factor',
            name='d',
            field=django_jalali.db.models.jDateField(auto_now_add=True, null=True, verbose_name='تاریخ خرید'),
        ),
        migrations.AlterField(
            model_name='order',
            name='d',
            field=django_jalali.db.models.jDateField(auto_now_add=True, null=True, verbose_name='تاریخ خرید'),
        ),
    ]