# Generated by Django 4.0.6 on 2023-01-03 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_factor_d_alter_order_d'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factor',
            name='factor_final_price',
            field=models.IntegerField(default=0, verbose_name='قیمت نهایی'),
        ),
        migrations.AlterField(
            model_name='factor',
            name='factor_n',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='شماره فاکتور'),
        ),
        migrations.AlterField(
            model_name='order',
            name='factor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.factor', verbose_name='فاکتور'),
        ),
        migrations.AlterField(
            model_name='service',
            name='is_avail',
            field=models.BooleanField(default=False, verbose_name='موجود'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=50, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
    ]
