from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.serializers import ArticleSerializer
User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    article_set = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields ='__all__'