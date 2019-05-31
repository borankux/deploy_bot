#!/anaconda3/bin/python
import time
start = time.time()

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
app_password = x['password']
base = x['base']
domain = x['domain']
sites = x['sites']
host = x['host']
dbi = env.get('ALI_RDS_INSTANCE')


def setup_code(sites):
    for site in sites:
        name = site['name']
        path = base + '/' + app_name + '/' + name
        repo = site['repo']
        type = site['type']
        rr = name + '.' + app_name
        server_name = rr + '.' + domain
        aliyun.add_domain_record(domain, host, rr)
        deploy.pull_code(repo, path)
        nginx.add_server(server_name, path, type)
        nginx.reload()


aliyun.setup_db(dbi, app_name, app_password, app_title)
print("------ Aliyun RDS setup complete ! --------")
setup_code(sites)
print("------ Code Deploy Complete ! --------")
nginx.reload()

end = time.time()
duration = math.ceil(end - start)
dingding.ding_md('Deploy Report, for' + 'easy_deploy:8', '### Deploy complete in *'+str(duration)+'* `s`. 🤯')