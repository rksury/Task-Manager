from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile_number = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return self.email


class Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
