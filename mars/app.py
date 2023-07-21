
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

application = app = Flask(__name__)

# Mongo 클라이언트 객체화
client = MongoClient('mongodb+srv://conanmoon:cmst9917@cluster0.vsoy9sp.mongodb.net/mars?retryWrites=true&w=majority') # 여기에 본인의 계정/비번/데이터베이스/컬렉션 정보가 담긴 URL을 넣는다.

# 데이터베이스 정의
db = client.mars

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/mars", methods=["POST"])
def mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']

    # 데이터 기록
    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }

    # 데이터 저장
    db.orders.insert_one(doc)

    # POST(주문)요청에 대한 응답 출력
    return jsonify({'msg': '주문 완료!'})

@app.route("/mars", methods=["GET"])
def mars_get():
    orders_list = list(db.orders.find({},{'_id':False}))
    return jsonify({'orders':orders_list})

if __name__ == '__main__':
    app.run()
