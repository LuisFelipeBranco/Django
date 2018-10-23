from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=25)

class size_of_cape(models.Model):
    size = models.CharField(max_length=10)
