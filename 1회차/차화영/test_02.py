import requests
from pprint import pprint

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': '80c8b18bf43a69499e913dc21300b23c',
    'language': 'ko-KR'
}
response = requests.get(BASE_URL+path, params=params).json()
# keys가 page와 results로 이루어진 딕셔너리
results = response.get('results')
# 딕셔너리에서 results의 값만, results의 type은 <class 'list'> 
data = []
for i in results:
    if 'vote_average' >= 8:
        data = data.append(i)
        print(data)