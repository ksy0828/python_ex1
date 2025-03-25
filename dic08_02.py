#250325 #set()함수
#특정 디렉터리를 모니터링 - 파일 정보들을 수집
#새로운 파일이 업로드가 되면, 기존 파일 정보들과 비교!!!
#pre_file - new_file 목록을 차이점!
#비교한 결과 새롭게 추가된 파일을 리스트화!!
#새롭게 추가된 파일을 현재 점검한 날짜 기준으로 txt파일로 저장

import os, time
from datetime import datetime

DIR_PATH = "uploads"

#시간 정보
now = datetime.now() 
day = now.strftime("%Y-%m-%d")
hour = now.strftime("%H:%M:%S")

#기존 파일 목록 가져오기
pre_file = set(os.listdir(DIR_PATH)) #그냥하면 오류..set으로 타입 변환
print(pre_file)

#파일이  새로 들어오는지 모니터링
while True:
    current_file = set(os.listdir(DIR_PATH))
    result_diff = current_file - pre_file
    print(result_diff)
    print("파일 탐지 중..")

    if pre_file != current_file:
        with open('report.txt', 'a', encoding='utf-8') as file:
            file.write(f"\n 새 파일 감지, 시간 : {hour}")

    pre_file = current_file #차이점을 기존파일로 업데이트
    time.sleep(1)



