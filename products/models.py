from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()

    # show category name in admin
    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=5)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    # show product name in admin
    def __str__(self):
        return self.name
