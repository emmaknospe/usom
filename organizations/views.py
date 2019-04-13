from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from organizations.forms import OrganizationForm
from organizations.models import Organization


def organization_view(request, organization_id):
    return render('organizations/organization_view.html', {'organization': get_object_or_404(Organization,
                                                                                             id=organization_id)})


@login_required
def create_organization(request):
    if request.POST:
        form = OrganizationForm(request.POST)
        if form.is_valid():
            org = form.save(commit=False)
            assert isinstance(org, Organization)
            org.save()
            org.admins.add(request.user)
            return redirect('organization-view', organization_id=org.id)
    else:
        form = OrganizationForm()
    return render(request, 'forms/base-form.html', {'form': form, 'form_title': 'Create Organization',
                                                    'form_action': 'Create'})
