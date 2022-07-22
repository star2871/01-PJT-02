import requests


def popular_count():

    popular = "popular"
    url = f"https://api.themoviedb.org/3/movie/{popular}"
    params = {
        'api_key': 'personal key value input',
        'language': 'ko-KR'
    }
    res = requests.get(url, params = params).json() #목록반환
    return len(res["results"]) #개수세기


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
