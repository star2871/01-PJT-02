import requests
from pprint import pprint
title = '기생충'
api_key = '7f612bfdbaa738cd44a88077eead2d22'
URL = 'https://api.themoviedb.org/3'
path_1 = '/search/movie'
param_1 = {
    'api_key' : api_key,
    'language' : 'ko_KR',
    'query' : title
}
response_search = requests.get(URL + path_1, params = param_1)
movie_id = response_search.json()['results'][0].get('id')

path_2 = f'/movie/{movie_id}/credits'
param_2 = {
    'api_key' : api_key,
    'language' : 'ko_KR'
}
lst_crew = []
lst_cast = []
response_search = requests.get(URL + path_2, params=param_2).json()
crew = response_search.get('crew') # list
cast = response_search.get('cast') # list

for i in cast:
    if int(i['cast_id']) < 10 :
        lst_cast.append(i['name'])
for j in crew: # i = {} dict
    if j['department'] == 'Directing' :
        lst_crew.append(i['name'])


result = {
    'cast' : lst_cast,
    'crew' : lst_crew
}
pprint(result)

