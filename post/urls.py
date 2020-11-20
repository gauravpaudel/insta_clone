from django.urls import path
from .views import index,newPost, postDetail,tags


urlpatterns = [
    path('',index,name='index'),
    path('newpost/',newPost,name='newpost'),
    path('<uuid:post_id>/',postDetail, name='post_detail'),
    path('tags/<slug:tag_slug>/',tags,name='tags'),
   
]