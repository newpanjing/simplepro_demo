import json

from django.http import HttpResponse
from django.shortcuts import render

from components.models import StudentArea


# Create your views here.

# 地区搜索
def area_search(request):
    # 使用get 请求，参数名是：term ，是为了兼容 autocomplete_fields

    term = request.GET.get('term')

    rs = []
    areas = list(StudentArea.objects.filter(name__icontains=term))
    for item in areas:
        rs.append({
            'id': item.pk,
            'text': item.name
        })
    data = {
        'pagination': {
            'more': False
        },
        'results': rs
    }

    """
    返回 数据格式例子
    
    {
        pagination: {more: false},
        results:[
            {id: "1", text: "20级1班"},
            {id: "2", text: "20级2班"},
        ]
    }    
    """

    return HttpResponse(json.dumps(data), content_type='application/json')
