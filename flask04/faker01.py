# pip install faker
# https://faker.readthedocs.io/en/master/

from faker import Faker

fake = Faker("ko_KR") #한글로 만들기

for _ in range(20): #정해진 출력값 없이 돌릴 때 _ 가능
    print(fake.name())
    print(fake.address())
    print(fake.email())
    print(fake.phone_number())
    print("==========")