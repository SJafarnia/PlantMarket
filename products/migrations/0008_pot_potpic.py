# Generated by Django 4.0.6 on 2022-12-11 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_main_pic_product_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='عنوان')),
                ('img', models.ImageField(null=True, upload_to='media/product', verbose_name='تصویر اصلی')),
                ('caption', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='تعداد')),
                ('is_avail', models.BooleanField(default=False, verbose_name='موجود')),
                ('is_new', models.BooleanField(default=False, verbose_name='جدید')),
                ('is_off', models.BooleanField(default=False, verbose_name='تخفیف خورده')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='قیمت')),
                ('size', models.CharField(blank=True, max_length=10, null=True, verbose_name='سایز')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='تاریخ')),
            ],
            options={
                'verbose_name': 'گلدان',
                'verbose_name_plural': 'گلدان ها',
            },
        ),
        migrations.CreateModel(
            name='PotPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/product')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pic', to='products.pot')),
            ],
            options={
                'verbose_name': 'عکس گلدان',
                'verbose_name_plural': 'گالری گلدان',
            },
        ),
    ]
