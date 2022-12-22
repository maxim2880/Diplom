from django.urls import path

from . import views

urlpatterns = [

    path('verify', views.BotVerifyView.as_view()),


]