import os


def pull_code(repo, path, branch='master', verbose=False):
    os.popen('git clone ' + repo + ' ' + path).read()
    os.popen('cd' + ' ' + path + ' && make install').read()
    return True
