import os

dir_path = "uploads"
all_files = os.listdir(dir_path)

txt_files = []

for file in all_files:
    if file.endswith(".txt"): #endswith - 뒤에 .txt 붙은 파일 찾기
        txt_files.append(file)

for filename in txt_files:
    file_path = os.path.join(dir_path, filename)
    #print(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        print(f"{filename} 파일 내용")
        print(file.read())