# 필요한 라이브러리 가져오기
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

# 데이터를 가져올 URL 주소
URL = "https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20230101"

# 데이터의 headers 정의
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# requests라이브러리의 .get()매서드로 URL에서 정보 가져오기
data = requests.get(URL, headers=headers)

# BeautifulSoup 객체 활용하여 가져올 데이터의 텍스트 데이터를 HTML 포맷으로 parsing
soup = BeautifulSoup(data.text, 'html.parser')

# 클래스를 인스턴스화(MongoDB Client의 URL 주소 입력)
client = MongoClient("mongodb+srv://conanmoon:cmst9917@cluster0.vsoy9sp.mongodb.net/mydb?retryWrites=true&w=majority")

# 인스턴스의 db를 객체화
db = client.mydb

# db객체의 컬렉션을 인스턴스화
collection = db.music

lists = soup.select("#body-content > div.newest-list > div > table > tbody > tr")

for i in lists:
    song_rank = i.select_one("td.number").text[0:2].strip()
    song_title = i.select_one("td.info > a.title.ellipsis").text.strip()
    song_artist = i.select_one("td.info > a.artist.ellipsis").text.strip()
    print(song_rank, song_title, song_artist)
    song_info = {
        'rank': song_rank,
        'title': song_title,
        'artist': song_artist,
    }
    collection.insert_one(song_info)
