#!/anaconda3/bin/python
import time
start = time.time()

import yaml
import math
import env
import dingding
import deploy



with open('./site.yml') as f:
    x = yaml.safe_load(f)


name = x['name']
base = x['base']
domain = x['domain']
sites = x['sites']

dingding.ding_text('starting deploy ...')


for site in sites:
    path = base + '/' + site['domain']
    repo = site['repo']
    full_url = site['domain'] + '.' + domain

    if deploy.pull_code(repo, path):
        print(name + ":"+ full_url + 'deploy complete !')
        pass
    dingding.ding_text(full_url+' is done !')

end = time.time()
duration = math.ceil(end - start)
dingding.ding_text('Deploy complete in ' + str(duration) + 's.')