import django.contrib.auth as auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import CustomUserCreationForm


def register(request):
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {"form": form})


def link_profile(request):
    return None


def confirm_link(request):
    return None


def custom_link(request):
    return None


def finalize_link(request):
    return None

