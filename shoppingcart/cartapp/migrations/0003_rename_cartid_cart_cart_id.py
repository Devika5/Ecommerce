# Generated by Django 4.2.5 on 2023-10-19 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0002_cart_cartid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cartid',
            new_name='cart_id',
        ),
    ]
