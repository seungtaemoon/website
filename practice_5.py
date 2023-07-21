# pymong 라이브러리의 MongoClient 클래스 가져오기
from pymongo import MongoClient
import pymongo

# 클래스를 인스턴스화(MongoDB Client의 URL 주소 입력)
client = MongoClient("mongodb+srv://conanmoon:cmst9917@cluster0.vsoy9sp.mongodb.net/mydb?retryWrites=true&w=majority")

# 인스턴스의 db를 객체화
db = client["mydb"]

# db객체의 컬렉션을 인스턴스화
collection = db["users"]

doc = {
    "name": "철수",
    "age": 35
}

x = collection.insert_one(doc)