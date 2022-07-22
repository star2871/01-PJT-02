import requests

# https://api.themoviedb.org/3/movie/550?api_key=b730b79937fc4c4e8a1d72531451f76b

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'

    params = {
        'api_key': 'b730b79937fc4c4e8a1d72531451f76b',
        'language': 'ko-KR'
    }

    response = requests.get(BASE_URL + path, params=params).json()

    return len(response['results'])
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
