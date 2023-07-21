# Flask 라이브러리 가져오기
from flask import Flask, render_template, jsonify, request

# Flask 객체 인스턴스화
app = Flask(__name__)

# Python 파일과 라우팅 ('/'이후의 경로로 연결)
@app.route('/')
def home():
    return render_template('index.html')

# # Python 파일과 라우팅 ('/'이후의 경로로 연결)
@app.route('/test', methods=['GET'])
def test_get():
    receive = request.args.get('give')
    print(receive)
    return jsonify({'result': 'success', 'msg': 'GET 요청'})

# Python 파일과 라우팅 ('/'이후의 경로로 연결)
@app.route('/test', methods=['POST'])
def test_post():
    receive = request.form['give']
    print(receive)
    return jsonify({'result': 'success', 'msg': 'POST 요청'})

# Python 파일과 라우팅 ('/'이후의 경로로 연결)
@app.route("/movie", methods=["GET"])
def movie_get():
    movie_list = list(db.movies.find({},{'_id':False}))
    return jsonify({'movies':movie_list})

# Python 파일을 명기된 IP 주소와 Port로 실행한다.
if __name__ == '__main__':
    app.run('0.0.0.0', port=5003, debug=True)
