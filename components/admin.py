import random
import time
from datetime import datetime

from django.contrib import admin

# Register your models here.
from django.http import JsonResponse

from components.models import *
from simpleui.admin import AjaxAdmin


@admin.register(CharModel)
class CharModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8')


@admin.register(MeditorModel)
class MeditorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'md')


@admin.register(UeditorModel)
class UeditorModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'html', 'description')


@admin.register(RadioModel)
class RadioModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'f')


@admin.register(CheckBoxModelTest)
class CheckBoxModelTestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'f')


@admin.register(SwitchModel)
class SwitchModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'f')


@admin.register(InputNumberModel)
class InputNumberModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'f')


@admin.register(SliderModel)
class SliderModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'f1', 'f2', 'f3')


@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'f1', 'f2')


@admin.register(RateModel)
class RateModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'f1', 'f2', 'f3')


@admin.register(TimeModel)
class TimeModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'f1', 'f2', 'f3')


@admin.register(DateModel)
class DateModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'f1', 'f2', 'f3')


@admin.register(DateTimeModel)
class DateTimeModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'f1', 'f2', 'f3')


@admin.register(StudentClasses)
class StudentClassesAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    pass


@admin.register(StudentOneToOneModel)
class StudentOneToOneModelAdmin(admin.ModelAdmin):
    search_fields = ('f',)


@admin.register(StudentArea)
class StudentAreaAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentManyToManyModel)
class StudentManyToManyModelAdmin(admin.ModelAdmin):
    search_fields = ('f',)


@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('classes', 'sex',)
    # 这里指定字段，对象的admin 必须定义search_fields进行搜索
    autocomplete_fields = ('classes',)
    list_display = ('pk', 'name', 'sex', 'star', 'money', 'score', 'classes')


# 一对一

@admin.register(OneToOneModel)
class OneToOneModelAdmin(admin.ModelAdmin):
    # 可以开启远程搜索，要指定对象在admin中的search_fields
    autocomplete_fields = ('one_to_one',)


@admin.register(StudentIdCard)
class StudentIdCardModelAdmin(admin.ModelAdmin):
    # 可以开启远程搜索，要指定对象在admin中的search_fields
    list_display = ('pk', 'id_card')


# 穿梭框
@admin.register(TransferManyToManyModel)
class StudentTransferModelAdmin(admin.ModelAdmin):
    search_fields = ('pk',)


@admin.register(TransferModel)
class TransferModelAdmin(admin.ModelAdmin):
    pass


# 多对多
@admin.register(ManyToManyModel)
class ManyToManyModelAdmin(admin.ModelAdmin):
    # 多对多也是可以开启 autocomplete_fields 的
    autocomplete_fields = ('many_to_many',)

    list_display = ('id', 'name', 'many_to_many_display')


# Intger字段
@admin.register(IntegerModel)
class IntegerModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Layer)
class LayerAdmin(AjaxAdmin):
    actions = ('layer_input', 'upload_file', 'async_layer_action')
    list_per_page = 10
    search_fields = ('name', 'status')
    list_filter = ('name', 'status', 'desc')

    def async_layer_action(self, request, queryset):
        """
        异步执行的方法，可以动态返回layer的配置，自simplepro 3.5版本开始
        """
        return JsonResponse({'status': 'success', 'msg': '操作成功'})

    async_layer_action.short_description = '异步获取Layer配置'
    async_layer_action.icon = 'el-icon-view'
    # 设置不选择数据也可以执行配置
    async_layer_action.enable = True

    def async_get_layer_config(self, request):
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
            'value': '123321'
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
class UUIDModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(AMapModel)
class AMapModelAdmin(admin.ModelAdmin):
    """
    高德地图支持
    """
    list_display = ('pk', 'name', 'geo', 'address')
