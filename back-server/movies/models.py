from django.db import models

class Movie(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    original_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()
    genre_id = models.IntegerField()
    adult = models.BooleanField(default=False)
    popularity = models.DecimalField(default=None, max_digits=20, decimal_places=2)

class Keyword(models.Model):
    keyword_id = models.IntegerField(primary_key=True)
    keyword_name = models.CharField(max_length=255, null=True)
    movies = models.ManyToManyField(Movie, through="MovieKeyword", related_name='keywords')
  
# Create your models here.
class MovieKeyword(models.Model):
    tmdb_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)

