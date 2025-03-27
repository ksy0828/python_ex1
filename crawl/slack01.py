import os
from dotenv import load_dotenv
import requests

load_dotenv()

slack_url = os.getenv('HOOK_url') #여러분의 Slack API 주소

def sendSlackWebHook(strText):
    headers = {
        "Content-type": "application/json"
    }
    
    data = {
        "text": strText
    }
    res = requests.post(slack_url, headers=headers, json=data)

    if res.status_code == 200:
        return "OK"
    else:
        return "Error"

print(sendSlackWebHook("파이썬 자동화 슬랙 메시지 테스트"))