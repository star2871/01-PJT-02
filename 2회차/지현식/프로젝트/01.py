import requests

def popular_count():
    URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'

    params={
        'api_key':'3d086799f6ddf19a461e5ed8f4712adf'
    }
    response = requests.get(URL+path, params=params).json()
    data = response.get('results')
    popular_len=[]
    for i in data:
        popular_len.append(i.get('popularity'))
    return len(popular_len)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
