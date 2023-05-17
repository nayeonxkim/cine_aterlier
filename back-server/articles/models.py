from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     pass

class Article(models.Model):
    img = models.ImageField(blank=False) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_user = models.ManyToManyField(User, related_name='like_articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)