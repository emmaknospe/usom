from organizations.models import Organization, Position
from usom.forms import CustomModelForm


class OrganizationForm(CustomModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'short_name', 'description']


class PositionForm(CustomModelForm):
    class Meta:
        model = Position
        fields = ['name']