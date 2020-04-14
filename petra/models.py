from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        # These should be PLURAL, lowercase, strings - i.e. "categories"
        verbose_name_plural = "Category"


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)

    # Images should be ImageFields
    image1 = models.TextField()
    image2 = models.TextField(null=True, blank=True)
    image3 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product"
