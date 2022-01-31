from rest_framework import viewsets, permissions
from .serializers import ArtistSerializer, SongSerializer, UserSerializer
from .models import Artist, Song
from django.contrib.auth.models import User

# Create your views here.
class ArtistViewSet(viewsets.ModelViewSet):
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SongViewSet(viewsets.ModelViewSet):
  queryset = Song.objects.all()
  serializer_class = SongSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer