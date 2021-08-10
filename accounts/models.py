from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    bio = models.TextField(blank=True)
    address = models.CharField(max_length=80, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)

    # Show username on admin page
    def __str__(self):
        return self.user.username
