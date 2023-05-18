import requests

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
            if item['original_title'].is_english():
                dict = {"model" : "movies.movie",
                        "pk" : item['id'],
                        'fields': {
                            "original_title": item['original_title'],
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
