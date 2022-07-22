import requests
from pprint import pprint
from dotenv import load_dotenv
import os


def popular_count():
    load_dotenv()
    key = os.getenv("KEY")
    # 기본 url
    base_url = 'https://api.themoviedb.org/3'
    
    # 기본 url에 이어 붙일 details
    path = '/movie/popular'
    
    # url에 함께 보낼 변수 
    params = {
        'api_key' : key,
        'language' : 'ko'
    }
    
    # requests 객체 생성, 정보 요청 
    res = requests.get(base_url + path, params=params)

    # 받은 데이터 -> dict, 변수 저장
    data = res.json()

    # 원하는 정보에 해당하는 값 따로 변수에 저장
    target_data = data['results']  
  
    # 갯수 변수에 저장
    result = len(target_data)

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
