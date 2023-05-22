from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.http import JsonResponse, FileResponse
import requests
import json
import io
import os
import base64
from PIL import Image
from django.conf import settings
from .models import Movie, MovieKeyword, Keyword
from .serializers import MovieSerializer, MovieDetailSerialzer, RatingSerializer, MovieImgSerializer

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
def t2i(text, batch_size=1):
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

    # 응답의 첫 번째 이미지 생성 결과 출력하기
    result = stringToImage(response.get("images")[0].get("image"), mode='RGB')
    result.show()
    # 저장할 폴더 경로
    output_folder_path = './movies/static'

    # 폴더가 없을 경우 생성
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # 이미지 저장
    output_image_path = os.path.join(output_folder_path, f'{movieId}.png')
    result.save(output_image_path)
  
    return FileResponse(open(output_image_path, 'rb'), content_type='image/png')
