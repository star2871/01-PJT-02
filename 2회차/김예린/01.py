import requests

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular' # 상세경로
    params = {
        'api_key': '3b6818af52c899a45712c6e71f6ecc94',
        'language': 'ko-KR'
    }
    response = requests.get(BASE_URL+path, params=params).json()
    return len(response.get('results'))


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
