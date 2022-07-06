from django.db import models
from django.contrib.auth import get_user_model

from apps.category.models import Category

User = get_user_model()


class Product(models.Model):
    product_name = models.CharField(max_length=80, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category')
    in_stock = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=1)
    imgs = models.ImageField(blank=True, null=True, upload_to='images', default="api_pic/wblogo.jpeg")

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Image')

    def __str__(self):
        return self.product.product_name


