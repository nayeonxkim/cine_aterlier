from django.db import models
class Movie(models.Model):
    tmdb_id = models.IntegerField()
    original_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()
    genre_id = models.IntegerField()
    api_category = models.CharField(max_length=20)

class Keyword(models.Model):
    keyword_id = models.IntegerField(primary_key=True)
    keyword_name = models.CharField(max_length=255, null=True)
    movies = models.ManyToManyField(Movie, through="MovieKeyword", related_name='keywords')
  
# Create your models here.
class MovieKeyword(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    tmdb_id = models.IntegerField()
    keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)

