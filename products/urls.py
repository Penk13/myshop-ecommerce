from django.urls import path

from .views import homepage, product_detail


app_name = 'products'
urlpatterns = [
    path('', homepage, name='homepage'),
    path('<int:pk>/', product_detail, name='product-detail'),
]
