import re

def replace(template, key, value):
    mold = re.compile('\{\{' + key + '\}\}')
    final = mold.sub(value, template)
    return final



def replace_all (template, vars):
    final = template
    for key in vars:
        final = replace(final, key, vars[key])

    return final
template = open('./templates/nginx/laravel.tpl', 'r').read()

res = replace_all(template, {
    'SERVER_NAME':'youjiu.app.caomeidd.com',
    'ROOT':'/home/admin/youjiu/public',
    'ACCESS_LOG':'/var/logs/youjiu.access.log'
})

print(res)