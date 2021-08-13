from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Show category name on admin page
    def __str__(self):
        return self.name


class Product(models.Model):
    # order = models.ManyToManyField(Order)

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    stock = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, blank=True)
    image = models.ImageField(upload_to='products/')  # automatically upload to MEDIA_ROOT/products/

    def available(self):
        return self.stock > 0

    # Show product name on admin page
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"pk": self.pk})
