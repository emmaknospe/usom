from django.shortcuts import render

# Create your views here.
from accounts.forms import CustomUserCreationForm


def register(request):
    return render(request, 'registration/register.html', {"form": CustomUserCreationForm()})


def link_profile(request):
    return None


def confirm_link(request):
    return None


def custom_link(request):
    return None


def finalize_link(request):
    return None

