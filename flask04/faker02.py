from pymongo import MongoClient
from faker import Faker

# MongoDB에 연결
client = MongoClient('mongodb://localhost:27017/')

# 데이터베이스 선택
db = client['mydatabase_faker']

# 컬렉션 선택
collection = db['people']

# Faker 객체 생성
fake = Faker("ko_KR")

# 가짜 데이터 생성 및 입력
for _ in range(20):
    person = {
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email(),
        'phone': fake.phone_number()
    }
    collection.insert_one(person)

print("가짜 데이터가 성공적으로 입력되었습니다.")