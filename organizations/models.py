from django.db import models
from django.db.models import Count, FloatField, Q
from django.db.models.functions import Cast

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

    def get_all_emails(self):
        base = "mailto:"
        for profile in self.members.all():
            base += profile.email + ","
        return base

    def get_recommended_organizations(self):
        return Organization.objects.annotate(
            relevance=Cast(100 * Count('members', filter=Q(members__in=self.members.all())), FloatField()) / Cast(
                Count('members'), FloatField())).order_by('-relevance')[1:6]



class Position(models.Model):
    name = models.CharField(max_length=40)
    organization = models.ForeignKey(Organization, related_name='profiles', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name='positions', null=True, on_delete=models.SET_NULL)
