# pymong 라이브러리의 MongoClient 클래스 가져오기
from pymongo import MongoClient

# 클래스를 인스턴스화(MongoDB Client의 URL 주소 입력)
client = MongoClient("mongodb+srv://conanmoon:cmst9917@cluster0.vsoy9sp.mongodb.net/mydb?retryWrites=true&w=majority")

# 인스턴스의 db를 객체화
db = client.mydb

# db객체의 컬렉션을 인스턴스화
collection = db.users

example_data = collection.find_one({"title": "좋.댓.구"})

# target = collection.find({}, {'title':1, 'rate':1})

compare_data = collection.find({'rate': example_data["rate"]})

for i in compare_data:
    print(i["title"])

# for i in target:
#     if(i['rate'] == example_data["rate"]):
#         print(i["title"])

collection.update_one({"title": "밀수"}, {"$set": {"rate": 0}})