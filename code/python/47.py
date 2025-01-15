# requests

import requests
import json

url = "https://api.sampleapis.com/avatar/info"
res = requests.get(url)  # get 가지고 오는겨

# print(res.json())

print(res.status_code)
if res.status_code == 200:
    data = res.json() # json() 값으로 가져오기
    print(data[0]["synopsis"])
    #print(data[0].synopsis)
    print(res.text)  # 응답의 본문 내용 전부 가져오기
    print(res.url)   # 요청했던 주소를 다시 가지고 오는거임


