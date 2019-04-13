from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.CharField(max_length=100)

    def get_full_name(self):
        return self.first_name + " " + self.last_name
