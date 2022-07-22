import requests
from pprint import pprint


def credits(title):
    
    api_key = "f4dd99962cc7bdf87852d77531969501"
    base_url = f"https://api.themoviedb.org/3"
    movie_path = "/search/movie"
    
    payload =\
    {
        "api_key" : api_key,
        "language" : "ko-KR",
        "query" : title
    }
    
    response = requests.get(url = base_url + movie_path, params = payload).json()
        
    movie_id_list = []
    
    for movie_info in response.get("results"):
        movie_id_list.append(movie_info["id"])
        
    response_list = []
    
    for movie_id in movie_id_list:
        credit_path = f"/credit/{movie_id}"
        response_credit = requests.get(url = base_url + credit_path + f"?api_key={api_key}").json()
        print(response_credit)
        '''response_list.append(response_credit.get("results"))

    movie_title = []

    for movies in response_list:
        for movie_info in movies:
            movie_title.append(movie_info.get("title"))

    return (movie_title if movie_title != [] else None)  '''


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
