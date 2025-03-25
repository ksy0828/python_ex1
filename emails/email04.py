#퀴즈
#한글로 된 텍스트 파일 -> 영어로 번역을 합니다. 
#번역된 파일을 날짜를 더해서 저장 -> 이메일로 보내기. 

from deep_translator import GoogleTranslator 
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

    text = f"번역본 \n {line}"

    msg = MIMEMultipart()
    msg['Subject'] = f"{name}-번역: {file_path}"  
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

dir_path = "uploads"
all_files = os.listdir(dir_path)
txt_files = []

for file in all_files:
    if file.endswith(".txt"): #endswith - 뒤에 .txt 붙은 파일 찾기
        txt_files.append(file)

for filename in txt_files:
    file_path = os.path.join(dir_path, filename)

    now = datetime.now() 
    day = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:%M:%S")

    with open(file_path, 'r', encoding='utf-8') as file:
        koreanT = file.read()

        # 2. 번역하기
        translated = GoogleTranslator(source='ko', target='en').translate(koreanT)

        print(f"입력한 한글 : {koreanT}")
        print(f"번역된 영어 : {translated}")

        # # 3. 파일 저장하기
        # with open(f'translated_1.txt', 'w', encoding='utf-8') as file:
        #     file.write(f"원문 : \n {koreanT} \n")
        #     file.write(f"번역 : \n {translated}\n")
        #     file.write(f"작성 시간 : {day} {hour}\n")
        #     mail_sender("번역본",file_path, translated)

        translated_file_path = f'translated_1.txt'
        with open(translated_file_path, 'w', encoding='utf-8') as file:
            file.write(f"원문 : \n {koreanT} \n")
            file.write(f"번역 : \n {translated}\n")
            file.write(f"작성 시간 : {day} {hour}\n")

            # 수정된 부분: translated_file_path로 변경
            mail_sender("번역본", translated_file_path, translated)










# for file in all_files:
#     if file.endswith(".txt"): #endswith - 뒤에 .txt 붙은 파일 찾기
#         txt_files.append(file)

# for filename in txt_files:
#     file_path = os.path.join(dir_path, filename)
#     with open(file_path, 'r', encoding='utf-8') as file:

#         lines = file.readlines()
#         for index, line in enumerate(lines):
#                 if line.startswith("#") or line.startswith("//"):
#                     print(f"{file_path} (line: {index + 1}) {line.strip()}")









