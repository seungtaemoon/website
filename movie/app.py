# 필요한 라이브러리 가져오기
from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Flask 객체 인스턴스화
app = Flask(__name__)

# Mongo 클라이언트 객체화
client = MongoClient('mongodb+srv://conanmoon:cmst9917@cluster0.vsoy9sp.mongodb.net/movie?retryWrites=true&w=majority') # 여기에 본인의 계정/비번/데이터베이스/컬렉션 정보가 담긴 URL을 넣는다.

# 데이터베이스 정의
db = client.movie

# 메인 페이지 그리기
@app.route('/')
def home():
    return render_template('index.html')

# POST 요청
@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    star_receive = request.form["star_give"]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')
    image = og_image['content']
    title = og_title['content']
    description = og_description['content']
    doc = {
        'image': image,
        'title': title,
        'desc': description,
        'comment': comment_receive,
        'star': star_receive
        }
    db.movies.insert_one(doc)
    return jsonify({'msg': '포스팅 완료!'})

# GET 요청
@app.route("/movie", methods=["GET"])
def movie_get():
    movie_list = list(db.movies.find({},{'_id':False}))
    return jsonify({'movies':movie_list})

# 정의된 IP 주소 및 Port 번호로 서버 프로그램 실행
if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)
