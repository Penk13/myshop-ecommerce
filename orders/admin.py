from django.contrib import admin

from .models import Order


# @admin.register(Order)
# Modify admin site
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'products', 'address', 'quantity', 'total_price', 'date_created')


admin.site.register(Order, OrderAdmin)
