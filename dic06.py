#250325
index = 1
with open('example.txt', 'r', encoding='utf-8') as hellofile:
    content = hellofile.readlines()
    
    for line in content:
        print(f"{index}번째 줄 :{line}", end='')
        index = index + 1

print("================") # 이 방식 추천천
with open('example.txt', 'r', encoding='utf-8') as hellofile:
    content = hellofile.readlines()
    
    for i, line in enumerate(content):
        print(f"{i+1}번째 줄 :{line}", end='')