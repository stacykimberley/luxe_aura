from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from products.models import Product



class BagItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} in {self.user.username}'s bag"
