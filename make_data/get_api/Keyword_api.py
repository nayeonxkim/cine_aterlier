import requests
import json


# TMDB API 키
api_key = '42a52760a5d3f83a9c59c93e3265ddd7'

## Movie 모델 데이터 API 요청
# API 응답 결과 -> id를 담아서 keyword요청
keyword_res = []

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
                dict = {
                        "model": "movies.keyword",
                        "pk": keyword['id'],
                        "fields": {
                            "keyword_name": keyword['name']
                        }
                    }
                    
                keyword_res.append(dict)
        except:
            pass
        print('error')

            
print(len(keyword_res))


with open('keyword_model.json', "w") as f:
    json.dump(keyword_res,f,indent=4)