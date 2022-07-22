import requests
# https://api.themoviedb.org/3/movie/550?api_key=94ceed584568fa7a9113545f2e4291f5

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '94ceed584568fa7a9113545f2e4291f5',
        'language' : 'ko-KR'
    }
    response = requests.get(BASE_URL+path, params=params)
    movie_dict = response.json()

    return len(movie_dict['results'])


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
