# 웹 스크래핑 예제

# 라이브러리 가져오기
import requests
from bs4 import BeautifulSoup

# 데이터를 가져올 URL 주소
URL = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=%EC%B1%85+%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%85%80%EB%9F%AC&qdt=0&ie=utf8&query=%EC%B1%85+%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%85%80%EB%9F%AC"

# 데이터의 headers 정의
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# requests라이브러리의 .get()매서드로 URL에서 정보 가져오기
data = requests.get(URL, headers=headers)

# BeautifulSoup 객체 활용하여 가져올 데이터의 텍스트 데이터를 HTML 포맷으로 parsing
soup = BeautifulSoup(data.text, 'html.parser')

# select_one()을 통해 복사한 selector에서 데이터를 가져온다.
title = soup.select_one("#main_pack > section.sc_new.sp_nbook._prs_bok_cat._nshopping_book_pc > div > div._content_root > div:nth-child(2) > ul > li:nth-child(1) > div > div.info_area > a")
# 가져온 데이터를 보기
print(title.text)


