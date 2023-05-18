import requests
import json


# TMDB API 키
api_key = '42a52760a5d3f83a9c59c93e3265ddd7'

## Movie 모델 데이터 API 요청
# API 응답 결과 -> id를 담아서 keyword요청
movie_res = []

for pageNum in range(1, 501):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page={pageNum}'
    response = requests.get(url)
    data = response.json()

    for item in data['results']:
        try:
            tmdb_id = item['id']
            print(tmdb_id)
        except:
            pass

            
print(len(movie_res))


# with open('movie_model.json', "w", encoding='utf-8') as f:
#     json.dump(movie_res,f, ensure_ascii=False,indent=4)