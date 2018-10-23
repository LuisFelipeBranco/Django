from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('music/', include('music.urls')),
    path('video/', include('video.urls')),
    path('admin/', admin.site.urls),
]
