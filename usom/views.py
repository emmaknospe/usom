from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import CustomUserCreationForm

def index(request):
    if request.user.is_authenticated:
        if hasattr(request.user, "profile"):
            return redirect("profile-view", profile_id = request.user.profile.id)
    return render(request, "index.html", {"user": request.user, 'form': CustomUserCreationForm()})

