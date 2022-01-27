from rest_framework import serializers
from .models import Artist, Song

class ArtistSerializer(serializers.ModelSerializer):
  songs = serializers.StringRelatedField(many=True)

  class Meta:
    model = Artist
    fields = ['name', 'songs']

class SongSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Song
    fields = ['name', 'genre', 'extra', 'artist']