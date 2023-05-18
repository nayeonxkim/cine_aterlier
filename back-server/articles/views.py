from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from rest_framework import status

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer

# 게시글 전체 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):
    article = Article.objects.all()
    serializer = ArticleSerializer(article, many=True)
    return Response(serializer.data)

# 게시글 생성
@api_view(['POST'])
@permission_classes([AllowAny])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
# 게시글 상세 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

# 게시글 수정
@api_view(['PUT'])
@permission_classes([AllowAny])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

# 게시글 삭제
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# 댓글 생성
@api_view(['POST'])
@permission_classes([AllowAny])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data)
    
# 댓글 삭제
@api_view(['DELETE'])
@permission_classes([AllowAny])
def comment_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)