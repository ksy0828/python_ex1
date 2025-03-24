person = {"name": "John", "age": 30, "city": "New York"}

#1. 직접 인덱싱 사용
try:
    print("Name:", person["name"])  # 존재하는 키
    print("Salary:", person["salary"])  # 존재하지 않는 키
except KeyError:
    print("KeyError: 'salary' key does not exist.")

#2. get() 메서드 사용
print("\nUsing get() method:")
print("Name:", person.get("name"))  # 존재하는 키
print("Salary:", person.get("salary"))  # 존재하지 않는 키, None을 반환
print("Salary with default:", person.get("salary", "Not Available"))  # 존재하지 않는 키, 기본값 "Not Available" 반환
