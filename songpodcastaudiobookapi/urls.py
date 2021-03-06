from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('songs',views.Songs_File,basename='songs')
router.register('podcasts',views.Podcasts_File,basename='podcasts')
router.register('audiobooks',views.Audiobooks_File,basename='audiobooks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls),name='home')
]
