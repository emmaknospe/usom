from organizations.models import Organization
from usom.forms import CustomModelForm


class OrganizationForm(CustomModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'short_name', 'description']
