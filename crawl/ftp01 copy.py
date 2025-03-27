import ftplib
#파일전송 프로토콜

def upload_file(ftp, filename):
    with open(filename, 'rb') as file:
        ftp.storbinary('STOR ' + filename, file)

def main():
    #ftp 접속
    hostname = "192.168.61.128" 
    ftp = ftplib.FTP(hostname)
    ftp.login('msfadmin','msfadmin')

    #파일 읽어서 보낸다.
    # filename = 'snews.xlsx'
    upload_file(ftp, 'snews.xlsx')

    #리스트 확인
    ftp.retrlines('LIST')
    ftp.quit()

if __name__ == "__main__":
    main()