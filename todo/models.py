from django.db import models

# Create your models here.
class Artist(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Song(models.Model):
  name = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  extra = models.CharField(max_length=456)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')

  def __str__(self):
    return self.name