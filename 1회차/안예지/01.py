# e0c0d3622b43ae47c6135b0a8f2cb8f2
import requests


def popular_count():
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'e0c0d3622b43ae47c6135b0a8f2cb8f2',
        'language' : 'ko-KR'        
    }
    
    response = requests.get(BASE_URL+path, params=params).json()
    # /movie/popular에 있는 값 json으로 불러와서 response 에 저장
    # print(response.keys())
    # response의 key 목록 확인
    # print(type(response['results'])) # <class 'list'>
    cnt = 0
    for n in response['results']:
        n.get('id')
        cnt += 1
    # print(cnt)
    return cnt

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
