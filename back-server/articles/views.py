from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http  import JsonResponse
from rest_framework.decorators import permission_classes

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from rest_framework import status

from .models import Article, Comment
from django.contrib.auth import get_user_model



from .serializers import ArticleSerializer, CommentSerializer
User = get_user_model()

# 게시글 전체 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    print(request.user)
    articles = Article.objects.all()
    article_count = articles.count()
    serializer = ArticleSerializer(articles, many=True)
    return Response({
        'articles': serializer.data,
        'article_count': article_count,
    })

# 게시글 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(author=request.user)
        return Response(serializer.data)
    
# 게시글 상세 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

# 게시글 수정
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, article_pk):
    user = User.objects.get(id=request.user.id)
    article = get_object_or_404(Article, pk=article_pk)

    if article.author != user:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(img=article.img)
        return Response(serializer.data)
    

# 게시글 삭제
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, article_pk):
    user = User.objects.get(id=request.user.id)
    article = get_object_or_404(Article, pk=article_pk)

    article = get_object_or_404(Article, pk=article_pk)
    if article.author != user:
        return Response(status=status.HTTP_403_FORBIDDEN)
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# 댓글 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        token = Token.objects.get(user=request.user)
        serializer.save(article=article, author=request.user, token=token.key)
        return Response(serializer.data)
    
# 댓글 삭제
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, article_pk, comment_pk):
    user = User.objects.get(id=request.user.id)
    comment = get_object_or_404(Comment,article_id=article_pk, pk=comment_pk)
    # if comment.author != user:
    #     return Response(status=status.HTTP_403_FORBIDDEN)
    # if comment.token != request.auth.key:
    #     return Response(status=status.HTTP_403_FORBIDDEN)
    
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.like_user.filter(id=request.user.id).exists():
        article.like_user.remove(request.user)
        message = 'cancel'
    else:
        article.like_user.add(request.user)
        message = 'like'

    context = {
        'message': message
        }
    return Response(context, status=status.HTTP_200_OK)