import requests as http
import json
import os

DINGDING = 'https://oapi.dingtalk.com/robot/send'


def send_request(data):
    token = os.getenv('DING_TOKEN')
    url = DINGDING + '?access_token=' + token
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data)
    res = http.post(url=url, headers=headers, data=data)
    return res


def ding_text(msg):
    return send_request({
        'msgtype': 'txt',
        'content': {
            'text': msg
        }
    })


def ding_md(title, text):
    return send_request({
        'msgtype': 'markdown',
        'markdown': {
            'title': title,
            'text':text
        }
    })
