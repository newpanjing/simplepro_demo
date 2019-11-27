from django.apps import AppConfig

from .core import loader

IS_READY = False


class ExtConfig(AppConfig):
    name = 'extensions'

    def ready(self):
        global IS_READY

        # 利用django的 apps的ready作为入口
        if IS_READY:
            return
        IS_READY = True

        # 将当期的url注册
        loader.load_urls('extensions.urls')

        # 注册菜单到simpleui中
        loader.load_settings('extensions.settings')

        loader.setup(self)
