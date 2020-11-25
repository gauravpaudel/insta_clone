from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile


class Profile_View(LoginRequiredMixin, DetailView):

    permission_denied_message = 'Please login'
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    
class Update_Profile(LoginRequiredMixin,UpdateView):
    permission_denied_message = 'Please login'
    model = Profile
    template_name = 'pupdateform.html'
    fields = ['location','website','bio']
    
    def get_success_url(self):
        return reverse('profile',kwargs={'pk':self.object.id})
