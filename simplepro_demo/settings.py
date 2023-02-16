"""
Django settings for simpleui_demo project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&%up9@!s_$$4(qurnori=vit2#kg!bzs$_+m64^j$2-vzibx&p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Application definition

INSTALLED_APPS = [
    'simplepro',
    'simpleui',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'demo.apps.DemoConfig',
    # 注册自己的app
    'demo',
    'finance',
    'components',
    'dialog'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 加入simplepro的中间件
    'simplepro.middlewares.SimpleMiddleware',

    # 该中间件用于屏蔽普通用户修改密码功能，可以注释掉
    # 'simplepro_demo.middlewares.PasswordChangeMiddleware'
]

ROOT_URLCONF = 'simplepro_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'simplepro_demo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'OPTIONS': {
            # 防止数据库锁死
            'timeout': 20,
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
# LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'ja'


TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

# simpleui 设置

# 首页配置
# SIMPLEUI_HOME_PAGE = 'https://simpleui.72wo.com'
# 首页标题
# SIMPLEUI_HOME_TITLE = '百度一下你就知道'
# 首页图标,支持element-ui的图标和fontawesome的图标
# SIMPLEUI_HOME_ICON = 'el-icon-date'

# 设置simpleui 点击首页图标跳转的地址
SIMPLEUI_INDEX = 'https://www.88cto.com'

# 首页显示服务器、python、django、simpleui相关信息
# SIMPLEUI_HOME_INFO = False

# 首页显示快速操作
# SIMPLEUI_HOME_QUICK = False

# 首页显示最近动作
# SIMPLEUI_HOME_ACTION = False

# 自定义SIMPLEUI的Logo
# SIMPLEUI_LOGO = 'http://f.hiphotos.baidu.com/image/h%3D300/sign=0c78105b888ba61ec0eece2f713597cc/0e2442a7d933c8956c0e8eeadb1373f08202002a.jpg'

# 登录页粒子动画，默认开启，False关闭
# SIMPLEUI_LOGIN_PARTICLES = False

# 让simpleui 不要收集相关信息
SIMPLEUI_ANALYSIS = True

# 自定义simpleui 菜单
SIMPLEUI_CONFIG = {
    # 在自定义菜单的基础上保留系统模块
    'system_keep': True,
    'dynamic': False,
    'menus': [{
        'name': '社区',
        'icon': 'fas fa-code',
        'url': 'https://simpleui.72wo.com',
        'codename': 'community'
    }, {
        'name': '产品',
        'icon': 'fa fa-file',
        'codename': 'product',
        'models': [{
            'name': 'SimplePro',
            'codename': 'SimplePro',
            'icon': 'far fa-surprise',
            'models': [{
                'name': 'Pro文档',
                'url': 'https://simpleui.72wo.com/docs/simplepro'
            }, {
                'name': '购买Pro',
                'url': 'http://simpleui.72wo.com/simplepro'
            }]
        }, {
            'name': 'SimpleUI',
            'url': 'https://github.com/newpanjing/simpleui',
            'icon': 'fab fa-github',
            'codename': 'simpleui',
            'newTab': True
        }, {
            'name': '图片转换器',
            'url': 'https://convert.72wo.com',
            'icon': 'fab fa-github',
            'codename': 'convert',
            'newTab': True
        }, {
            'name': '全文检索',
            'url': 'https://github.com/sea-team/gofound',
            'icon': 'fab fa-github',
            'codename': 'gofound',
            'newTab': True
        }]
    }],
    "ccc": "ddd"
}

# 是否显示默认图标，默认=True
# SIMPLEUI_DEFAULT_ICON = False

# 图标设置，图标参考：
SIMPLEUI_ICON = {
    '系统管理': 'fab fa-apple',
    '员工管理': 'fas fa-user-tie'
}

# 指定simpleui 是否以脱机模式加载静态资源，为True的时候将默认从本地读取所有资源，即使没有联网一样可以。适合内网项目
# 不填该项或者为False的时候，默认从第三方的cdn获取

SIMPLEUI_STATIC_OFFLINE = True

# 隐藏所有simpleui和simplepro相关的信息
SIMPLEPRO_INFO = False

# 上传文件，如果是ImageField字段，simplepro将默认显示为图片，但是请保证有MEDIA_URL字段，否则图片将会404无法显示
# urls.py 中需要加入:+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 参考文章地址：https://www.cnblogs.com/ohahastudy/p/11179493.html
# demo 是全部已经配置好了的。

# Simplepro显示图片原理, <img src='img.url'> 将会直接读取django给到的url地址，所以不管是用本地，或者第三方的oss，都是可以的。

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/meida/'

# 配置Simple Pro是否显示首页的图标，默认为True，显示图表，False不显示
SIMPLEPRO_CHART_DISPLAY = True

# 3.1及以上版本支持
# 配置是否显示监控图表
SIMPLEPRO_MONIT_DISPLAY = True

# AUTH_USER_MODEL = 'simplepro.AuthUser'

# 默认主题
# SIMPLEUI_DEFAULT_THEME = 'dark.css'

# django新版本警告话，可以配置这句
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SIMPLEUI_LOGO='https://simpleui.72wo.com/static/images/pro/icon3.png'

# 指定SimplePro以异步的方式获取外键数据，只支持many_to_many字段 自6.3+ 开始支持
SIMPLEPRO_FK_ASYNC_DATA = True
