import ftplib
#파일전송 프로토콜

#ftp 접속속
hostname = "192.168.61.128" 
ftp = ftplib.FTP(hostname)
ftp.login('msfadmin','msfadmin')

# print(ftp.pwd()) #우리가 접속을 한 후에 현재 어느 디렉토리리에 있나 
# ftp.mkd('test')

#파일 읽어서 보낸다.
filename = 'snews.xlsx'
with open(filename, 'rb') as file:
    ftp.storbinary('STOR ' + filename, file) #STOR 뒤에 공백 필수 

#리스트 확인
ftp.retrlines('LIST') #어느 파일들이 있나
ftp.quit()