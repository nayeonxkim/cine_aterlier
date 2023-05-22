from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, required=False)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'token',)

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('author', 'like_user',)