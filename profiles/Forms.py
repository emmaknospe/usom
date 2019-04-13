from profiles.models import Profile
from usom.forms import CustomModelForm

class ProfileForm(CustomModelForm):
    class Meta:
        model = Profile
        fields =["first_name", "last_name", "class_year", "email"]