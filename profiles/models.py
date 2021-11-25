from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # settings.AUTH_USER_MODEL
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
