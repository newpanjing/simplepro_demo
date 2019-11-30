import os
import importlib
import zipfile


def check_app(app):
    """
    检查app是否正常
    :param app:
    :return:
    """
    require = ['NAME', 'ICON', 'SHORT_DESCRIPTION', 'DESCRIPTION', 'VERSION', 'AUTHOR', 'EMAIL', 'HOME']
    package = app + '.package'
    mod = importlib.import_module(package)
    for key in require:
        if hasattr(mod, key):
            val = getattr(mod, key)
            if type(app) != str:
                print('"{}" Must be a string.'.format(key))
                return False
            if not val or len("".join(val.split())) == 0:
                print('"{}" Can not be empty.'.format(key))
                return False

    return True


def zip_dir(source, target):
    """
    压缩文件夹
    :param source:
    :param target:
    :return:
    """
    filelist = []
    if os.path.isfile(source):
        filelist.append(source)
    else:
        for root, dirs, files in os.walk(source):
            for name in files:
                filelist.append(os.path.join(root, name))
    zf = zipfile.ZipFile(target, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(source):]
        # print arcname
        zf.write(tar, arcname)
    zf.close()


if __name__ == '__main__':
    zip_dir('/Users/panjing/dev/simplepro_demo/plugins/bbs', '/Users/panjing/Downloads/bbs.zip')
