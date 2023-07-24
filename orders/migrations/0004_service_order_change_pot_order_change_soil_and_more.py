# Generated by Django 4.0.6 on 2022-12-11 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_main_pic_product_img_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0003_alter_order_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('is_avail', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'سرویس',
                'verbose_name_plural': 'خدمات',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='change_pot',
            field=models.BooleanField(default=False, verbose_name='تعویض گلدان'),
        ),
        migrations.AddField(
            model_name='order',
            name='change_soil',
            field=models.BooleanField(default=False, verbose_name='تعویض خاک'),
        ),
        migrations.AddField(
            model_name='order',
            name='service3',
            field=models.BooleanField(default=False, verbose_name='سرویس 3'),
        ),
        migrations.AlterField(
            model_name='order',
            name='costumer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='costumers', related_query_name='get_customers', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='order',
            name='final_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='قیمت نهایی'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='پراداخت شده'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_seen',
            field=models.BooleanField(default=False, verbose_name='دیده شده'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_sent',
            field=models.BooleanField(default=False, verbose_name='ارسال شده'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', related_query_name='get_orders', to='products.product', verbose_name='محصول'),
        ),
    ]
