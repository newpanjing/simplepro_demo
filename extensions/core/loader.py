import os
import importlib

DATA = {
    'apps': []
}

IS_READY = False


def setup(app):
    # apps.is_installed(app_name)
    global DATA, IS_READY

    if IS_READY:
        return
    IS_READY = True

    # print('init extensions')

    __scan()
    # print(app)


def __scan():
    """
    扫描插件包目录，动态加载和注册url
    :return:
    """
    plugins_dir = os.path.join(os.getcwd(), 'plugins')

    # 如果插件目录不存在，就不处理
    if not os.path.exists(plugins_dir):
        print('Tip! There is no plug-in directory and it will be created automatically')
        os.makedirs(plugins_dir)
        print('Creating a successful! {}'.format(plugins_dir))

        return

    # 读取所有文件夹
    for f in os.listdir(plugins_dir):
        p = os.path.join(plugins_dir, f)
        if os.path.isdir(p):
            # 如果文件中有package.py 才当做一个插件
            if 'package.py' in os.listdir(p):
                # 如果app包不合格，就不加载

                load(p, 'plugins', f)
                # 初始化 安装包

    done()


def done():
    # 有app的时候才注册
    if len(DATA.get("apps")) == 0:
        return
    # print('加载完成，开始注册')
    # 完成加载后，重新注册app
    from django.apps import apps
    from django.conf import settings
    from collections import OrderedDict

    apps.app_configs = OrderedDict()
    apps.ready = False
    apps.loading = False
    apps.populate(settings.INSTALLED_APPS)

    # 注册app完成
    # print('register app done.')


def load(path, root, p):
    # print('load:{}'.format(path))

    # 检查是否有conf文件
    conf_path = os.path.join(path, 'settings.py')
    if os.path.exists(conf_path):
        load_settings('{}.{}.{}'.format(root, p, 'settings'))

    # 检查是否有urls.py文件
    urls_path = os.path.join(path, 'urls.py')
    if os.path.exists(urls_path):
        load_urls('{}.{}.{}'.format(root, p, 'urls'))
    # 检查是否有迁移文件
    # TODO 待处理

    # load app
    info = load_app('{}.{}'.format(root, p))
    DATA.get('apps').append(info)


def add_app(app):
    from django.apps import apps
    from django.conf import settings
    from collections import OrderedDict

    # TODO 判断settings，如果不启用插件中心，就不注册

    if app not in settings.INSTALLED_APPS:
        apps.app_configs = OrderedDict()
        apps.ready = False
        apps.loading = False
        settings.INSTALLED_APPS.append(app)
        apps.populate(settings.INSTALLED_APPS)


def load_app(p):
    # print('加载核心app:{}'.format(p))

    from django.conf import settings
    if hasattr(settings, 'INSTALLED_APPS'):
        INSTALLED_APPS = getattr(settings, 'INSTALLED_APPS')

        if p not in INSTALLED_APPS:
            INSTALLED_APPS.append(p)
        # 让django加载app

    return get_app_info(p)


def get_app_info(p):
    package = importlib.import_module(p + '.package')

    return {
        'name': package.NAME,
        'version': package.VERSION,
        'icon': package.ICON,
        'short_description': package.SHORT_DESCRIPTION,
        'description': package.DESCRIPTION,
        'author': package.AUTHOR,
        'email': package.EMAIL,
        'home': package.HOME,
    }


def load_settings(p):
    # 载入settings文件规则，如果是变量就覆盖，数组就追加，字典就替换和追加
    from django.conf import settings

    p_settings = importlib.import_module(p)
    # print(p_settings)

    d = p_settings.__dict__
    for item in d:
        if item.find('__') != 0:
            # print(item)
            pv = getattr(p_settings, item)
            if hasattr(settings, item):
                val = getattr(settings, item)
                t = type(val)
                if t is list or t is tuple:
                    for v in pv:
                        if v not in val:
                            val.append(v)

                elif t is dict:
                    for k in pv:
                        val[k] = pv[k]
            else:
                setattr(settings, item, pv)

    # 处理左边菜单
    if hasattr(p_settings, 'MENUS'):
        menus = getattr(p_settings, 'MENUS')
        CONFIG = {}
        if hasattr(settings, 'SIMPLEUI_CONFIG'):
            CONFIG = getattr(settings, 'SIMPLEUI_CONFIG')
        else:
            setattr(settings, 'SIMPLEUI_CONFIG', CONFIG)

        if 'menus' in CONFIG:
            CONFIG['menus'].extend(menus)
        else:
            CONFIG['menus'] = menus
        if 'system_keep' not in CONFIG:
            CONFIG['system_keep'] = True
        setattr(settings, 'SIMPLEUI_CONFIG', CONFIG)
        # print(settings.SIMPLEUI_CONFIG)


def load_urls(p):
    # print('载入urls文件：{}'.format(p))

    from django.conf import settings
    from django.conf.urls import url
    from django.urls import include
    # from django.core import management

    # print(settings)
    urls = __import__(settings.ROOT_URLCONF).urls
    #
    p_urls = importlib.import_module(p)
    if hasattr(p_urls, 'urlpatterns') and p_urls.urlpatterns:

        # 如果有app_name 就include，没有就追加
        if hasattr(p_urls, 'app_name'):
            urls.urlpatterns.append(url(r'^{}/'.format(p_urls.app_name), include(p, namespace=p_urls.app_name)), )
        else:
            # 追加app的urls
            urls.urlpatterns += p_urls.urlpatterns


if __name__ == '__main__':
    setup(None)
