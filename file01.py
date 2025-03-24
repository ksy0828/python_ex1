import os

"""
file_path = "dic03.py"
if os.path.isfile(file_path):
    print("파일이다.")
else:
    print("파일 아니다.")
"""

entries = os.listdir('.')
print("Entries in current directory:", entries)

for dirpath, dirnames, filenames in os.walk(r"C:\Users\wd\Desktop\Rookies\python_ex1"):
    print(f"Found directory: {dirpath}")
    print(f"Subdir: {dirnames}")
    print(f"File: {filenames}")
    print("-"*50)