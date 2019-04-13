from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import CustomUserCreationForm


def index(request):
    return render(request, "index.html", {"user": request.user, 'form': CustomUserCreationForm()})

