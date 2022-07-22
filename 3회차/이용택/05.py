import requests
from pprint import pprint
from dotenv import load_dotenv
import os


def credits(title):
    load_dotenv()
    key = os.getenv("KEY")
    
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
            'api_key' : key,
            'language' : 'ko-kr',
            'query' : f'{title}'}

    response = requests.get(base_url + path, params = params).json()
    # title이 serachable
    if response['results']:
        movie_id = response['results'][0]['id']
        path = f'/movie/{movie_id}/credits'

        response = requests.get(base_url + path, params = params).json()
        cast_info = response['cast']
        
        casting = []
        for cast in cast_info:
            if cast['cast_id'] < 10:
                casting.append(cast['original_name'])
        
        crew_info = response['crew']
        directing = []
        for crew in crew_info:
            if crew['department'] == 'Directing':
                directing.append(crew['original_name'])

        result = {}  
        result['cast'] = casting
        result['crew'] = directing

    else:
        result = None
    
    return result
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    # pprint(credits('검색할 수 없는 영화'))
    # None
