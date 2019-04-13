from django.db import models

from accounts.models import User
from profiles.models import Profile
# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    # TODO: picture
    # TODO: markdownify
    charter = models.CharField(max_length=1000)
    members = models.ManyToManyField(Profile, related_name='organizations')
    admins = models.ManyToManyField(User, related_name='organizations_admined')


class Position(models.Model):
    name = models.CharField(max_length=40)
    organization = models.ForeignKey(Organization, related_name='profiles', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name='positions', null=True, on_delete=models.SET_NULL)
