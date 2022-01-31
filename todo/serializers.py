from rest_framework import serializers
from .models import Artist, Song
from django.contrib.auth.models import User

class ArtistSerializer(serializers.ModelSerializer):
  songs = serializers.StringRelatedField(many=True)

  class Meta:
    model = Artist
    fields = '__all__'


class SongSerializer(serializers.ModelSerializer):

  class Meta:
    model = Song
    fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']