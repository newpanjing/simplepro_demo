from django.http import HttpResponse
from django.urls import path
from . import views

name = 'test'
# 变量必须是urlpatterns，在系统启动的时候 自动进行注册
urlpatterns = [
    path('asd', views.index, name='index'),
    path('hello', views.hello, name='hello'),
]
