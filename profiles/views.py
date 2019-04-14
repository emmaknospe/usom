from django.shortcuts import render, get_object_or_404, redirect

from accounts.forms import CustomUserCreationForm
from profiles.Forms import ProfileForm
from profiles.models import Profile


def profile_view(request, profile_id, tab='About'):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, "Profiles/Profile_"+tab+".html", {"profile": profile})

def create_profile(request):
        if request.POST:
            form = ProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                request.user.profile = profile
                request.user.save()
                return redirect('profile-view', profile_id=profile.id)
        else:
            form = ProfileForm()
        return render(request, 'forms/base-form.html', {"form": form, "form_title": "Create Profile", "form_action": "Create Profile"})