import env
import os
import dingding

nginx_path = env.get('NGINX_PATH')
def reaload():
    os.system('service nginx reload')

def add_server(app, domain, root, type='vue'):

    conf_file = nginx_path + '/conf/conf.d'
    server_name = app + '.' + domain
    log_file = root + '/logs/' + app + '.access.log'

    tpl = os.path.abspath('./templates/nginx/' + type + '.tpl')
    template = open(tpl).read()


    print(template)
    if type == 'vue':
        root += '/' + app + '/dist'

    if type == 'laravel':
        root += '/' + app + '/public'

    if os.path.exists(conf_file):
        os.system('rm -rf ' + conf_file)

add_server('console.youjiu', 'caomeidd.com', '/home/youjiu', 'vue')
