from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from todo.views import ArtistViewSet, SongViewSet

router = routers.DefaultRouter()
router.register('artist', ArtistViewSet)
router.register('song', SongViewSet)

urlpatterns = [
  path('', include(router.urls))
]