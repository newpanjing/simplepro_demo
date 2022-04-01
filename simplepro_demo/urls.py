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
from django.contrib import admin
from django.http import HttpResponse
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView

admin.site.site_title = '管理后台PRO'
admin.site.site_header = '员工管理后台PRO'
from components import views
from dialog import views as dialog_views

urlpatterns = [
                  path('dialog/', include('dialog.urls')),
                  path('area/search', views.area_search, name='area_search'),
                  # 这里可以配置网页收藏夹的图标
                  path('favicon.ico', RedirectView.as_view(url=r'static/favicon.ico')),
                  # 如果出现sp 未定义，就加入这一句
                  path('sp/', include('simplepro.urls')),
                  path('', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
