# organizations/urls.py
from django.urls import path
from organizations import views

urlpatterns = [
    path('organization-view/<int:organization_id>/', views.organization_view, name='organization-view'),
    path('organization-view/<int:organization_id>/<slug:tab>/', views.organization_view, name='organization-view-tab'),
    path('organization-join/<int:organization_id>/<slug:tab>/', views.organization_join, name='organization-join'),
    path('organization-leave/<int:organization_id>/<slug:tab>/', views.organization_leave, name='organization-leave'),
    path('organization-manage-positions/<int:organization_id>/', views.organization_manage_positions, name='organization-manage-positions'),
    path('organization-create/', views.create_organization, name='organization-create'),
    path('get-organizations-by-name/', views.get_organizations_by_name, name='get-organizations-by-name'),
    path("all-orgs/", views.get_all_organization, name = 'get-all-organizations'),
    path('assign-user/<int:organization_id>/<int:position_id>/', views.assign_user, name='assign-user'),
    path('assign-user-process/<int:organization_id>/<int:position_id>/<int:profile_id>/', views.assign_user_process, name='assign-user-process')


]
