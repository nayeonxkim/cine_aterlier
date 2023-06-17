from django.db import models
from django.conf import settings

class Movie(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    original_language = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField(null=True)
    poster_path = models.TextField(null=True)
    genre_id = models.IntegerField()
    adult = models.BooleanField(default=False)
    popularity = models.DecimalField(default=None, max_digits=20, decimal_places=3)
    vote_average = models.DecimalField(max_digits=20, decimal_places=1)
    vote_count = models.IntegerField()

class Keyword(models.Model):
    keyword_id = models.IntegerField(primary_key=True)
    keyword_name = models.CharField(max_length=255, null=True)
    movies = models.ManyToManyField(Movie, through="MovieKeyword", related_name='keywords')
  
# Create your models here.
class MovieKeyword(models.Model):
    tmdb_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    score = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class KarloImg(models.Model):
    movie_id1 = models.IntegerField()
    movie_id2 = models.IntegerField()
    original_title1 = models.CharField(max_length=255)
    original_title2 = models.CharField(max_length=255)
    painter = models.CharField(max_length=255)
    img_url = models.ImageField(upload_to='karloResults/')

