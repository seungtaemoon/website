# Python 예제

import requests  # 필요한 라이브러리는 반드시 설치한 후에 활용할 수 있다.

# requests 라이브러리로 HTTP GET 요청하여 원하는 데이터를 가져온다.
r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')

# 데이터를 JSON로 parsing한다.
rjson = r.json()

# 원하는 데이터의 키에 접근한다.
rows = rjson["RealtimeCityAir"]["row"]

# 반복문을 활용해 원하는 정보를 출력한다.
for i in rows:
    area = i["MSRSTE_NM"] # 지역정보 가져오기
    value = i["IDEX_MVL"] # 미세먼지값 가져오기
    # 처리된 데이터를 출력한다.
    print(area, value)
