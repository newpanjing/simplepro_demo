from django.apps import AppConfig
from django.http import HttpResponse
from django.urls import path


def aa(request):
    return HttpResponse('123', content_type='text/html')


class DemoConfig(AppConfig):
    name = 'demo'
    verbose_name = '综合管理'

    def ready(self):
        # from finance.models import Record
        # print(Record.objects.count())
        # # 扫描app的时候 对文件进行检查，除了package.py 其他文件都可以是没有
        # # 扫描所有的app，读取app中的requirements.txt 进行自动安装包
        # # 包安装完成后，读取包结构
        #
        # # 动态加载app
        #
        # # 动态注册url
        # from simplepro_demo.urls import urlpatterns
        # urlpatterns.append(path('abc', aa))
        # # super(self).ready()
        pass
