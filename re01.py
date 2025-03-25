#정규표현식 
import re

#raw string(r)
text = "오늘은 2024년 5월 6일입니다."
pattern = re.compile(r"\d+") #\d+ 숫자가 하나 이상인 것 찾기
matches = pattern.findall(text)
print(matches)  # ['2024', '5', '6']

#일반문자열
pattern = re.compile("\\d+")  # 숫자를 찾는 정규 표현식
text = "There are 123 apples"
matches = pattern.findall(text)
print(matches)  # ['123']