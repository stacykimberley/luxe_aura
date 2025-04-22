from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=100)
    volume = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
