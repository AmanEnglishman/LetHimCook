from django.contrib.auth.models import User
from django.db import models

from apps.product.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart for {self.user.email} / Product {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Wishlist for {self.user.email} / Product {self.product.name}'
