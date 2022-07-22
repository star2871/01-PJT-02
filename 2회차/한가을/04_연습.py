# 영화 조회 및 추천 영화 조회
# 영화 제목으로 검색하여 추천 영화 목록 출력

# query는 데이터베이스에게 특정한 데이터를 보여달라는 클라이언트의 요청

from pprint import pprint
import requests

URL = 'https://api.themoviedb.org/3'
path = '/search/movie'
params ={
    'api_key' : 'd84fbf5eb517d499e6c3ce37311d4394',
    'language' : 'ko-KR',
    'query' : 'title'
}
response = requests.get(URL + path, params = params).json()
data = response.get('results')
movie_id = data[0]['id']
# pprint(movie_id)


URL = 'https://api.themoviedb.org/3'
path = f'/movie/{movie_id}/recommendations'
params ={
    'api_key' : 'd84fbf5eb517d499e6c3ce37311d4394',
    'language' : 'ko-KR',
}
response = requests.get(URL + path, params = params)



if __name__ == '__main__':
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None