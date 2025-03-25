#250325 퀴즈
#특정 디렉터리 내의 txt 파일을 검사
#txt 파일 내의 앞쪽에 #이나 // 주석 처리로 되어 있는 것을 검사  ex) startswith()
#탐지된 파일에서 줄 인덱스와 함께 탐지 문자 출력

import os

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
                    print(f"{file_path} (line: {index + 1}) {line.strip()}")
                