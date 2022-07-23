import requests
from pprint import pprint


def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3' 
    path = '/search/movie'
    params = {
        'api_key' : '801b2f9c7a6d8dce6f3bd7f807c9ffc5',
        'language' : 'ko-KR',
        'query' : title
    }
    response = requests.get(BASE_URL+path, params=params).json()

    if response['results']:
        movie_id = response['results'][0]['id']
        path2 = f'/movie/{movie_id}/credits' 
        params2 = {
            'api_key' : '801b2f9c7a6d8dce6f3bd7f807c9ffc5', 
            'language' : 'ko-KR',
            'query' : 'cast' 
        }
        response2 = requests.get(BASE_URL+path2, params=params2).json()
        
        result_dict ={'cast':[], 'crew':[]}

        for i in response2['cast']: # i
            if i['cast_id'] < 10:
                result_dict['cast'].append(i['name'])
        
        for j in response2['crew']:
            if j['department'] == 'Directing' :
                result_dict['crew'].append(j['name'])

        return result_dict
    
    else:
        return None

    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
