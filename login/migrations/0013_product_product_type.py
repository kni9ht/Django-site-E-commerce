# Generated by Django 2.2.17 on 2020-12-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_product_product_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(default='', max_length=50),
        ),
    ]