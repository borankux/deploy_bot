import requests as http
import json
import os

DINGDING = 'https://oapi.dingtalk.com/robot/send'


def ding_text(msg):
    token = os.getenv('DING_TOKEN')
    url = DINGDING + '?access_token=' + token
    headers = {}
    headers['Content-Type'] = 'application/json'

    data = json.dumps({
        "msgtype": "text",
        "text": {
            "content": msg
        }
    })
    res = http.post(url=url, headers=headers, data=data)
    print(res.content)
    return res
