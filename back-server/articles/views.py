from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

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
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def detail(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     serializer = ArticleSerializer(article)
#     return Response(serializer.data)

# @api_view([''])