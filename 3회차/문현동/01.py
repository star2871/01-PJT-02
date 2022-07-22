import requests

######################################################################################

def popular_count():
    
    api_key = "f4dd99962cc7bdf87852d77531969501"
    base_url = f"https://api.themoviedb.org/3"
    population_path = "/movie/popular"
    
    payload = {"api_key" : api_key,
            "language" : "ko-KR",
            "page" : 1}
    
    
    
    response = requests.get(url = base_url + population_path, params = payload).json()
        
    movie_title_list = []
    
    for movie_info in response.get("results"):
        movie_title_list.append(movie_info.get("title"))
    return len(movie_title_list)



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
