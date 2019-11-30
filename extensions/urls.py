from django.conf.urls import url
from . import views

# 指定命名空间和前缀，避免和其他url重复
app_name = 'plugins'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'proxy', views.proxy, name='proxy')
]
