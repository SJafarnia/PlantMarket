# Generated by Django 4.0.6 on 2022-12-06 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_avail',
            field=models.BooleanField(default=False, verbose_name='موجود'),
        ),
        migrations.CreateModel(
            name='ProductPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='media/product')),
                ('r_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
