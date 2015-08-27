from django.db import models

# Create your models here.




class Artist(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    hobby = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True)


class Album(models.Model):
    artist = models.ForeignKey('Artist')
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)


class Track(models.Model):
    album = models.ForeignKey('Album')
    title = models.CharField(max_length=255)
    length = models.IntegerField()
    genre = models.CharField(max_length=255)
