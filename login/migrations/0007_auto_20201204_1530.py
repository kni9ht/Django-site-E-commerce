# Generated by Django 2.2.17 on 2020-12-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20201204_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(
                height_field=273, upload_to=b'product_img', width_field=218),
        ),
    ]
