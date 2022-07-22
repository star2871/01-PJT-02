 # import requests library 
import requests  

# API 통신을 위한 URL 저장
url = "https://api.bithumb.com/public/ticker/BTC_KRW"  

# get method 를 통해 requests 객체 response 생성하여 서버에 요청
response = requests.get(url)  

# 요청하여 받은 데이터를 json() method를 통해 json -> dict으로 처리
# dict type의 자료형에 get() method를 적용하여 원하는 값 출력
print(response.json().get('data').get('prev_closing_price')) 