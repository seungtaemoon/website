# 라이브러리 가져오기
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

# Flask 객체 인스턴스화
app = Flask(__name__)

# MongoClient 클래스 인스턴스화
# 여기에 본인의 계정/비번/데이터베이스/컬렉션 정보가 담긴 URL을 넣는다.
client = MongoClient(
    'mongodb+srv://conanmoon:cmst9917@cluster0.vsoy9sp.mongodb.net/fan?retryWrites=true&w=majority')
db = client.fan  # 데이터베이스 인스턴스화

# Index.html 기본 페이지 그리기
@app.route('/')
def home():
    return render_template('index.html')

# POST API
@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]
    doc = {
    'name': name_receive,
    'comment': comment_receive
    }
    db.guestbook.insert_one(doc)
    return jsonify({'msg': '응원 완료!'})

# GET API
@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    comment_list = list(db.guestbook.find({},{'_id':False}))
    return jsonify({'comments':comment_list})


# 명기된 주소와 포트 번호로 서버 프로그램 실행
if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
