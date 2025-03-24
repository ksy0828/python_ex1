helloFile = open('example.txt', 'w', encoding='utf-8')
helloFile.write('Line 1: Welcome to Python file handling.\n')
helloFile.write('Line 2: This is the second line.\n')
helloFile.write('Line 3: Here is the third line.\n')
helloFile.write('Line 4: The file ends here.\n')
helloFile.close()

helloFile = open('example.txt', 'r', encoding='utf-8')
content = helloFile.read()
print(content)
helloFile.close()
"""
helloFile = open('example.txt', 'r', encoding='utf-8')
print(helloFile.readline())  # 첫 번째 줄 읽기
print(helloFile.readline())  # 두 번째 줄 읽기
helloFile.close()
"""


# 'with' 문을 사용하여 파일을 열고 자동으로 닫기
with open('example.txt', 'r', encoding='utf-8') as helloFile:
    content = helloFile.read()
    print(content)

with open('example.txt', 'r', encoding='utf-8') as helloFile:
    content = helloFile.readlines() 
    for line in content:
        print(line, end='')