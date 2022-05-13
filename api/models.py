from django.db import models


class Product(models.Model):
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.title} -> {self.category}'
