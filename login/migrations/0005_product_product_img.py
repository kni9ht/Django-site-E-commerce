# Generated by Django 2.2.17 on 2020-12-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_remove_product_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(default='assets/img/error.png', height_field=273, upload_to=None, width_field=218),
        ),
    ]
