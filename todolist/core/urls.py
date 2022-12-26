
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views as rest_views

from . import views

urlpatterns = [
    path('signup', views.RegistrationView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('update_password', views.UpdatePasswordView.as_view(), name='update password'),
    path('token_login', rest_views.obtain_auth_token),
]
