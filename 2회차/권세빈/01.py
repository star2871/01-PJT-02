import requests
def popular_count():
    URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '79d21b47771ad41e6e0ed5b1a8b503e7',
        'language': 'ko-KR'
    }
    response = requests.get(URL+path, params=params).json()
    movie = response.get('results')
    cnt = 0
    for i in movie:
        cnt += 1    
    return(cnt)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
