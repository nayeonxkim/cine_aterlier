from django.db import models
from accounts.models import User

class Article(models.Model):
    img = models.ImageField(blank=False) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_user = models.ManyToManyField(User, blank=True, related_name='like_articles')
    title = models.CharField(max_length=100)
    content = models.TextField()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()