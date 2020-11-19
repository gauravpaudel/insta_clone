from django.urls import path
from .views import index,newPost


urlpatterns = [
    path('',index,name='index'),
    path('newpost/',newPost,name='newpost')
   
]