from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from organizations.forms import OrganizationForm, PositionForm
from organizations.models import Organization, Position
from profiles.models import Profile


def organization_view(request, organization_id, tab='about'):
    organization = get_object_or_404(Organization, pk=organization_id)
    is_member = False
    is_admin = False
    if request.user.is_authenticated and request.user.profile:
        if request.user.profile in organization.members.all():
            is_member = True
        if request.user in organization.admins.all():
            is_admin = True
    return render(request, 'organizations/organization_view_' + tab + '.html', {'organization': organization,
                                                                                'tab': tab,
                                                                                'is_member': is_member,
                                                                                'is_admin': is_admin})


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


def organization_manage_positions(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    if request.POST:
        form = PositionForm(request.POST)
        if form.is_valid():
            position = form.save(commit=False)
            assert isinstance(position, Position)
            position.organization = organization
            position.save()
    else:
        form = PositionForm()
    positions = Position.objects.filter(organization_id=organization.id)
    return render(request, 'organizations/manage_positions.html', {'positions': positions, 'form': form,
                                                                   'organization': organization})


def assign_user(request, organization_id, position_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    profiles = organization.members.all()
    position = get_object_or_404(Position, pk=position_id)
    print(profiles)
    return render(request, 'organizations/assign_user.html', {'organization': organization,
                                                              'position': position, 'profiles': profiles})


def assign_user_process(request, organization_id, position_id, profile_id):
    position = get_object_or_404(Position, pk=position_id)
    position.profile = get_object_or_404(Profile, pk=profile_id)
    position.save()
    return redirect('organization-manage-positions', organization_id=organization_id)
