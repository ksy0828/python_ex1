#위의 변조된 파일, 중요한 정보가 포함되면 이메일 통지
# + 탐지된 txt 파일을 첨부파일에 같이 보낸다.!!!

import os, time, re
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

#사용자 정의 함수 - 메일 보내기 mail_sender
def mail_sender(name, file_path, line):
    load_dotenv()
    send_email = os.getenv("SECRET_ID")
    send_pwd = os.getenv("SECRET_PASS")
    recv_email = "kim42348@naver.com"

    smtp = smtplib.SMTP('smtp.naver.com', 587)
    smtp.ehlo()
    smtp.starttls()

    smtp.login(send_email,send_pwd)

    text = f"탐지라인: {line}"

    msg = MIMEMultipart()
    msg['Subject'] = f"{name}-모니터 탐지: {file_path}"  
    msg['From'] = send_email          
    msg['To'] = recv_email

    contentPart = MIMEText(text) 
    msg.attach(contentPart)     

    etc_file_path = file_path
    with open(etc_file_path, 'rb') as f : 
        etc_part = MIMEApplication( f.read() )
        etc_part.add_header('Content-Disposition','attachment', filename=etc_file_path)
        msg.attach(etc_part)

    email_string = msg.as_string()
    print(email_string)

    smtp.sendmail(send_email, recv_email, email_string)
    smtp.quit()

DIR_PATH= 'uploads'

#현재 시간 표시
now = datetime.now()
day = now.strftime("%Y-%m-%d")
hour = now.strftime("%H:%M:%S")

#정규 표현식 - 이메일 탐지
email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
jumin_pattern = re.compile(r'\d{6}[-]\d{7}')

pre_file = set(os.listdir(DIR_PATH))

while True:
    cureent_file = set(os.listdir(DIR_PATH))
    result_diff = cureent_file - pre_file
    
    for file_name in result_diff:
        print(f"새로운 파일 탐지 : {file_name}")
        with open(f"{day}월_탐지 보고서.txt", "a", encoding="UTF-8") as file:
            file.write(f"작성자: 조정원\n")
            file.write(f"주요 내용: 신규 파일 탐지\n")
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

    pre_file = cureent_file
    print("확인!!")
    time.sleep(1)