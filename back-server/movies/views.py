from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.http import JsonResponse
import requests
import json
import io
import os
import base64
from PIL import Image
from django.conf import settings
from .models import Movie, KarloImg
from .serializers import MovieSerializer, MovieDetailSerialzer, RatingSerializer, MovieImgSerializer, KarloSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerialzer(movie)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def rating(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = RatingSerializer(movie, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([AllowAny])
def img(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieImgSerializer(movie)
    return Response(serializer.data)


# 1. 프론트에서 받아온 movieId로 모델에서 영화 인스턴스 찾기
# 2. 그 인스턴스 정보를 직렬화하기 -> 키워드명, 영어제목 정보 담은 serializer
# 3. 그 데이터의 value만 뽑아서 text로 만들기 + painter (쉼표로 구분)
# 4. text넣어서 함수 실행
# 5. 이미지가 외부 폴더에 저장됨
# 6. context에 영화 제목, 화가, 이미지 경로를 넣어서 반환

# [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
REST_API_KEY = '9a5517b855fcd53e94751f63e3795c75'

# 이미지 생성하기 요청
def t2i(text, batch_size=2):
    r = requests.post(
        'https://api.kakaobrain.com/v1/inference/karlo/t2i',
        json = {
            'prompt': {
                'text': text,
                'batch_size': batch_size
            }
        },
        headers = {
            'Authorization': f'KakaoAK {REST_API_KEY}',
            'Content-Type': 'application/json'
        }
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    return response

# Base64 디코딩 및 변환
def stringToImage(base64_string, mode='RGBA'):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata)).convert(mode)
    return img

@api_view(['GET'])
@permission_classes([AllowAny])
def getKarloImg(request, movieId, painter):
    movie = Movie.objects.get(pk=movieId)
    title = movie.original_title
    keywords = movie.keywords.all()
    keyword_names = [keyword.keyword_name for keyword in keywords]

    # 입력단어 prompt 만들기
    prompt = title +', '
    if painter != 'null':
        prompt += painter + ', '
    for keyword in keyword_names:
        prompt += keyword + ', '
    
    
    response = t2i(prompt, 1)
    # return JsonResponse(response)
    for image_data in response["images"]:
        image_id = image_data["id"]
        image_url = image_data["image"]
        nsfw = image_data["nsfw"]
        nsfw_score = image_data["nsfw_score"]
        
        # KarloImg 인스턴스 생성 및 저장
        karlo_img = KarloImg.objects.create(
            movie_id=movieId,
            original_title=title,
            painter=painter,
            img_url=f'/media/{movieId}_{image_id}.png'
        )
        
        # 이미지 저장
        image_path = os.path.join(settings.MEDIA_ROOT, f'{movieId}_{image_id}.png')
        result = stringToImage(image_url, mode='RGB')
        result.save(image_path, 'PNG')
        
        karlo_img.save()

    result_images = KarloImg.objects.filter(movie_id=movieId, painter=painter)
    serializer = KarloSerializer(result_images, many=True)
    # print(prompt)
    return Response(serializer.data)
