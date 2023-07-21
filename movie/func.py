
# 필요한 라이브러리 가져오기
import requests
from bs4 import BeautifulSoup

# 데이터를 가져올 URL 및 header 정의 
url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=191597'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# GET 요청
data = requests.get(url, headers=headers)

# 가져온 데이터의 텍스트만을 출력
soup = BeautifulSoup(data.text, 'html.parser')

# meta 태그 정보 가져오기
og_image = soup.select_one('meta[property="og:image"]') # 이미지 meta 태그
og_title = soup.select_one('meta[property="og:title"]') # 제목 meta 태그
og_description = soup.select_one('meta[property="og:description"]') # 설명 meta 태그

# meta 태그 정보 출력
print(og_image)
print(og_title)
print(og_description)

# meta 태그의 콘텐츠 뜯어보기
image = og_image['content']
title = og_title['content']
description = og_description['content']

# meta 태그 콘텐츠 출력
print(image)
print(title)
print(description)