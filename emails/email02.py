import os, time
import re
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

def mail_sender(name, file_path, line): #정의함수 지정
    load_dotenv()
    send_email = os.getenv("SECRET_ID")
    send_pwd = os.getenv("SECRET_PASS")
    recv_email = "@naver.com"

    smtp_name = "smtp.naver.com" 
    smtp_port = 587              

    text = f"탐지라인: {line}" #내용

    msg = MIMEText(text, 'plain', 'utf-8') 
    msg['Subject'] = f"모니터링- {name}: {file_path} 탐지" # 메일 제목
    msg['From'] = send_email          
    msg['To'] = recv_email            

    email_string = msg.as_string()
    print(email_string)

    s = smtplib.SMTP(smtp_name, smtp_port)
    s.starttls()
    s.login(send_email, send_pwd)
    s.sendmail(send_email, recv_email, email_string)
    s.quit()

DIR_PATH = 'uploads'

#정규 표현식 - 이메일 탐지
email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
jumin_pattern = re.compile(r'\d{6}[-]\d{7}')

pre_file = set(os.listdir(DIR_PATH))

while True:
    now = datetime.now()
    day = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:%M:%S")
    current_file = set(os.listdir(DIR_PATH))
    result_diff = current_file - pre_file

    for file_name in result_diff:
        print(f"새로운 파일 탐지: {file_name}")
        with open(f"{day}월 탐지 보고서.txt", "a", encoding='utf-8') as file:
            file.write(f"작성자: 짱구\n")
            file.write(f"주요 내용 : 신규 파일 탐지\n")
            file.write(f"시간: {hour} 파일 내용 {file_name}\n")
        
        #파일의 내용을 확인하기
        file_path = os.path.join(DIR_PATH, file_name)

        with open(file_path, "r", encoding="UTF-8") as file:
            lines = file.readlines()
            for num, line in enumerate(lines):
                if line.startswith(("#","//")):
                    print(f"주석처리: {num}번째줄 : {line}")
                    mail_sender("주석처리",file_path, line)
                #이메일 탐지
                emails = email_pattern.findall(line)
                for email in emails:
                    print(f"이메일 {num}번째줄: {email}")
                    mail_sender("이메일", file_path, line)
                #주민번호 탐지
                jumins = jumin_pattern.findall(line)
                for jumin in jumins:
                    print(f"주민번호 {num}번째줄: {jumin}")
                    mail_sender("주민번호",file_path, line)

    pre_file = current_file
    
    print("모니터링 중")
    time.sleep(1)
