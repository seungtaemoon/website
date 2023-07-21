# 필요한 라이브러리 가져오기
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

# MongoClient 클래스 인스턴스화
client = MongoClient('mongodb+srv://conanmoon:cmst9917@cluster0.vsoy9sp.mongodb.net/buckets?retryWrites=true&w=majority') # 여기에 본인의 계정/비번/데이터베이스/컬렉션 정보가 담긴 URL을 넣는다.
db = client.buckets # 데이터베이스 인스턴스화

# Flask 객체 인스턴스화
application = app = Flask(__name__)

# 기본 페이지 index.html 출력
@app.route('/')
def home():
    return render_template('index.html')

# POST 요청 API
@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    print(bucket_receive)
    doc = {
        'bucket': bucket_receive
    }
    db.bucket.insert_one(doc)
    return jsonify({'msg': '🥰 버킷리스트가 저장되었습니다!'})

# GET 요청 API
@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_list = list(db.bucket.find({}, {'_id': False}))
    return jsonify({'bucket_list': bucket_list})

# 아래 주소와 포트 번호로 서버프로그램 실행
if __name__ == '__main__':
    app.debug = True
    app.run()