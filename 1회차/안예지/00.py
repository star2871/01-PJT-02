# API 문서와 requests 활용(연습)
# BTC(비트코인)의 KRW(원) 전일종가 출력

import requests
# URL 생성
order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# 요청을 보내서
response = requests.get(URL)
# 응답 받은 값을 가져온다.
# print(response)

# .json() 메서드는 텍스트 형식의 JSON 파일을 파있너 데이터 타입으로 변경
# print(response.json())

data = response.json()

print(data.get('data').get('prev_closing_price'))
