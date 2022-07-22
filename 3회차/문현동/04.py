import requests
from pprint import pprint


def recommendation(title):
    
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
        recommendations_path = f"/movie/{movie_id}/recommendations"
        response_recommendations = requests.get(url = base_url + recommendations_path + f"?api_key={api_key}&language=ko-KR&page=1").json()
        response_list.append(response_recommendations.get("results"))

    movie_title = []

    for movies in response_list:
        for movie_info in movies:
            movie_title.append(movie_info.get("title"))

    return (movie_title if movie_title != [] else None)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
