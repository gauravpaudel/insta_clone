from django.urls import path
from django.shortcuts import render
from .views import Profile_View,Update_Profile

urlpatterns = [
    path('<int:pk>/',Profile_View.as_view(), name='profile'),
    path('edit-profile/<int:pk>/',Update_Profile.as_view(),name='update_profile'),

]