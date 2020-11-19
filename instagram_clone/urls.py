
from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [

    path('',include('post.urls')),

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

