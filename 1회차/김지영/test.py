import requests
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': '66c53dabd7bc9afc53c2ca7eba855583',
    'language' : 'ko-KR'
}
response = requests.get(BASE_URL+path, params=params).json()
    