import env
import os
import dingding
import template_engine

nginx_path = env.get('NGINX_PATH')


def reload():
    os.system('service nginx reload')


def add_server(server_name, path, type='vue'):
    conf_file_path = nginx_path + '/conf/conf.d/'+server_name +'.conf'

    log_file = nginx_path + '/logs/' + server_name + '.access.log'
    root = ''
    if type == 'vue':
        root = path +'/dist'

    if type == 'laravel':
        root = path + '/public'

    tpl = os.path.abspath('./templates/nginx/' + type + '.tpl')
    template = open(tpl).read()
    final_config_file = template_engine.replace_all(template, {
        "SERVER_NAME": server_name,
        "ROOT": root,
        "ACCESS_LOG": log_file
    })
    mod = 'w'
    if os.path.exists(conf_file_path):
        mod = 'w+'
    os.popen('touch '+ conf_file_path)
    conf_file = open(conf_file_path, mod)
    conf_file.write(final_config_file)
    conf_file.close()

# add_server('console.youjiu', 'caomeidd.com', '/home/youjiu', 'vue')
