import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()
send_email = os.getenv("SECRET_ID")
send_pwd = os.getenv("SECRET_PASS")
recv_email = "@naver.com"

smtp_name = "smtp.naver.com" 
smtp_port = 587              

text = "이메일 보내기 테스트입니다" # 메일 내용 - 감지 내용

msg = MIMEText(text, 'plain', 'utf-8') 
msg['Subject'] = "메일 제목 입력"  # 메일 제목 - 0월0일 감지
msg['From'] = send_email          
msg['To'] = recv_email            

email_string = msg.as_string()
print(email_string)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, email_string)
s.quit()