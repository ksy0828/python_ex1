# pip install deep_translator - google trans 
# import deep_translator
from deep_translator import GoogleTranslator # 딥 어쩌구 모듈에서 구글어쩌구 사용하겠다

input_text = input("번역할 한글을 입력하세요.")
translated = GoogleTranslator(source='ko', target='en').translate(input_text)

print(f"입력한 한글 : {input_text}")
print(f"번역된 영어 : {translated}")

input_text2 = input("번역할 영어를를 입력하세요.")
translated2 = GoogleTranslator(source='en', target='ko').translate(input_text2)

print(f"입력한 영어 : {input_text2}")
print(f"번역된 한글글 : {translated2}")