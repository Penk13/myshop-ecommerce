from django.db import models

from products.models import Product
from accounts.models import Profile

STATUS = (
    ("CREATED", "Created"),
    ("IN_PROCESS", "In Process"),
    ("SUCCESS", "Success"),
)


class Order(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Product)

    quantity = models.IntegerField(default=0)
    address = models.CharField(max_length=80)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS, default="CREATED")
    date_created = models.DateField(auto_now_add=True)

    # Show order id on admin page
    def __str__(self):
        return str(self.id)
