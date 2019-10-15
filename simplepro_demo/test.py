import datetime
import os
import django
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.encoding import force_text
from django.utils.functional import Promise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simplepro_demo.settings")
django.setup()

from django.contrib.auth.models import Permission
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
        return super(LazyEncoder, self).default(obj)


def get_action_name(name):
    name = name.replace('Can add ', '增加').replace('Can change ', '编辑').replace('Can delete ', '删除').replace('Can view ',
                                                                                                            '查看')
    return name

#
# all = Permission.objects.all()
#
# # 处理第一级
# data = {}
# # id label children
# for item in all:
#     label = item.content_type.app_label
#     if label not in data:
#         data[label] = {
#             'label': label,
#             'children': [item]
#         }
#     else:
#         d = data.get(label)
#         children = d.get('children')
#         children.append(item)
#     # print(item)
# # 处理具体的增删改查权限
#
# # 处理第二级
# for key in data:
#     item = data.get(key)
#     children = item.get('children')
#     print('开始:\n')
#
#     obj = {}
#     for i in children:
#         # 对二级归类
#         label = i.content_type.name
#         if label not in obj:
#             obj[label] = {
#                 'label': label,
#                 'children': [{
#                     'id': i.id,
#                     'label': get_action_name(i.name)
#                 }]
#             }
#         else:
#             obj[label].get('children').append({
#                 'id': i.id,
#                 'label': get_action_name(i.name)
#             })
#     array = []
#     for i in obj:
#         array.append(obj.get(i))
#     item['children'] = array
#
# jsonData = []
# for i in data:
#     jsonData.append(data.get(i))
# print(jsonData)
