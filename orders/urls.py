from django.urls import path

from .views import (
    create_order,
    order_list,
)


app_name = 'orders'
urlpatterns = [
    path('new-order/<int:pk>/', create_order, name='create'),
    path('order-list/', order_list, name='list')
]