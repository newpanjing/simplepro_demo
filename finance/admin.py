import json

from django.contrib import admin
from django.db.models import Sum
from django.shortcuts import redirect

from finance.models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin
from django.utils.html import format_html

from simplepro.decorators import button
from datetime import datetime


class ProxyResource(resources.ModelResource):
    class Meta:
        model = Record


# Register your models here.
@admin.register(Record)
class RecordAdmin(ExportActionModelAdmin):
    resource_class = ProxyResource
    # native_render = True
    search_fields = ('name',)
    list_filter = ('type', 'create_date')
    list_display = ('id', 'name', 'type', 'money', 'money_display', 'create_date')
    list_per_page = 10

    actions = ('custom_btn', 'btn1')

    def money_display(self, obj):
        val = obj.money
        if val < 100:
            return format_html('<span style="color:blue">{}</span>', val)
        elif val < 1000:
            return format_html('<span style="color:green">{}</span>', val)
        else:
            return format_html('<span style="color:red">{}</span>', val)

    money_display.short_description = '金额(自定义排序)'
    money_display.admin_order_field = 'money'

    @button(
        enable=True,
        short_description='重定向按钮',
        icon='fa fa-rocket',
    )
    def btn1(self, request, queryset):
        return redirect('https://simpleui.72wo.com')

    def custom_btn(self, request, queryset):

        pass

    custom_btn.short_description = '测试按钮'

    # 动态统计，Simple Pro独有功能
    def get_summaries(self, request, queryset):
        # 如果想统计满足当前搜索条件的数据的话 ，可以直接使用queryset.来进行统计
        # queryset.aggregate(total=Sum('money')).get('total')

        a = "￥{}".format(queryset.aggregate(total=Sum('money')).get('total'))
        # 需要有空字符串占位
        return ('', '数据合计', '', '', a, '2020年01月14日')


@admin.register(DynamicDisplay)
class DynamicDisplayAdmin(admin.ModelAdmin):
    list_display = ('name', 'money', 'create_date', 'type')

    list_filter = ('type',)

    search_fields = ('name',)

    # 动态文本，Simple Pro独有功能，自6.5+版本开始支持
    def get_dynamic_render(self, request, queryset):
        # 获得当前日期
        now = datetime.now()

        # 所有查询参数都在request.POST中
        params = request.POST

        # 条件过滤参数
        print(params.get('filters'))

        # 搜索框参数
        print(params.get('search'))

        # 返回一个字典，top=顶部，bottom=底部，如果存在get_dynamic_render 那么get_top_html和get_bottom_html也会生效，不受影响
        # 如果返回的是None，顶部和底部都不会有任何显示
        # 如果top是None，那么顶部不会有任何显示
        # 如果bottom是None，那么底部不会有任何显示

        # 这里的filters返回的是一个json字符串，所以要用json转成字典

        # 默认_filter是None
        if 'filters' not in params:
            top_html = f'{now}<div style="color: blue">顶部动态文本，啥都没有</div>'
        else:
            _filter = json.loads(params.get('filters'))
            _type = _filter.get('type__exact')
            if _type == '1':
                top_html = f'{now}<div style="color: blue">顶部动态文本，你选择的是：{_type}</div>'
            else:
                top_html = f'{now}<div style="color: red">顶部动态文本，你选择的是：{_type}</div>'

        return {
            'top': top_html,
            'bottom': f'动态文本:{now}',
        }
