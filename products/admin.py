from django.contrib import admin

from .models import Product, Category


# register to admin page so we can see the tables/models
admin.site.register(Product)
admin.site.register(Category)
