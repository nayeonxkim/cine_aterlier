import requests
import googletrans
import json

# original_title은 번역기 돌려서 전부 영어로
def to_english(title):
    translator = googletrans.Translator()
    eng_title = translator.translate(title, dest='en', src='auto')
    return eng_title.text


# TMDB API 키
api_key = '42a52760a5d3f83a9c59c93e3265ddd7'

## Movie 모델 데이터 API 요청
# API 결과를 JSON형식으로 담을 리스트
movie_res = []

for pageNum in range(1, 501):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page={pageNum}'
    response = requests.get(url)
    data = response.json()

    for item in data['results']:
        try:
            dict = {"model" : "movies.movie",
                    "pk" : item['id'],
                    'fields': {
                        "original_title": to_english(item['original_title']),
                        "title": item['title'],
                        "overview": item['overview'],
                        "release_date": item['release_date'],
                        "poster_path": item['poster_path'],
                        "genre_id": item['genre_ids'][0],
                        "adult": item['adult'],
                        "popularity": item['popularity']
                    }}
            movie_res.append(dict)
        except:
            pass
        
print(len(movie_res))


with open('movie_model.json', "w", encoding='utf-8') as f:
    json.dump(movie_res,f, ensure_ascii=False,indent=4)