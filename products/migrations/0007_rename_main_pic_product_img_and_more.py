# Generated by Django 4.0.6 on 2022-12-07 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_main_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='main_pic',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='productpic',
            old_name='pic',
            new_name='img',
        ),
    ]