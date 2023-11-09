import random
import time
from datetime import datetime

from django.contrib import admin
from django.http import JsonResponse

from components.models import *
from simplepro.action import CellAction, CellMultipleAction
from simplepro.decorators import button, layer
from simpleui.admin import AjaxAdmin


class SourceCodeAdmin(object):

    def get_bottom_html(self, request):
        source_url = f"https://github.com/newpanjing/simplepro_demo/blob/master/{self.opts.app_label}/admin.py"
        return f"""
        <el-alert
    title="提示"
    type="success">
    <div>移除本提示，请移除【{str(self.__module__)}.{self.__class__.__qualname__}中的SourceCodeAdmin】类</div>
    <div>
        <b>本页源码地址：</b>
        <el-link target="_blank" href="{source_url}" type="primary">{source_url}</el-link>
    </div>
     <div>
        <b>文档地址：</b>
        <el-link target="_blank" href="https://www.mldoo.com/docs/simplepro" type="primary">https://www.mldoo.com/docs/simplepro</el-link>
    </div>
     <div>
        <b>购买地址：</b>
        <el-link target="_blank" href="https://www.mldoo.com/simplepro" type="primary">https://www.mldoo.com/simplepro</el-link>
    </div>
     <div>
        <b>QQ群：</b>
        <div>786576510</div>
        <div>873469913</div>
        <div>722755389</div>
    </div>
  </el-alert>
        
        """


@admin.register(CharModel)
class CharModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8')


@admin.register(MeditorModel)
class MeditorAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'md')


@admin.register(UeditorModel)
class UeditorModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'html', 'description')


@admin.register(RadioModel)
class RadioModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'f')


@admin.register(CheckBoxModelTest)
class CheckBoxModelTestAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'f')


@admin.register(SwitchModel)
class SwitchModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'f')


@admin.register(InputNumberModel)
class InputNumberModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'f', 'f2', 'f3', 'f4', 'f5', 'f6')
    fieldsets = (
        ('第一列', {'fields': ('f', ('f2', 'f3'))}),
        ('第二列', {'fields': ('f4', 'f5', 'f6')}),
    )


@admin.register(SliderModel)
class SliderModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'f1', 'f2', 'f3')


@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'f1', 'f2')


@admin.register(RateModel)
class RateModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'f1', 'f2', 'f3')


@admin.register(TimeModel)
class TimeModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'f1', 'f2', 'f3')


@admin.register(DateModel)
class DateModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'f1', 'f2', 'f3')


@admin.register(DateTimeModel)
class DateTimeModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'f1', 'f2', 'f3')


@admin.register(StudentClasses)
class StudentClassesAdmin(admin.ModelAdmin, SourceCodeAdmin):
    search_fields = ('name',)
    pass


@admin.register(StudentOneToOneModel)
class StudentOneToOneModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    search_fields = ('f',)


@admin.register(StudentArea)
class StudentAreaAdmin(admin.ModelAdmin, SourceCodeAdmin):
    pass


