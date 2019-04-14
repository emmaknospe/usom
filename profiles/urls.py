from django.urls import path

from . import views

urlpatterns = [
    path('<int:profile_id>/', views.profile_view, name="profile-view"),
    path("create-profile", views.create_profile, name="create-profile"),
    path('<int:profile_id>/<slug:tab>/', views.profile_view, name='profile_view_tab'),
    path('user-recommend', views.get_user_recommended, name="user_recon")

]