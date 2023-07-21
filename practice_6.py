# pymong 라이브러리의 MongoClient 클래스 가져오기
from pymongo import MongoClient

# 클래스를 인스턴스화(MongoDB Client의 URL 주소 입력)
client = MongoClient("mongodb+srv://conanmoon:cmst9917@cluster0.vsoy9sp.mongodb.net/mydb?retryWrites=true&w=majority")

# 인스턴스의 db를 객체화
db = client.mydb

# db객체의 컬렉션을 인스턴스화
collection = db.users

# 컬렉션에 데이터 넣기
doc_1 = {
    "name": "철수",
    "age": 35
}

doc_2 = {
    "name": "영희",
    "age": 34
}

doc_3 = {
    "name": "하늬",
    "age": 32
}

doc_4 = {
    "name": "두리",
    "age": 40
}

# collection.insert_one(doc_1)
# collection.insert_one(doc_2)
# collection.insert_one(doc_3)
# collection.insert_one(doc_4)

#데이터를 찾는다.

# all_users = list(db.users.find({}, {'_id':False}))
# print(all_users)

# for i in all_users:
#   print(i["name"], i["age"])

# user = db.users.find_one({})
# print(user)

# collection.update_one({'name':'철수'},{'$set':{'age':39}})

db.users.delete_one({'name':'두리'})