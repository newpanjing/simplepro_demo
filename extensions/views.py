import datetime

from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.views.decorators.csrf import csrf_exempt

from extensions.core import loader

import requests

from . import conf
import json


class LazyEncoder(DjangoJSONEncoder):
    """
        解决json __proxy__ 问题
    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, Promise):
            return force_text(obj)
        return str(obj)


# 为了安全，只允许登录的访问

def write(data=None, msg='ok'):
    rs = {
        'state': not data,
        'msg': 'ok',
        'data': data
    }
    return HttpResponse(json.dumps(rs), content_type='application/json')


@login_required
def index(request):
    return render(request, 'plugins/index.html', {
        'apps': loader.DATA.get('apps')
    })


@csrf_exempt
def proxy(request):
    post = json.loads(request.body.decode())
    method = post.get('method')
    url = '{}{}/'.format(conf.get_url(), method)
    r = requests.post(url, data=post)
    if r.status_code == 200:
        return HttpResponse(r.text, content_type='application/json')
    else:
        return write(msg='服务器开了小差，稍后再试！')
