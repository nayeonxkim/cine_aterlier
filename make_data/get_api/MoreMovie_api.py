import requests
import googletrans
import json
import googletrans
def to_english(title):
    translator = googletrans.Translator()
    translator.raise_Exception = True
    eng_title = translator.translate(title, dest='en', src='auto')
    return eng_title.text

# original_title은 번역기 돌려서 전부 영어로
# def to_english(title):
#     translator = googletrans.Translator()
#     eng_title = translator.translate(title, dest='en', src='auto')
#     return eng_title.text
# to_english('title')

# TMDB API 키
api_key = '42a52760a5d3f83a9c59c93e3265ddd7'

## Movie 모델 데이터 API 요청
# API 결과를 JSON형식으로 담을 리스트
movie_res = []
i = 0
for pageNum in range(1, 501):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page={pageNum}'
    response = requests.get(url)
    data = response.json()

    for item in data['results']:
        try:
            if item['original_language'] != 'en':
                english_title = to_english(item['original_title'])
            else:
                english_title = item['original_title']
                
            if item['release_date']:
                i += 1
                dict = {"model" : "movies.movie",
                        "pk" : item['id'],
                        'fields': {
                            "original_language": item['original_language'],
                            "original_title": english_title,
                            "title": item['title'],
                            "overview": item['overview'],
                            "release_date": item['release_date'],
                            "poster_path": item['poster_path'],
                            "genre_id": item['genre_ids'][0],
                            "adult": item['adult'],
                            "popularity": item['popularity'],
                            "vote_average": item['vote_average'],
                            "vote_count": item['vote_count']
                        }}
                movie_res.append(dict)
                print(i)
        except:
            pass

            
print(len(movie_res))


with open('movie_10000.json', "w", encoding='utf-8') as f:
    json.dump(movie_res,f, ensure_ascii=False,indent=4)