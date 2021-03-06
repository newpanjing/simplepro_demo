from django.contrib import admin
from django.db.models import Sum

from finance.models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin


class ProxyResource(resources.ModelResource):
    class Meta:
        model = Record


# Register your models here.
@admin.register(Record)
# class RecordAdmin(admin.ModelAdmin):
# class RecordAdmin(ImportExportModelAdmin):
# class RecordAdmin(ImportExportActionModelAdmin):
class RecordAdmin(ExportActionModelAdmin):
    resource_class = ProxyResource

    search_fields = ('name',)
    list_filter = ('type',)
    list_display = ('id', 'name', 'type', 'money', 'create_date')
    list_per_page = 10

    # 动态统计，Simple Pro独有功能
    def get_summaries(self, request, queryset):
        # 如果想统计满足当前搜索条件的数据的话 ，可以直接使用queryset.来进行统计
        # queryset.aggregate(total=Sum('money')).get('total')

        a = "￥{}".format(Record.objects.aggregate(total=Sum('money')).get('total'))
        print(a)
        # 需要有空字符串占位
        return ('', '数据合计', '', '', a, '2020年01月14日')
