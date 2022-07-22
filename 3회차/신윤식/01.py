import requests
from pprint import pprint


def popular_count():

    Base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key':'c50a19b48082034474f496795a05cb2c',
        'language':'ko-KR'
    }
    response = requests.get(Base_url+path, params = params).json().get('results')
    return len(response)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    pprint(popular_count())
    # 20
