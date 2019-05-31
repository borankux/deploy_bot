import env
import os
import dingding
import template_engine

nginx_path = env.get('NGINX_PATH')
def reaload():
    os.system('service nginx reload')

def add_server(app, domain, root, type='vue'):

    conf_file_path = nginx_path + '/conf/conf.d'
    server_name = app + '.' + domain
    log_file = root + '/logs/' + app + '.access.log'

    if type == 'vue':
        root += '/' + app + '/dist'

    if type == 'laravel':
        root += '/' + app + '/public'

    tpl = os.path.abspath('./templates/nginx/' + type + '.tpl')
    template = open(tpl).read()
    final_config_file = template_engine.replace_all(template, {
        "SERVER_NAME" : server_name,
        "ROOT" : root,
        "ACCESS_LOG" : log_file
    })

    conf_file = open(conf_file_path, 'w')
    conf_file.write(final_config_file)

#add_server('console.youjiu', 'caomeidd.com', '/home/youjiu', 'vue')
