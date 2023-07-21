import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Requests 및 BeautifulSoup 활용
URL = "https://movie.daum.net/ranking/reservation"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# pymongo 라이브러리 활용
client = MongoClient("mongodb+srv://conanmoon:cmst9917@cluster0.vsoy9sp.mongodb.net/mydb?retryWrites=true&w=majority")
db = client.mydb
collection = db.users

for i in range(1, 21, 1):
    movie_ranking = soup.select_one(f"#mainContent > div > div.box_ranking > ol > li:nth-child({i}) > div > div.thumb_item > div.poster_movie > span.rank_num")
    movie_title = soup.select_one(f"#mainContent > div > div.box_ranking > ol > li:nth-child({i}) > div > div.thumb_cont > strong > a")
    movie_rate = soup.select_one(f"#mainContent > div > div.box_ranking > ol > li:nth-child({i}) > div > div.thumb_cont > span.txt_append > span:nth-child(1) > span")
    movie_production_date = soup.select_one(f"#mainContent > div > div.box_ranking > ol > li:nth-child({i}) > div > div.thumb_cont > span.txt_info > span")
    print(movie_ranking.text, movie_title.text, movie_rate.text, movie_production_date.text)
    movies = {
        "rank": movie_ranking.text,
        "title": movie_title.text,
        "rate": movie_rate.text,
        "production date": movie_production_date.text
    }
    collection.insert_one(movies)
