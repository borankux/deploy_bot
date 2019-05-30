#!/anaconda3/bin/python


import time
start = time.time()

import yaml
import json
import os
import requests as http
import math
from subprocess import run

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

DINGDING = 'https://oapi.dingtalk.com/robot/send'


with open('./site.yml') as f:
    x = yaml.safe_load(f)


def pull_code(repo, path, branch='master'):

    print('Pulling repository...')
    gc = os.system('git clone ' + repo + ' ' + path)
    if gc !=0:
        return gc
    print('Done !')

    print('Installing packages...')
    mf = os.system('cd' + ' ' + path + ' && make install')
    if mf !=0:
        return mf
    print('Done !')
    return True


def ding(msg):
    token = os.getenv('DING_TOKEN')
    url = DINGDING + '?access_token=' + token
    headers = {}
    headers['Content-Type'] = 'application/json'

    data = json.dumps({
        "msgtype": "text",
        "text": {
            "content":msg
        }
    })
    res = http.post(url=url, headers=headers, data=data)
    print(res.content)
    return res


def set_nginx(path, domain):
    pass


name = x['name']
base = x['base']
domain = x['domain']
sites = x['sites']

ding('starting deploy ...')

for site in sites:
    path = base + '/' + site['domain']
    repo = site['repo']
    full_url = site['domain'] + '.' + domain

    if pull_code(repo, path):
        print(name + ":"+ full_url + 'deploy complete !')
        pass
    ding(full_url+' is done !')

end = time.time()
duration = math.ceil(end - start)
ding('Deploy complete in ' + str(duration) + 's.')