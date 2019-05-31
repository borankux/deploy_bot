import re


def replace(template, key, value):
    mold = re.compile('\{\{' + key + '\}\}')
    final = mold.sub(value, template)
    return final


def replace_all(template, vars):
    final = template
    for key in vars:
        final = replace(final, key, vars[key])

    return final
