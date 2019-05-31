#!/anaconda3/bin/python
# import time
# start = time.time()

import yaml
import math
import env
import dingding
import deploy
import aliyun
import nginx



with open('./site.yml') as f:
    x = yaml.safe_load(f)


app_title = x['title']
app_name = x['name']
base = x['base']
domain = x['domain']
sites = x['sites']
host = x['host']
dbi = env.get('ALI_DB_INSTANCE')

aliyun.create_account(dbi, app_name)
for site in sites:
    name = site['name']
    path = base + '/' + name
    repo = site['repo']
    url = name + '.' + domain
    type = site['type']

    # set up account
    # set up domain
    # set up code
    # set up nginx
    # restart nginx

    #deploy.pull_code(repo, path)
    print(" repo: " + repo)
    print(" path: " + path)
    print(" url:" + url)
    print("-------------------")
# end = time.time()
# duration = math.ceil(end - start)
# dingding.ding_text('Deploy complete in ' + str(duration) + 's.')

