import requests

def popular_count():
    base = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '1fbf55bcf78cb7b7e9b4e5832c889a5c',
    'language': 'ko-KR'
    }

    response = requests.get(base+path, params=params).json()
    return len(response.get('results'))

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
