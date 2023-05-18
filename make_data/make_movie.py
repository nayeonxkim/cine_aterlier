import requests
import csv
from datetime import datetime


def save_to_csv(csv_file, api_name, api_response):

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['tmdb_id', 'original_title', 'title', 'overview', 'release_date', 'poster_path', 'genre_id', 'api_category']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for movie in api_response:
            writer.writerow({
                'tmdb_id' : movie['id'],
                'original_title' : movie['original_title'],
                'title' : movie['title'],
                'overview' : movie['overview'],
                'release_date' : movie['release_date'],










































                
                'poster_path' : movie['poster_path'],
                'genre_id' : movie['genre_ids'][0],
                'api_category' : api_name
            })
        print(f'Saved to {csv_file}')


# TMDB API 키
api_key = '42a52760a5d3f83a9c59c93e3265ddd7'

# Popular API
url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR'
response = requests.get(url)
data = response.json()
popular = data['results']
save_to_csv('popular.csv', 'popular', popular)

# # NowPlaying API
# url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=ko-KR'
# response = requests.get(url)
# data = response.json()
# now_playing = data['results']
# save_to_csv('now_playing.csv', 'now_playing', now_playing)

# # TopRated
# url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=ko-KR'
# response = requests.get(url)
# data = response.json()
# top_rated = data['results']
# save_to_csv('top_rated.csv', 'top_rated', top_rated)


def csv_to_Movie(csv_file, Model):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                movie = Model(
                    tmdb_id=row['tmdb_id'],
                    original_title = row['original_title'],
                    title=row['title'],
                    overview=row['overview'],
                    release_date=datetime.strptime(row['release_date'], '%Y-%m-%d').date(),
                    poster_path=row['poster_path'],
                    genre_id=row['genre_id'],
                    api_category=row['api_category']
                )
                movie.save()

def csv_to_Keyword(csv_file, Model):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                movie = Model(
                    keyword_id=row['keyword_id'],
                    keyword_name=row['keyword_name']

                )
                movie.save()

def csv_to_MovieKeyword(csv_file, Model):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                movie = Model(
                    tmdb_id=row['tmdb_id'],
                    keyword_id=row['keyword_id']
                )
                movie.save()



csv_to_Movie('popular.csv', Movie)
csv_to_Movie('now_playing.csv', Movie)
csv_to_Movie('top_rated.csv', Movie)
# csv_to_Keyword('keyword.csv', Keyword)
# csv 순회하면서 id가 일치하는 keyword 객체 찾기
# def csv_to_MovieKeyword(csv_file, Model):
#     with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             keyword = Model.objects.get(keyword_id=row['keyword_id'])
#             k_ins = Model(
#                 tmdb_id=row['tmdb_id'],
#                 keyword_id=keyword
#             )
#             k_ins.save()

# csv_to_MovieKeyword('movie_keyword.csv', MovieKeyword)

# # 영화 키워드받기

# api_key = '42a52760a5d3f83a9c59c93e3265ddd7'


# movies = Movie.objects.all()
# result_key = []
# result_mid = []
# cnt = 0
# for movie in movies:
#     url = f'https://api.themoviedb.org/3/movie/{movie.tmdb_id}/keywords?api_key={api_key}&language=ko-KR'
#     response = requests.get(url)
#     data = response.json()
#     # print(data)
#     # 키워드 테이블
#     for item in data['keywords']:
#         cnt += 1
#         key_id = item['id']
#         key_name = item['name']
#         keyword_lst = [key_id, key_name]
#         if keyword_lst not in result_key:
#             result_key.append(keyword_lst)

#         keyword_id = item['id']
#         middle_lst = [movie.tmdb_id, keyword_id]
#         result_mid.append(middle_lst)

# print(f'개수: {cnt}')
# print('키워드 테이블 데이터')
# print(len(result_key))
# print('중개 테이블 데이터')
# print(len(result_mid))

# # 키워드 테이블 데이터
# with open('movie_keyword.csv', 'w', newline='', encoding='utf-8') as file:
#     fieldnames = ['keyword_id', 'keyword_name']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()

#     for keyword in result_key:
#         writer.writerow({
#             'keyword_id' : keyword[0],
#             'keyword_name' : keyword[1]
#         })

# # 중개 테이블 데이터
# with open('keyword.csv', 'w', newline='', encoding='utf-8') as file:
#     fieldnames = ['tmdb_id', 'keyword_id']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()

#     for keyword in result_mid:
#         writer.writerow({
#             'tmdb_id' : keyword[0],
#             'keyword_id' : keyword[1]
#         })

