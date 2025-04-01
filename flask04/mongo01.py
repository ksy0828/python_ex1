from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017') #몽고db 로컬로 연결
db = client['mydatabase'] #데이터베이스 만들기

collection = db['mycollection'] #몽고db의 table 

#"key":"values" 형식으로 삽입
# post = {"title":"세번째 포스트", "content":"안녕하세요.333", "author":"young"}
# collection.insert_one(post) #하나씩 집어넣기 many는 한번에 많이 
# print("OK")

#데이터 검색
result = collection.find_one({"author":"John"})
print(f"검색된 문서  {result}")

#데이터 수정
query = {"author":"John"}
new_values = {"$set": {"content":"수정된 내용입니다."}}
collection.update_one(query, new_values)
print("문서가 수정되었습니다.")

#수정된 데이터 확인
result = collection.find_one(query)
print("수정된 문서 : ", result)

