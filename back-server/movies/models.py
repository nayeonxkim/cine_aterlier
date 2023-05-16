from django.db import models

# Create your models here.
class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()
    genre_id = models.IntegerField()

