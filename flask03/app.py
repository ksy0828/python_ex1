from flask import Flask, render_template, request, send_file
import os
from datetime import datetime
import zipfile

app = Flask(__name__)

@app.route('/')
def list():
    UPLOAD_PATH = 'uploads'
    files = []

    for file in os.listdir(UPLOAD_PATH):
        file_path = os.path.join(UPLOAD_PATH, file)
        file_size = os.path.getsize(file_path)
        file_ctime = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        #ㄴfromtimestamp 사람이 있을 수 있게 바꾸기 / strtime 시간 형식 설정 (초단위 빼고)
        files.append((file, file_size, file_ctime, file_path))
        
    print(files) #디버깅

    return render_template('list.html', files=files)

@app.route('/compress', methods=['GET', 'POST'])
def compress():
    UPLOAD_PATH = 'uploads'
    files = request.form.getlist("files")

    #압축기능
    zip_path = os.path.join(UPLOAD_PATH, 'compressd.zip')
    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        for file in files:
            file_path = os.path.join(UPLOAD_PATH, file)
            zip_file.write(file_path, file)
    
    return send_file(zip_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)