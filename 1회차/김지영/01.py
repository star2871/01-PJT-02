# 인기영화 목록의 개수 출력
# TMDB에서 인기있는 영화목록 데이터 요청
# 영화갯수 반환 함수 작성
# https://api.themoviedb.org/3/movie/550?api_key=66c53dabd7bc9afc53c2ca7eba855583
import requests

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '66c53dabd7bc9afc53c2ca7eba855583',
        'language' : 'ko-KR'
    }
    # response = requests.get(BASE_URL+path, params=params).json()    # RequestsJSONDecodeError...
    response = requests.get(BASE_URL+path, params=params).json()
    # print(response,type(response))                               # <Response [200]>
    # print(response.text, type(response.text))     # ?ajldkaf
    # base_url부터 잘못된거였다....
    # print(response.json())
    pop = response.get('results')
    # print(type(pop)) # <class 'list'>
    # print(len(pop)) # 20
    return len(pop)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
