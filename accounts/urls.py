# accounts/urls.py
from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('link_profile/', views.link_profile, name='link_profile'),
    path('confirm_link/<int:profile_id>/', views.confirm_link, name="confirm_link"),
    path('custom_link/', views.custom_link, name="custom_link"),
    path('finalize_link/<int:profile_id>/<slug:token>/', views.finalize_link, name='finalize-link')
]


