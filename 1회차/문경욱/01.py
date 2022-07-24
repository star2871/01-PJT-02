import requests

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    # api_key = 'e5d3a52ec6678bdeec4350297f8456fb'
    # movie/76341?api_key={api_key}
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : 'e5d3a52ec6678bdeec4350297f8456fb',
        'language' : 'ko-KR'
    }
    response = requests.get(BASE_URL+path, params=params).json()
    # print(response, type(response))

    movie_list = response.get('results')

    popular_count = 0
    for movie in movie_list:
        popular_count += 1
        
    return popular_count


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
