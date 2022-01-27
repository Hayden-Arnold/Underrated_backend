from rest_framework import viewsets
from .serializers import ArtistSerializer, SongSerializer
from .models import Artist, Song

# Create your views here.

class ArtistViewSet(viewsets.ModelViewSet):
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer

class SongViewSet(viewsets.ModelViewSet):
  queryset = Song.objects.all()
  serializer_class = SongSerializer