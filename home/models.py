from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(help_text="Volume in ml")
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name