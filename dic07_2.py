#250325 퀴즈
#특정 디렉터리 내의 txt 파일을 검사
#txt 파일 내의 앞쪽에 #이나 // 주석 처리로 되어 있는 것을 검사  ex) startswith()
#탐지된 파일에서 줄 인덱스와 함께 탐지 문자 출력

import os
import re

dir_path = "uploads"
all_files = os.listdir(dir_path)
txt_files = []

for file in all_files:
    if file.endswith(".txt"): #endswith - 뒤에 .txt 붙은 파일 찾기
        txt_files.append(file)

for filename in txt_files:
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
                if line.startswith("#") or line.startswith("//"):
                    print(f"주석 {file_path} (line: {index + 1}) {line}")
                if re.search(r'\d{6}\s*[-]\s*\d{7}', line): # \s*은 공백이 포함되어 있을 경우까지 찾기
                    print(f"주민번호 {file_path} (line: {index + 1}) {line}")
                #if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', line): #이건 이제 잘안씀씀
                if re.search(r'[\w\.-]+@[\w\.-]+', line):
                    print((f"이메일 {file_path} (line: {index + 1}) {line}"))