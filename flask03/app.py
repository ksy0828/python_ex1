from flask import Flask, render_template, request, send_file
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def list():
    UPLOAD_PATH = 'uploads'
    files = []

    for file in os.listdir(UPLOAD_PATH):
        file_path = os.path.join(UPLOAD_PATH, file)
        file_size = os.path.getsize(file_path)
        file_ctime = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        #fromtimestamp 사람이 있을 수 있게 바꾸기 / strtime 시간 형식 설정 (초단위 빼고)
        
        print(file_path, file_size, file_ctime)

    return render_template('list.html')

    
if __name__ == '__main__':
    app.run(debug=True)