import os


def pull_code(repo, path, branch='master'):
    print('Pulling repository...')
    gc = os.system('git clone ' + repo + ' ' + path)
    if gc != 0:
        return gc
    print('Done !')

    print('Installing packages...')
    mf = os.system('cd' + ' ' + path + ' && make install')
    if mf != 0:
        return mf
    print('Done !')
    return True
