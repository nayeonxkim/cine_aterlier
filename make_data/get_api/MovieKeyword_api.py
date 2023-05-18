import requests
import json


# TMDB API 키
api_key = '42a52760a5d3f83a9c59c93e3265ddd7'

## Movie 모델 데이터 API 요청
# API 응답 결과 -> id를 담아서 keyword요청
movieKeyword_res = []
i = 0
for pageNum in range(1, 251):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page={pageNum}'
    response = requests.get(url)
    data = response.json()
    
    for item in data['results']:
        try:
            tmdb_id = item['id']
            url = f'https://api.themoviedb.org/3/movie/{tmdb_id}/keywords?api_key={api_key}&language=ko-KR'
            response = requests.get(url)
            data = response.json()
            for keyword in data['keywords']:
                i += 1
                dict = {
                        "model": "movies.moviekeyword",
                        "pk": i,
                        "fields": {
                            "tmdb_id": tmdb_id,
                            "keyword_id": keyword['id']
                        }
                    }
                    
                movieKeyword_res.append(dict)
                print(i)
        except:
            pass

            
print(len(movieKeyword_res))


with open('movieKeyword_model.json', "w") as f:
    json.dump(movieKeyword_res,f,indent=4)