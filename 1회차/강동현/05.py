import requests
from pprint import pprint


def credits(title):
    mvsearch = f"search/movie?query={title}"
    url = f"https://api.themoviedb.org/3/movie/{mvsearch}"
    params = {
        'api_key': 'personal key value input',
        'language': 'ko-KR'
    }   
    res = requests.get(url, params = params).json() #목록반환
    
    try:
        resp = res['results']
        movie_id =  resp[0]['id']
    except:
        return None
    dic = {}
    cast_li = []
    crew_li = []
    print(res,movie_id)
    url2 = f'https://api.themoviedb.org/3//movie/{movie_id}/credits'
    res2 = requests.get(url2, params=params).json()
    crew_li2 = res2.get('crew')
    cast_li2 = res2.get('cast')
    for i in crew_li2:
        if i.get('department') == 'Directing':
            crew_li.append(i.get('name'))
    for i in cast_li2:
        if i.get('cast_id') < 10:
            cast_li.append(i.get('name'))
        dic["cast"] = cast_li
        dic["crew"] = crew_li
    return dic


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
