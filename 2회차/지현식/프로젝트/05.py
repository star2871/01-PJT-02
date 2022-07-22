import requests
from pprint import pprint
def search(title):
    URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '3d086799f6ddf19a461e5ed8f4712adf',
        'language': 'ko-KR',
        'query': f'{title}'
    }
    response = requests.get(URL + path, params = params)
    if response == None:
        return None
    else:
        data = response.json()
        results = data.get('results')
        for i in range(len(results)):
            movie_id = results[i].get("id")
            return movie_id

def credits(title):
    movie_id = search(title)
    URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'
    params = {
        'api_key': '3d086799f6ddf19a461e5ed8f4712adf',
        'language': 'ko-KR',
        'query': f'{title}'
    }
    cast1 = []
    crew1 = []
    response = requests.get(URL + path, params=params).json()
    res1=response.get("cast")
    res2=response.get("crew")
    for i in range(len(res1)):
        if res1[i].get("cast_id")<10:
            cast1.append(res1[i].get("name"))
    for i in range(len(res2)):
        if res2[i].get("department") == 'Directing':
            crew1.append(res2[i].get("name"))
    dict2 = {"cast": cast1,"crew":crew1}
    return dict2
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    # pprint(credits('검색할 수 없는 영화'))
    # None
