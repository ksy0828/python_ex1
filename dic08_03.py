#특정 디렉터리를 모니터링 - 파일 정보들을 수집
#새로운 파일이 업로드가 되면, 기존 파일 정보들과 비교!!!
#pre_file - new_file 목록을 차이점!
#비교한 결과 새롭게 추가된 파일을 리스트
#그리고, 개인정보, 주석처리 등 처리하기 기능까지 포함을 해보세요!!

import os, time
import re 
from datetime import datetime

DIR_PATH = "uploads"

#기존 파일 목록 가져오기
pre_file = set(os.listdir(DIR_PATH)) #그냥하면 오류..set으로 타입 변환
print(','.join(pre_file))

#파일이  새로 들어오는지 모니터링
while True:

    #시간 정보
    now = datetime.now() 
    day = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:%M:%S")

    current_file = set(os.listdir(DIR_PATH))
    result_diff = current_file - pre_file
    #print(result_diff)
    
    for file_name in result_diff:
        file_path = os.path.join(DIR_PATH, file_name)
        print(f"새로운 파일 탐지 : {file_name}")
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                
                with open('report.txt', 'a', encoding='utf-8') as file:
                    file.write(f"\n 새 파일 감지 : {file_name}, 시간 : {hour}")
                    
                    if line.startswith("#") or line.startswith("//"):
                        file.write(f"\n 주석 {file_path} (line: {index + 1}) {line}")
                
                    if re.search(r'\d{6}\s*[-]\s*\d{7}', line): # \s*은 공백이 포함되어 있을 경우까지 찾기
                        file.write(f"\n 주민번호 {file_path} (line: {index + 1}) {line}")

                    if re.search(r'[\w\.-]+@[\w\.-]+', line):
                        file.write(f"\n 이메일 {file_path} (line: {index + 1}) {line}")




    print("파일 탐지 중..")
    pre_file = current_file #차이점을 기존파일로 업데이트
    time.sleep(1)