from django.shortcuts import render, get_object_or_404, redirect

from accounts.forms import CustomUserCreationForm
from profiles.models import Profile


def profile_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)

    return render(request, "Profile.html", {"profile": profile})

def create_profile(request):
    def register(request):
        if request.POST:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {"form": form})