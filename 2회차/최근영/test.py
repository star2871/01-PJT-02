from pprint import pprint
import requests

# def recommendation(title):
    
#     base_url = 'https://api.themoviedb.org/3/movie/popular'
#     params = {
#         'api_key': 'f25f9449dadd6f959e63b7b058966cea',
#         'language': 'ko-KR'
#     }
#     response = requests.get(base_url,params=params).json()
    
#     recommand_url = https://api.themoviedb.org/3/movie/{reco_id}/recommendations
#     reco_response = requests.get(recommand_url,params=params).json()
#     print(reco_response)



# # 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     """
#     제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
#     추천 영화가 없을 경우 []를 반환
#     영화 id 검색에 실패할 경우 None을 반환
#     (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
#     """
#     pprint(recommendation('기생충'))
#     # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
#     pprint(recommendation('그래비티'))
#     # []
#     pprint(recommendation('검색할 수 없는 영화'))
#     # None

title="기생충"
base_url = 'https://api.themoviedb.org/3/search/movie'
params = {
    'api_key': 'f25f9449dadd6f959e63b7b058966cea',
    'language': 'ko-KR',
    'query' : title
}
response = requests.get(base_url,params=params).json()

for i in response['results']:
    if title == i['title']:
        reco_id = i['id']

recommand_url = f'https://api.themoviedb.org/3/movie/{reco_id}/recommendations'
reco_response = requests.get(recommand_url,params=params).json()
reco_list=[]
for j in reco_response['results']:
    reco_list.append(j['title'])
print(reco_list)
        