from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Article(models.Model):
    # 안넣으면 생성 못하게 막기 -> views.py 작업, 지금하면 오류 반환
    img = models.ImageField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_user = models.ManyToManyField(User, related_name='like_articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)