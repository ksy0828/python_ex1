import os

names = ['짱구', '철수', '맹구']
#print(names)
#print(type(names))
"""
print(names[0])
print(names[1])
print(names[2])
"""
for name in names:
    print(name)

"""
#파일 정보 리스트
files = os.listdir('.')
for file in files:
    print(file)
"""

print(len(names))  #길이

#range(3) => 0, 1, 2
for i in range(3):
    print(i)

"""
for i in range(len(names)):
    print(names[i])
"""

#인덱스 값 같이 
for i in range(len(names)):
    print(f"{i+1}번째: {names[i]}")

# 많이 사용 (ex. txt파일에서 몇번째 줄에 개인정보를 찾을 때 주로 사용) 
for i, name in enumerate(names): 
    print(f"{i+1}번째: {name}")

# ''이 있다면 어디에 있는지 찾을 때 
if '짱구' in names:
    print("짱구 있음")
    print(f"짱구는 {names.index('짱구')+1}번째에 있음")