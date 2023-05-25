from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.serializers import ArticleSerializer, ArticleLikeSerializer
User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id', 'username')

class UserMypageSerializer(serializers.ModelSerializer):
    article_set = ArticleSerializer(many=True, read_only=True)
    like_articles = ArticleLikeSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'article_set', 'like_articles')