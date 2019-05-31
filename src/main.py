#!/anaconda3/bin/python
import time
start = time.time()

import yaml
import math
import env
import dingding
import deploy
import aliyun



with open('./site.yml') as f:
    x = yaml.safe_load(f)


name = x['name']
base = x['base']
domain = x['domain']
sites = x['sites']
dbi = env.get('ALI_DB_INSTANCE')

aliyun.setup_db()

for site in sites:
    path = base + '/' + site['domain']
    repo = site['repo']
    full_url = site['domain'] + '.' + domain
    deploy.pull_code(repo, path)


end = time.time()
duration = math.ceil(end - start)
dingding.ding_text('Deploy complete in ' + str(duration) + 's.')
