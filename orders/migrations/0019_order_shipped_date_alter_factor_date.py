# Generated by Django 4.0.6 on 2023-02-12 12:50

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_shipmentmethods'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped_date',
            field=django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ ارسال'),
        ),
        migrations.AlterField(
            model_name='factor',
            name='date',
            field=django_jalali.db.models.jDateField(auto_now_add=True, verbose_name='تاریخ فاکتور'),
        ),
    ]
