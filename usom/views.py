from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

from accounts.forms import CustomUserCreationForm

def index(request):
    if request.user.is_authenticated:
        if request.user.profile:
            return redirect("profile-view", profile_id = request.user.profile.id)
        else:
            return redirect("create-profile")
    return render(request, "index.html", {"user": request.user, 'form': CustomUserCreationForm()})

