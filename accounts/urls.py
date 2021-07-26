from django.urls import path

from .views import (
    register_view,
    login_view,
)

app_name = 'accounts'
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]
