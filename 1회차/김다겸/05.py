import requests
from pprint import pprint

def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    search = '/search/movie'
    params = {
        'api_key' : '94ceed584568fa7a9113545f2e4291f5',
        'language' : 'ko-KR',
        'query' : title
    }
    response = requests.get(BASE_URL+search, params=params)
    movies = response.json().get('results')
    
    id = movies[0]['id']

    credit1 = '/movie/'
    movie_id = str(id)
    credit2 = '/credits'
    params = {
            'api_key' : '94ceed584568fa7a9113545f2e4291f5',
            'language' : 'ko-KR'
        }

    response = requests.get(BASE_URL+credit1+movie_id+credit2, params=params).json()
    ans = {'cast':[], 'crew':[]}
    
    for cast in response['cast']:
        if cast['cast_id'] < 10:
            ans['cast'].append(cast['name'])
    
    for crew in response['crew']:
        if crew['department'] == 'Directing':
            ans['crew'].append(crew['name'])

    return ans


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
