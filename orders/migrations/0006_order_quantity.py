# Generated by Django 4.0.6 on 2022-12-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_pot_alter_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
