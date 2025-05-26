"""simpleui_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.http import FileResponse
import os

admin.site.site_title = 'SimplePro 管理后台'
admin.site.site_header = 'SimplePro 管理后台 演示'
from components import views




urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+[
                  # simplepro
                  path('sp/', include('simplepro.urls')),
                  # admin界面
                  path('admin/', admin.site.urls),
                  # 其他自定义url
                  path('dialog/', include('dialog.urls')),
                  path('area/search', views.area_search, name='area_search'),
                  # 这里可以配置网页收藏夹的图标
                  path('favicon.ico', RedirectView.as_view(url=r'static/favicon.ico')),
                  # 添加media文件处理路由
                  path('', admin.site.urls),
              ]

