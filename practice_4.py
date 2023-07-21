# 웹 스크래핑 예제

# 라이브러리 가져오기
import requests
from bs4 import BeautifulSoup

# 데이터를 가져올 URL 주소
URL = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=%EC%B1%85+%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%85%80%EB%9F%AC&qdt=0&ie=utf8&query=%EC%B1%85+%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%85%80%EB%9F%AC"

# 데이터의 headers 정의
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# requests라이브러리의 .get()매서드로 URL에서 정보 가져오기
data = requests.get(URL, headers=headers)

# BeautifulSoup 객체 활용하여 가져올 데이터의 텍스트 데이터를 HTML 포맷으로 parsing
soup = BeautifulSoup(data.text, 'html.parser')

# for i in range(1, 101):
#     book_rank = soup.select_one(f"#book_list > ul > li:nth-child({i}) > div > a.bookListItem_info_top__VgpiO.linkAnchor > div.bookListItem_text_area__hF892 > div.bookListItem_title__X7f9_ > span > span.bookListItem_rank__x1oKQ > span")
#     book_title = soup.select_one(f"#book_list > ul > li:nth-child({i}) > div > a.bookListItem_info_top__VgpiO.linkAnchor > div.bookListItem_text_area__hF892 > div.bookListItem_title__X7f9_ > span > span:nth-child(2)")
#     book_author = soup.select_one(f"#book_list > ul > li:nth-child({i}) > div > a.bookListItem_info_top__VgpiO.linkAnchor > div.bookListItem_text_area__hF892 > div.bookListItem_detail__RBQ6x > div:nth-child(1) > span.bookListItem_define_data__kKD8t")
#     book_date = soup.select_one(f"#book_list > ul > li:nth-child({i}) > div > a.bookListItem_info_top__VgpiO.linkAnchor > div.bookListItem_text_area__hF892 > div.bookListItem_detail__RBQ6x > div.bookListItem_define_item__LdTib.bookListItem_publish____VOP > div.bookListItem_detail_date___byvG")

book_rank = soup.select_one("#Myform > div:nth-child(3) > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td > div")
print(book_rank)