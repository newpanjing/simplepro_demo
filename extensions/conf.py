import os


def get_url():
    return 'http://localhost:8002/appapi/'


def get_plugin_dir():
    """
    获取插件目录
    :return:
    """
    return os.path.join(os.getcwd(), 'plugins'), 'plugins'
