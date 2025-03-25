#250325
#파일 탐지  #보고서 작성

import os
from datetime import datetime

now = datetime.now() #많이 사용함 

day = now.strftime("%Y-%m-%d") #포맷을 이 형식으로 바꾼다
hour = now.strftime("%H:%M:%S")

with open(f'{day}_report.txt', 'a', encoding='utf-8') as file:
    file.write(f"\n보고서 작성 완료")
    file.write(f"탐지시간 : {hour}")