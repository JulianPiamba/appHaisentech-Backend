# Generated by Django 5.0.6 on 2024-06-13 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_usr_password_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pro_review',
            field=models.IntegerField(null=True),
        ),
    ]
