from django.urls import path

from .views import create_order


app_name = 'orders'
urlpatterns = [
    path('new-order/<int:pk>/', create_order, name='create'),
]