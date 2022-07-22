import requests
from pprint import pprint


def vote_average_movies():
  pass 
  # 여기에 코드를 작성합니다.  
  BASE_URL = 'https://api.themoviedb.org/3'
  path = '/movie/popular'
  params = {
      'api_key': '66c53dabd7bc9afc53c2ca7eba855583',
      'language' : 'ko-KR'
  }
  response = requests.get(BASE_URL+path, params=params).json()
  v = response.get('results') 
  return v

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(vote_average_movies())