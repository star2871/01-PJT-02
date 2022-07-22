from pprint import pprint
import requests


title="프린세스"
base_url = 'https://api.themoviedb.org/3/movie/popular'
params = {
    'api_key': 'f25f9449dadd6f959e63b7b058966cea',
    'language': 'ko-KR',

}
check_list=[]
response = requests.get(base_url,params=params).json()

for i in response['results']:
    if title == i['title']:
        reco_id = i['id']

recommand_url = f'https://api.themoviedb.org/3/movie/{reco_id}/recommendations'
re_params = {
    'api_key': 'f25f9449dadd6f959e63b7b058966cea',
    'language': 'ko-KR'    
}
reco_response = requests.get(recommand_url,params=params).json()
pprint(reco_response)        
        