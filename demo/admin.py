import datetime

from django.contrib import admin, messages
from django.db import transaction
from django.urls import reverse

from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin


# Register your models here.
@admin.register(Department)
class DepartmentAdmin(ImportExportActionModelAdmin):
    # 要显示的字段
    list_display = ('id', 'name', 'create_time')
    list_filter = ('name',)
    # 需要搜索的字段
    search_fields = ('name',)

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('id', 'name')

    # 需要搜索的字段
    # search_fields = ('name',)

    # 分页显示，一页的数量
    list_per_page = 10
    inlines = [
        ImageInline,
    ]


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    """
    字段过多的情况下，可以用simplepro的特性，将列进行固定

    左边固定公司名称，右边固定联系电话

    文档参考地址：https://github.com/newpanjing/simplepro/blob/master/table.md#fields_options%E5%AD%97%E6%AE%B5
    """

    fields_options = {
        'name': {
            'fixed': 'left',
            'width': '80px',
            'align': 'center'
        },
        'contact_name': {
            'fixed': 'right',
            'width': '200px',
            'align': 'left'
        }
    }

    list_display = (
        'type', 'name', 'lite_name', 'address', 'phone', 'website', 'business', 'ceo', 'email', 'ceo_phone',
        'contact_name',
        'contact_email', 'contact_phone', 'status', 'sales', 'line_credits', 'input_time', 'text')

    list_per_page = 20
    search_fields = ('name', 'lite_name')
    list_filter = ('type',)


class AgeListFilter(admin.SimpleListFilter):
    """
    配置自定义的过滤器
    """
    title = u'最近生日'
    parameter_name = 'ages'

    def lookups(self, request, model_admin):
        return (
            ('0', u'最近7天'),
            ('1', u'最近15天'),
            ('2', u'最近30天'),
        )

    def queryset(self, request, queryset):
        # 当前日期格式
        cur_date = datetime.datetime.now().date()

        if self.value() == '0':
            # 前一天日期
            day = cur_date - datetime.timedelta(days=1)

            return queryset.filter(birthday__gte=day)
        if self.value() == '1':
            day = cur_date - datetime.timedelta(days=15)
            return queryset.filter(birthday__gte=day)
        if self.value() == '2':
            day = cur_date - datetime.timedelta(days=30)
            return queryset.filter(birthday__gte=day)


class ProxyResource(resources.ModelResource):
    """
    配置导入导出
    """

    class Meta:
        model = Employe


@admin.register(Employe)
class EmployeAdmin(ImportExportActionModelAdmin):

    # save_on_top = True

    def delete_queryset(self, request, queryset):
        """
        重写delete方法
        :param request:
        :param queryset:
        :return:
        """
        queryset.delete()
        pass

    def get_queryset(self, request):
        """
        重写默认查询方法，可以用于数据权限控制
        例如张三登录后，只显示张三的数据，李四登录后就只显示李四的数据
        :param request:
        :return:
        """
        qs = super().get_queryset(request)
        return qs.filter(id__gte=1)

    def message_test(self, request, queryset):
        messages.add_message(request, messages.SUCCESS, '操作成功123123123123')
        messages.add_message(request, messages.ERROR, '操作成功123123123123')
        messages.add_message(request, messages.DEBUG, '操作成功123123123123')
        messages.add_message(request, messages.WARNING, '操作成功123123123123')
        messages.add_message(request, messages.INFO, '操作成功123123123123')

    message_test.short_description = '消息测试'

    # 设置按钮默认是否可点击，如果默认可点击，获取到的queryset将会是一个空的
    message_test.enable = True

    # 给按钮增加确认
    message_test.confirm = '你是否执意要点击这个按钮？'

    class Media:
        js = ('/js/test.js',)
        # css = ('test.css',)

    resource_class = ProxyResource
    list_display = (
        'id', 'name', 'gender', 'phone', 'birthday', 'department', 'department_id', 'enable', 'create_time', 'test1',
        'test2')
    # search_fields = ('name', 'enable', 'idCard', 'department')
    search_fields = ('name', 'department__name')

    list_per_page = 5
    raw_id_fields = ('department', 'title')
    list_filter = ('department', AgeListFilter, 'create_time', 'department__create_time')
    # list_filter = (AgeListFilter, 'department', 'create_time', 'birthday', 'time', 'enable', 'gender')

    list_display_links = ('name',)

    list_editable = ('department', 'phone', 'birthday', 'enable', 'gender')

    date_hierarchy = 'create_time'

    fieldsets = [(None, {'fields': ['name', 'gender', 'phone']}),
                 (u'其他信息', {
                     'classes': ('123',),
                     'fields': ['birthday', 'department', 'enable']})]

    @transaction.atomic
    def test(self, request, queryset):
        return {
            'state': False,
            'msg': '用户关联的数据还没有删除！'
        }

    # 增加自定义按钮
    actions = [test, 'make_copy', 'custom_button', 'message_test', 'exception_test']

    def custom_button(self, request, queryset):
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = '测试按钮'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'danger'

    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'

    # 链接按钮，设置之后直接访问该链接
    # 3中打开方式
    # action_type 0=当前页内打开，1=新tab打开，2=浏览器tab打开
    # 设置了action_type，不设置url，页面内将报错

    custom_button.action_type = 1
    custom_button.action_url = 'https://www.baidu.com'

    def make_copy(self, request, queryset):
        messages.add_message(request, messages.SUCCESS, '复制员工成功！')
        # 这里是需要判断是否选中全部，选中全部后，ids将无法获取，界面就会弹出错误提示
        ids = request.POST.get('ids').split(',')
        for id in ids:
            employe = Employe.objects.get(id=id)

            Employe.objects.create(
                name=employe.name,
                idCard=employe.idCard,
                phone=employe.phone,
                birthday=employe.birthday,
                department_id=employe.department_id
            )

    make_copy.short_description = '复制员工'

    def exception_test(self, request, qs):
        raise Exception('错误测试')

    exception_test.short_description = '点击报错'

    # simplepro 增加属性
    # def formatter(self, obj, field_name, value):
    #     # 这里可以对value的值进行判断，比如日期格式化等
    #     if field_name == 'department_id':
    #         return format_html('<span style="font-weight:700">{}</span>', value)

    # 模拟报错
    # if 1 == 1:
    #     raise Exception('test')

    # return value

    # 显示隐藏action，默认为True，只有显式指定为False的时候才隐藏
    # actions_show = False

    # admin 中字段设置，及时list_display 未定义该字段，在这里设置了也不会出错
    # 表头字段完全遵循elementui的table文档，https://element.eleme.cn/#/zh-CN/component/table
    # fields_options支持自定义字段的值，比如model中的自定义方法 就算自定义字段

    # 目前支持以下属性
    # fixed 取值 left 和right
    # width 取值 任意
    # algin 取值left center right
    # min_width 最小宽度
    # resizable
    # class_name
    # label_class_name

    fields_options = {
        'id': {
            'fixed': 'left',
            'width': '80px',
            'align': 'center'
        },
        'create_time': {
            'fixed': 'right',
            'width': '200px',
            'align': 'left'
        }
    }

    def get_list_display(self, request):
        # 这里可以进行判断，动态返回某些字段或表头
        return self.list_display

    def get_list_filter(self, request):
        # 这里可以进行判断，动态返回list_filter
        return self.list_filter

    def get_actions(self, request):
        # 这里可以进行判断，动态返回actions
        actions = super(EmployeAdmin, self).get_actions(request)
        return actions
