import requests


def popular_count():
  
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '801b2f9c7a6d8dce6f3bd7f807c9ffc5',
        'language' : 'ko-KR'
    }

    response = requests.get(BASE_URL+path, params=params).json()
    return response.get('results')

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    20
