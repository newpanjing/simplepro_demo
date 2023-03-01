from django.contrib import admin
from django.db.models import Sum
from django.shortcuts import redirect

from finance.models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin
from django.utils.html import format_html

from simplepro.decorators import button


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
