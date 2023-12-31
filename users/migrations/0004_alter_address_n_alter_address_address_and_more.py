# Generated by Django 4.0.6 on 2023-01-05 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_address_options_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='N',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='واحد'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='address',
            name='block',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='پلاک'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='کد پستی'),
        ),
        migrations.AlterField(
            model_name='address',
            name='user_o',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
