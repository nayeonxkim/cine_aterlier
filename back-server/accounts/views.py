from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from rest_framework.decorators import permission_classes
from .serializers import UserSerializer, UserMypageSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def info(request):
    current_user = request.user
    serializer = UserSerializer(current_user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mypage(request):
    current_user = request.user
    serializer = UserMypageSerializer(current_user)
    return Response(serializer.data)
