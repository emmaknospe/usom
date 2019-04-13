from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

from profiles.models import Profile


class User(AbstractUser):
    email = models.CharField(max_length=100)
    profile = models.OneToOneField(to=Profile, on_delete= models.SET_NULL, null = True)

    def get_full_name(self):
        return self.first_name + " " + self.last_name
