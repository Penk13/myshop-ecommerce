from django.urls import path

from .views import (
    create_order,
    delete_order,
    order_list,
    order_detail,
)


app_name = 'orders'
urlpatterns = [
    path('new-order/<int:pk>/', create_order, name='create'),
    path('delete/<int:pk>/', delete_order, name='delete'),
    path('order-list/', order_list, name='list'),
    path('<int:pk>/', order_detail, name='detail'),
]
