from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, required=False)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id','article', 'token',)

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id','author', 'like_user',)

class ArticleLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','like_user', 'author', 'title','img')