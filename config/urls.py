from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from todo.views import ArtistViewSet, SongViewSet, UserViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('artist', ArtistViewSet)
router.register('song', SongViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
]