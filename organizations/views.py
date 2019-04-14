from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from organizations.forms import OrganizationForm
from organizations.models import Organization


def organization_view(request, organization_id, tab='about'):
    organization = get_object_or_404(Organization, pk=organization_id)
    is_member = False
    if request.user.is_authenticated and request.user.profile:
        if request.user.profile in organization.members.all():
            is_member = True
    return render(request, 'organizations/organization_view_' + tab + '.html', {'organization': organization,
                                                                                'tab': tab,
                                                                                'is_member': is_member})


def get_organizations_by_name(request):
    name = request.GET['name']
    organizations = Organization.objects.filter(name__istartswith=name)
    return render(request, 'organizations/organizations_search_list.html', {'organizations': organizations})

def get_all_organization(request):
    organizations = Organization.objects.order_by("name")
    num_all_orgs = len(organizations)
    return render(request, 'All_Orgs.html', {'organizations': organizations, "num": num_all_orgs})




@login_required
def organization_join(request, organization_id, tab='about'):
    organization = get_object_or_404(Organization, pk=organization_id)
    organization.members.add(request.user.profile)
    organization.save()
    request.user.save()
    return redirect('organization-view-tab', organization_id=organization_id, tab=tab)

@login_required
def organization_leave(request, organization_id, tab='about'):
    organization = get_object_or_404(Organization, pk=organization_id)
    organization.members.remove(request.user.profile)
    organization.save()
    request.user.save()
    return redirect('organization-view-tab', organization_id=organization_id, tab=tab)

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
