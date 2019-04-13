# organizations/urls.py
from django.urls import path
from organizations import views

urlpatterns = [
    path('organization-view/<int:organization_id>/', views.organization_view, name='organization-view'),
    path('organization-view/<int:organization_id>/<slug:tab>/', views.organization_view, name='organization-view-tab'),
    path('organization-join/<int:organization_id>/', views.organization_join, name='organization-join'),
    path('organization-join/<int:organization_id>/<slug:tab>/', views.organization_join, name='organization-join-tab'),
    path('organization-create/', views.create_organization, name='organization-create')
]
