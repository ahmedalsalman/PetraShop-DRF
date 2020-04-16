from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey( Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=10)
    image1 = models.ImageField(max_length=150)
    image2 = models.ImageField(max_length=150, null=True, blank=True)
    image3 = models.ImageField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product"

    
class CartItem(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, blank=True)
    count= models.PositiveIntegerField(default=1)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(CartItem, blank=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    created = models.DateTimeField(default=datetime.now())

class Order(models.Model):
    products = models.ManyToManyField(Product) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now())
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)

@receiver(post_save, sender=get_user_model())
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)