@admin.register(StudentManyToManyModel)
class StudentManyToManyModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    search_fields = ('f',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            queryset |= self.model.objects.filter(f__contains=search_term)
        return queryset, use_distinct

@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    search_fields = ('name',)
    list_filter = ('classes', 'sex',)
    # 这里指定字段，对象的admin 必须定义search_fields进行搜索
    autocomplete_fields = ('classes',)
    list_display = ('pk', 'name', 'sex', 'star', 'money', 'score', 'classes')


# 一对一

@admin.register(OneToOneModel)
class OneToOneModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    # 可以开启远程搜索，要指定对象在admin中的search_fields
    autocomplete_fields = ('one_to_one',)


@admin.register(StudentIdCard)
class StudentIdCardModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    # 可以开启远程搜索，要指定对象在admin中的search_fields
    list_display = ('pk', 'id_card')


# 穿梭框
@admin.register(TransferManyToManyModel)
class StudentTransferModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    search_fields = ('pk',)


@admin.register(TransferModel)
class TransferModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    pass


# 多对多
@admin.register(ManyToManyModel)
class ManyToManyModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    # 多对多也是可以开启 autocomplete_fields 的
    autocomplete_fields = ('many_to_many',)

    list_display = ('id', 'name', 'many_to_many_display')

    def get_field_queryset(self, db, db_field, request):
        if db_field.name == 'many_to_many':
            return ManyToManyModel.objects.all()
        return super().get_field_queryset(db, db_field, request)

    def get_search_results(self, request, queryset, search_term):
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset, False


# Intger字段
@admin.register(IntegerModel)
class IntegerModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    pass


@admin.register(Layer)
class LayerAdmin(AjaxAdmin):
    actions = ('layer_input', 'upload_file', 'async_layer_action', 'set_in')
    list_per_page = 10
    search_fields = ('name', 'status')
    list_filter = ('name', 'status', 'desc')
    list_display = ('id', 'name', 'status', 'desc')

    def get_layer_config(self, request, queryset):
        return {
            'title': '测试批量修改',
            'params': [{
                'type': 'radio',
                'key': 'type',
                'label': '修改类型',
                'require': True,
                'value': 1,
                'options': [{
                    'key': 1,
                    'label': '更新'
                }, {
                    'key': 0,
                    'label': '新增'
                }]
            }, {
                'type': 'checkbox',
                'key': 'ck',
                'label': 'Checkbox',
                'require': True,
                'value': [1],
                'options': [{
                    'key': 1,
                    'label': '更新'
                }, {
                    'key': 0,
                    'label': '新增'
                }]
            }]
        }

    # 从6.0+ 我们支持了装饰器的方式来定义action和layer
    @button("开始入库", type='warning')
    # 支持方法与dict两种方式
    @layer(get_layer_config)
    def set_in(self, request, queryset):
        for obj in queryset:
            obj.name = request.POST.get('name')
            # obj.save()
            self.message_user(request, '%s 已经入库' % obj.name)
        return JsonResponse({'status': 'success', 'msg': '入库成功'})

    def async_layer_action(self, request, queryset):
        """
        异步执行的方法，可以动态返回layer的配置，自simplepro 3.5版本开始
        """
        return JsonResponse({'status': 'success', 'msg': '操作成功'})

    async_layer_action.short_description = '异步获取Layer配置'
    async_layer_action.icon = 'el-icon-view'
    # 设置不选择数据也可以执行配置
    async_layer_action.enable = True

    def async_get_layer_config(self, request, queryset):
        """
        这个方法只有一个request参数，没有其他的入参
        """
        # 模拟处理业务耗时
        time.sleep(2)
        # 可以根据request的用户，来动态设置返回哪些字段
        return {
            # 弹出层中的输入框配置

            # 这里指定对话框的标题
            'title': '异步获取配置的输入框',
            # 提示信息
            'tips': '异步获取配置' + datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            # 确认按钮显示文本
            'confirm_button': '确认提交',
            # 取消按钮显示文本
            'cancel_button': '取消',

            # 弹出层对话框的宽度，默认50%
            'width': '40%',

            # 表单中 label的宽度，对应element-ui的 label-width，默认80px
            'labelWidth': "80px",
            'params': [{
                # 这里的type 对应el-input的原生input属性，默认为input
                'type': 'input',
                # key 对应post参数中的key
                'key': 'name',
                # 显示的文本
                'label': '名称',
                # 为空校验，默认为False
                'require': True,
                'value': random.randint(0, 100)
            }, {
                'type': 'select',
                'key': 'type',
                'label': '类型',
                'width': '200px',
                # size对应elementui的size，取值为：medium / small / mini
                'size': 'small',
                # value字段可以指定默认值
                'value': '0',
                'options': [{
                    'key': '0',
                    'label': '收入'
                }]
            }]
        }

    # 这里的layer 配置下方法名就可以了，不需要写圆括号，不然不生效
    async_layer_action.layer = async_get_layer_config

    def layer_input(self, request, queryset):
        # 这里的queryset 会有数据过滤，只包含选中的数据

        post = request.POST
        # 这里获取到数据后，可以做些业务处理
        # post中的_action 是方法名
        # post中 _selected 是选中的数据，逗号分割
        if not post.get('_selected') and post.get('select_across') == '0':
            return JsonResponse(data={
                'status': 'error',
                'msg': '请先选中数据！'
            })
        else:
            return JsonResponse(data={
                'status': 'success',
                'msg': '处理成功！'
            })

    layer_input.short_description = '弹出对话框输入'
    layer_input.type = 'success'
    layer_input.icon = 'el-icon-s-promotion'

    # 设置不选中数据也可以执行操作
    layer_input.enable = True
    # 指定一个输入参数，应该是一个数组

    # 指定为弹出层，这个参数最关键
    layer_input.layer = {
        # 弹出层中的输入框配置

        # 这里指定对话框的标题
        'title': '弹出层输入框',
        # 提示信息
        'tips': '这个弹出对话框是需要在admin中进行定义，数据新增编辑等功能，需要自己来实现。',
        # 确认按钮显示文本
        'confirm_button': '确认提交',
        # 取消按钮显示文本
        'cancel_button': '取消',

        # 弹出层对话框的宽度，默认50%
        'width': '40%',

        # 表单中 label的宽度，对应element-ui的 label-width，默认80px
        'labelWidth': "80px",
        'params': [{
            # 这里的type 对应el-input的原生input属性，默认为input
            'type': 'input',
            # key 对应post参数中的key
            'key': 'name',
            # 显示的文本
            'label': '名称',
            # 为空校验，默认为False
            'require': True,
            'value': '123321',
            # 附加参数
            'extras': {
                'prefix-icon': 'el-icon-delete',
                'suffix-icon': 'el-icon-setting',
                'clearable': True
            }
        }, {
            'type': 'select',
            'key': 'type',
            'label': '类型',
            'width': '200px',
            # size对应elementui的size，取值为：medium / small / mini
            'size': 'small',
            # value字段可以指定默认值
            'value': '0',
            'options': [{
                'key': '0',
                'label': '收入'
            }, {
                'key': '1',
                'label': '支出'
            }]
        }, {
            'type': 'number',
            'key': 'money',
            'label': '金额',
            # 设置默认值
            'value': 1000
        }, {
            'type': 'date',
            'key': 'date',
            'label': '日期',
        }, {
            'type': 'datetime',
            'key': 'datetime',
            'label': '时间',
        }, {
            'type': 'rate',
            'key': 'star',
            'label': '评价等级'
        }, {
            'type': 'color',
            'key': 'color',
            'label': '颜色'
        }, {
            'type': 'slider',
            'key': 'slider',
            'label': '滑块'
        }, {
            'type': 'switch',
            'key': 'switch',
            'label': 'switch开关'
        }, {
            'type': 'input_number',
            'key': 'input_number',
            'label': 'input number'
        }, {
            'type': 'checkbox',
            'key': 'checkbox',
            # 必须指定默认值
            'value': [],
            'label': '复选框',
            'options': [{
                'key': '0',
                'label': '收入'
            }, {
                'key': '1',
                'label': '支出'
            }, {
                'key': '2',
                'label': '收益'
            }]
        }, {
            'type': 'radio',
            'key': 'radio',
            'label': '单选框',
            'options': [{
                'key': '0',
                'label': '收入'
            }, {
                'key': '1',
                'label': '支出'
            }, {
                'key': '2',
                'label': '收益'
            }]
        }]
    }

    def upload_file(self, request, queryset):
        # 这里的upload 就是和params中配置的key一样
        upload = request.FILES['upload']
        print(upload)
        return JsonResponse(data={
            'status': 'success',
            'msg': '处理成功！'
        })

    upload_file.short_description = '文件上传对话框'
    upload_file.type = 'success'
    upload_file.icon = 'el-icon-upload'
    upload_file.enable = True

    upload_file.layer = {
        'tips': '可以推拽任何文件到这里',
        'params': [{
            'type': 'file',
            'key': 'upload',
            'label': '文件'
        }]
    }


@admin.register(UUIDKeyModel)
class UUIDModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    list_display = ('pk', 'name')


@admin.register(AMapModel)
class AMapModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    """
    高德地图支持
    """
    list_display = ('pk', 'name', 'geo', 'address')


@admin.register(VideoModel)
class VideoModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    """
    视频支持
    """
    list_display = ('pk', 'name', 'video')


@admin.register(CellActionModel)
class CellActionModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    """
    单元格直接调用action
    """
    # list_display = ("id", 'name', 'desc', 'status', 'custom_action', 'custom_multiple_action')
    list_display = ('id', 'name', 'status', 'custom_action', 'custom_multiple_action', 'custom_action_boolean')

    # 指定单元格要调用的是哪个action

    actions = ('test_action', 'test_action2', 'test_action3')

    def test_action(self, request, queryset):
        print(queryset)
        return JsonResponse(data={
            'status': 'success',
            'msg': '处理成功！'
        })

    # 可以添加一个确认提示
    test_action.confirm = "您确定要执行该操作吗？"

    def test_action2(self, request, queryset):
        print(queryset)
        return JsonResponse(data={
            'status': 'success',
            'msg': '处理成功！'
        })

    def test_action3(self, request, queryset):
        # 通过单元格执行的action，可以通过request.POST.get('ids')获取到选中的id
        # queryset 的数据只有一个，如果通过自定义按钮勾线行执行，则有多个
        if queryset.count() == 1:
            # 每次都修改状态
            obj = queryset.first()
            obj.status = not obj.status
            obj.save()
        return JsonResponse(data={
            'status': 'success',
            'msg': '修改状态成功！'
        })

    def custom_action(self, obj):
        return CellAction(text='调用', action=self.test_action)

    custom_action.short_description = '调用单个Action'

    def custom_multiple_action(self, obj):
        return CellMultipleAction(actions=[
            # 可以实用vue的组件，但是内层的click事件会被覆盖，不支持
            CellAction(text='<el-link type="primary">调用1</el-link>', action=self.test_action),
            CellAction(text='<el-link type="danger">调用2</el-link>', action=self.test_action2)
        ])

    custom_multiple_action.short_description = '调用多个Action'

    def custom_action_boolean(self, obj):
        html = '<el-link type="primary">切换状态</el-link>'
        if obj.status:
            html += ' <i class="el-icon-close" style="color:red"></i>'
        else:
            html += '<i class="el-icon-check" style="color:green"></i>'

        return CellAction(text=html, action=self.test_action3)

    custom_action_boolean.short_description = '点击Action切换状态'


@admin.register(TreeComboboxModel)
class TreeComboboxModelAdmin(admin.ModelAdmin, SourceCodeAdmin):
    """
    树形下拉框+列表筛选
    """
    list_display = ('pk', 'name', 'parent')

    list_filter = ('parent',)

    # 树形下拉框，对于admin中的list_filter，需要指定需要树形显示的字段
    # 支持list_filter_tree与方法 get_list_filter_tree
    # ⚠️注意：必须要是TreeComboboxField字段或者ForeignKey外键字段，否则将会报错
    list_filter_tree = ('parent',)

    def get_list_filter_tree(self, request):
        """
        获取list_filter_tree
        :param request:
        :return:
        """
        return self.list_filter_tree

    def get_list_filter_tree_queryset(self, request, field_name):
        """
        树形下拉框数据过滤，可以用于数据筛选和排序等，默认可以不使用，一个字段只会调用一次
        :param field_name: 字段名
        :param request: request
        :param queryset: 字段所属外键的QuerySet
        """
        if field_name == 'parent':
            return self.get_queryset(request).order_by('id')
        # 如果无返回，或者返回None，将不起任何作用


@admin.register(TreeTable)
class TreeTableAdmin(admin.ModelAdmin, SourceCodeAdmin):
    """
    树形表格
    """

    # ⚠️注意：如果存在get_queryset，这个方法将会被调用2次以上
    # 第一次获取根节点的数据，后续递归获取子节点都是通过该queryset来查询

    # 要显示的字段
    list_display = ('name', 'desc', 'parent')

    # 这个树形表格也可以结合树形下拉筛选框使用，但是这个不适合，因为表格已经树形显示了，再进行筛选，会导致树形表格无法正确的显示
    list_filter = ('parent',)

    # 指定级联关系的字段，只能一个字段，不能是数组或者元组
    # 这个字段必须有，才会有树形的效果
    list_display_tree_cascade = 'parent'

    # 展开状态，默认不展开
    list_display_tree_expand_all = False

    def get_list_display_tree_expand_all(self, request):
        return self.list_display_tree_expand_all

    def get_list_display_tree_cascade(self, request):
        """
        获取list_display_tree_cascade
        :param request:
        :return:
        """
        return self.list_display_tree_cascade


@admin.register(TableSelection)
class TableSelectionAdmin(admin.ModelAdmin, SourceCodeAdmin):
    """
    表格复选框显示和隐藏
    """
    list_display = ('pk', 'name', 'desc')

    # 是否显示表格复选框，默认显示
    show_selection = False

    # 自定义Action
    actions = ['test_action']

    @button(type='danger', short_description='调用Action', enable=True, confirm="您确定要点这个按钮吗？")
    def test_action(self, request, queryset):
        pass

    def get_show_selection(self, request):
        """
        支持方方和属性，任选其一即可，如果没有返回值或者返回值是None，则默认为True，显示复选框
        """
        return self.show_selection

    def get_top_html(self, request):
        return "<el-alert type='primary'>可以通过设置admin中的show_selection来控制是否显示表格复选框，默认显示，如果不想显示，可以设置show_selection=False" \
               "，或者重写get_show_selection方法</el-alert> "
