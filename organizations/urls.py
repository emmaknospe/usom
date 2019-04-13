# organizations/urls.py
from django.urls import path
from organizations import views

urlpatterns = [
    path('organization-view/<int:organization_id>/', views.organization_view, name='organization-view'),
    path('organization-create/', views.create_organization, name='organization-create')
]
