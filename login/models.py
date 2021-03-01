from django.db import models


class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    product_des = models.CharField(
        max_length=300, default="product description")
    product_date = models.DateField(auto_now=True)
    product_img = models.ImageField(default="")
    product_value = models.IntegerField(default=1)
    product_type = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.product_name
