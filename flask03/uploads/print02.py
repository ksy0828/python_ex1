name = input("이름을 입력하세요.") #문자열
phone = input("번호를 입력하세요.") #문자열
# age = input("나이를 입력하세요.") #문자열(인풋으로 받는 값은 기본적으로 문자열)
age = int(input("나이를 입력하세요.")) #숫자형


print(type(name))
print(type(phone))
print(type(age))

print(name, "의 전화번호는", phone, "입니다.", "나이는", age, "세 입니다.") #거의 사용 Xp
print("내이음은 {}이고 나이는 {}살입니다." .format(name, age))
print(f"내 이름은 {name}이고 나이는 {age}살입니다.")