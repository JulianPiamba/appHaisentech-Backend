# Generated by Django 5.0.6 on 2024-06-13 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_paymentmethod_role_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='pro_products',
            new_name='products',
        ),
    ]
