import requests
import csv


def fetch_movies():
    # TMDB API 요청을 보낼 때 필요한 API 키
    api_key = '42a52760a5d3f83a9c59c93e3265ddd7'

    # TMDB API의 인기 영화 목록 엔드포인트
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'

    try:
        # API 요청 보내기
        response = requests.get(url)
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        # API 요청 실패 시 예외 처리
        print('Error occurred during API request:', str(e))
        return []

def save_as_csv(data):
    # 가져온 데이터를 가공하여 Movie 객체 리스트 생성
        csv_file = 'movies.csv'
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['tmdb_id', 'title', 'overview', 'release_date', 'poster_path', 'genre_id'])

            for result in data['results']:
                tmdb_id = result['id']
                title = result['title']
                overview = result['overview']
                release_date = result['release_date']
                poster_path = result['poster_path']
                genre_id = result['genre_ids'][0]

            print(f'Saved movies to {csv_file}')


movies = fetch_movies()
save_as_csv(movies)

