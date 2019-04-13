from django.db import models

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    # TODO: picture
    # TODO: markdownify
    charter = models.CharField(max_length=1000)
    # TODO: members
    # members = models.ManyToManyField(profiles.Profile)
