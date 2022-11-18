import uuid

from django.db import models
from django.utils import timezone

from simplepro.components import fields
from simplepro.editor import fields as editor_fields


# Create your models here.

class CharModel(models.Model):
    """
    文本输入框，包含：input、password、textarea
    """

    # 这里的max_length是数据库字段的长度，也是界面上文本框可输入的长度
    # type属性 对应input原生的type

    # style 原生属性，可通过width设置宽度

    # 普通文本框
    f1 = fields.CharField(verbose_name='基础输入框', max_length=128, input_type='text', placeholder='单行输入',
                          autocomplete=False, style='width:100px;color:red;')

    # 多行文本框
    # 如果设置了style的高度，就不要设置 rows属性了，不然样式会乱掉
    f2 = fields.CharField(verbose_name='多行输入', max_length=128, input_type='textarea', show_word_limit=True,
                          placeholder='多行输入', clearable=False,
                          style='width:500px;', rows=20)
    # 密码输入框
    f3 = fields.CharField(verbose_name='密码', placeholder='请输入密码', max_length=128, show_password=True)

    f4 = fields.CharField(verbose_name='左边带图标', suffix_icon="el-icon-date", max_length=128)
    f5 = fields.CharField(verbose_name='右边带图标', prefix_icon="el-icon-search", max_length=128)

    f6 = fields.CharField(verbose_name='显示可输入长度', max_length=128, show_word_limit=True)

    # solt取值：prepend、append
    f7 = fields.CharField(verbose_name='复合输入框', max_length=128, slot='prepend', slot_text='https://', null=True,
                          blank=True)

    f8 = fields.CharField(verbose_name='复合输入框', max_length=128, slot='append', slot_text='.com', null=True,
                          blank=True)

    class Meta:
        verbose_name = 'Char文本输入框'
        verbose_name_plural = 'Char文本输入框'


class MeditorModel(models.Model):
    # title = models.CharField(verbose_name='标题', max_length=128, null=True, blank=True)
    title = fields.CharField(verbose_name='标题', max_length=128, null=True, blank=True)
    md = editor_fields.MDTextField(max_length=1024, verbose_name='Markdown')
    md2 = editor_fields.MDTextField(max_length=1024, verbose_name='编辑框2', default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'markdown'
        verbose_name_plural = 'markdown 编辑器'


class UeditorModel(models.Model):
    title = fields.CharField(verbose_name='标题', max_length=128, null=True, blank=True)

    html = editor_fields.UETextField(max_length=1024, verbose_name='内容')
    description = editor_fields.UETextField(max_length=1024, verbose_name='描述', default=None, blank=True, null=True)
    detail = editor_fields.UETextField(max_length=1024, verbose_name='详情', default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Ueditor'
        verbose_name_plural = 'Ueditor 编辑器'


class RadioModel(models.Model):
    type_choices = (
        (0, '选项1'),
        (1, '选项2'),
        (2, '选项3'),
        (3, '选项4'),
    )

    # 必须包含 choices 字段，否则报错
    f = fields.RadioField(choices=type_choices, verbose_name='单选框', default=0, help_text='继承自IntegerField')

    class Meta:
        verbose_name = 'Radio单选框'
        verbose_name_plural = 'Radio单选框'


class CheckBoxModelTest(models.Model):
    type_choices = (
        (0, '选项1'),
        (1, '选项2'),
        (2, '选项3'),
        (3, '选项4'),
    )

    # 必须包含 choices 字段，否则报错

    f = fields.CheckboxField(choices=type_choices, verbose_name='复选框', default=None, blank=True, null=True,
                             help_text='继承自CharField，逗号分隔',
                             max_length=128)

    class Meta:
        verbose_name = 'Checkbox复选框'
        verbose_name_plural = 'Checkbox复选框'


class SwitchModel(models.Model):
    f = fields.SwitchField(default=False, verbose_name='Switch切换', help_text='继承自BooleanField')

    class Meta:
        verbose_name = 'Switch切换'
        verbose_name_plural = 'Switch切换'


class InputNumberModel(models.Model):
    f = fields.InputNumberField(max_value=100, min_value=1, default=1, verbose_name='InputNumber计数器',
                                help_text='继承自IntegerField')

    f2 = fields.InputNumberField(max_value=100, min_value=1, default=1, help_text='继承自IntegerField', )
    f3 = fields.InputNumberField(max_value=100, min_value=1, default=1)
    f4 = fields.InputNumberField(max_value=100, min_value=1, default=1)
    f5 = fields.InputNumberField(max_value=100, min_value=1, default=1, verbose_name='计数器2')

    f6 = fields.InputNumberField(max_value=100, min_value=1, default=1)

    class Meta:
        verbose_name = 'InputNumber计数器'
        verbose_name_plural = 'InputNumber计数器'


class SliderModel(models.Model):
    # input_size=large / medium / small / mini
    # show-tooltip
    # vertical=False
    f1 = fields.SliderField(show_input=True, max_value=100, min_value=1, step=1, input_size='large', show_tooltip=True,
                            default=1,
                            verbose_name='Slider滑块',
                            help_text='继承自IntegerField')

    f2 = fields.SliderField(max_value=1000,
                            min_value=1,
                            step=10,
                            input_size='mini',
                            width='50%',
                            default=1,
                            show_tooltip=False,
                            verbose_name='Slider滑块',
                            help_text='继承自IntegerField')

    f3 = fields.SliderField(max_value=100,
                            min_value=1,
                            step=2,
                            input_size='medium',
                            vertical=True,
                            height='100px',
                            default=1, verbose_name='Slider滑块',
                            help_text='继承自IntegerField')

    class Meta:
        verbose_name = 'Slider滑块'
        verbose_name_plural = 'Slider滑块'


class ImageModel(models.Model):
    # drag 是否可拖拽上传文件

    # accept 可以限制上传文件的类型，自版本3.4+支持
    f1 = fields.ImageField(drag=True, verbose_name='图片上传', max_length=128)
    # f1 = fields.ImageField(drag=True, verbose_name='图片上传', max_length=128, accept=".jpg")

    f2 = fields.ImageField(drag=False,
                           action='/123',  # 可以手动指定一个上传的url地址
                           verbose_name='图片上传', max_length=128, null=True, blank=True,
                           help_text='指定上传地址为/123，模拟出错')

    class Meta:
        verbose_name = 'Image图片上传'
        verbose_name_plural = 'Image图片上传'


class RateModel(models.Model):
    f1 = fields.RateField(verbose_name='评分1', max_value=5)

    # 指定最大值，和允许选半格
    f2 = fields.RateField(verbose_name='评分2', max_value=5, allow_half=True, show_score=False)

    # disabled 设为默认读
    f3 = fields.RateField(verbose_name='评分3', max_value=5, default=3.5, disabled=True)

    class Meta:
        verbose_name = 'Rate评分'
        verbose_name_plural = 'Rate评分'


class TimeModel(models.Model):
    f1 = fields.TimeField(verbose_name='Time时间选择1', size='small')

    f2 = fields.TimeField(verbose_name='Time时间选择2', default=timezone.now, clearable=False, help_text='不可清除',
                          size='mini')

    f3 = fields.TimeField(verbose_name='Time时间选择3', default=timezone.now,
                          align='right', clearable=False, editable=False, readonly=True, help_text='不可编辑')

    class Meta:
        verbose_name = 'Time时间选择'
        verbose_name_plural = 'Time时间选择'


class DateModel(models.Model):
    # options1 可以是个dict 也可以是个str，
    # 但是最终 是要一个完整的json串，
    # 否则可能导致报错控件无法显示出来

    options1 = """
    {
          disabledDate(time) {
            return time.getTime() > Date.now();
          },
          shortcuts: [{
            text: '今天',
            onClick(picker) {
              picker.$emit('pick', new Date());
            }
          }, {
            text: '昨天',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24);
              picker.$emit('pick', date);
            }
          }, {
            text: '一周前',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', date);
            }
          }]
        }
    """

    # 设置快捷选项
    f1 = fields.DateField(verbose_name='Date日期选择1', options=options1)

    f2 = fields.DateField(verbose_name='Date日期选择2', default=timezone.now, clearable=False, help_text='不可清除')

    f3 = fields.DateField(verbose_name='Date日期选择3', default=timezone.now,
                          align='right', clearable=False, editable=False, readonly=True, help_text='不可编辑')

    class Meta:
        verbose_name = 'Date日期选择'
        verbose_name_plural = 'Date日期选择'


class DateTimeModel(models.Model):
    # 可以设置 快捷操作
    # options1 可以是个dict 也可以是个str，
    # 但是最终 是要一个完整的json串，
    # 否则可能导致报错控件无法显示出来
    # 文档地址：https://element.eleme.cn/2.13/#/zh-CN/component/datetime-picker
    options1 = """
    {
          shortcuts: [{
            text: '今天',
            onClick(picker) {
              picker.$emit('pick', new Date());
            }
          }, {
            text: '昨天',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24);
              picker.$emit('pick', date);
            }
          }, {
            text: '一周前',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', date);
            }
          }]
        }
    """
    f1 = fields.DateTimeField(verbose_name='DateTime日期时间1', options=options1)

    f2 = fields.DateTimeField(verbose_name='DateTime日期时间2', default=timezone.now, clearable=False,
                              help_text='不可清除')

    f3 = fields.DateTimeField(verbose_name='DateTime日期时间3', default=timezone.now,
                              align='right', clearable=False, editable=False, readonly=True, help_text='不可编辑')

    class Meta:
        verbose_name = 'DateTime日期时间'
        verbose_name_plural = 'DateTime日期时间'


# Select，和外键测试

# 这个demo可能有人要问，班级不是class吗？为什么要写成classes，因为class是关键字
class StudentClasses(models.Model):
    name = fields.CharField(max_length=32, verbose_name='班级名', show_word_limit=True)

    def __str__(self):
        return self.name


class StudentArea(models.Model):
    name = fields.CharField(max_length=32, verbose_name='地区', show_word_limit=True)

    def __str__(self):
        return self.name


class StudentIdCard(models.Model):
    id_card = models.CharField(max_length=18, verbose_name='身份证', null=True, blank=True)

    def __str__(self):
        return self.id_card


class StudentOneToOneModel(models.Model):
    f = models.CharField(max_length=32, verbose_name='一对一')
    id_card = models.ForeignKey(StudentIdCard, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.f


class StudentManyToManyModel(models.Model):
    f = models.CharField(max_length=32, verbose_name='多对多')

    def __str__(self):
        return self.f


# 外键字段可以设置 queryset 来进行数据的筛选
def get_student_class_queryset():
    return StudentClasses.objects.order_by('-pk')[:10]


class StudentModel(models.Model):
    name = fields.CharField(max_length=128, verbose_name='名字', default='张三')

    sex_choices = (
        (0, '男'),
        (1, '女'),
        (2, '未知'),
    )
    sex = fields.RadioField(verbose_name='性别', default=0, choices=sex_choices)

    star = fields.RateField(verbose_name='评价', default=5, help_text='给用户评级')

    money = fields.InputNumberField(verbose_name='存款', default=0)

    score = fields.SliderField(verbose_name='考试分数', default=100)

    # ForeignKey和OneToOneField、ManyToManyField 都支持两个参数
    # action 是指 select在搜索的时候 请求的url，后台只需要返回 一个数组就可以搜索数据了。[{'text':'张三','id':'123'}]
    # queryset 是指 select 默认展示数据的时候 框架会调用get_queryset 可以进行数据过滤这一类处理。

    # 外键字段 如果不指定action，可以在admin中配置：autocomplete_fields = ('classes',) 就可以自动搜索了。不配置两者 就只能列表过滤
    classes = fields.ForeignKey(StudentClasses, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='班级',
                                help_text='一对多', clearable=True, placeholder='选择班级',
                                queryset=get_student_class_queryset,
                                # 这里这里可以传入function，但是返回的必须是个queryset，也可以传入queryset
                                limit=5,  # 这里限制默认显示的结果数量，设置下可以防止爆内存
                                )

    area = fields.ForeignKey(StudentArea, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='地区',
                             help_text='一对多', clearable=True, placeholder='选择地区',
                             # 指定自定义的url
                             action='/area/search'
                             )

    class Meta:
        verbose_name = '一对多 Select'
        verbose_name_plural = '一对多 Select'

    def __str__(self):
        return self.name


# Integer Select下拉框

class IntegerModel(models.Model):
    school_choices = (
        (0, '北大'),
        (1, '清华'),
        (2, '复旦'),
        (3, '交大'),
        (4, '厦大'),
        (5, '深大'),
        (6, '中山大学'),
        (7, '东南大学'),
        (8, '南开大学'),
    )
    school = fields.IntegerField(verbose_name='学校', choices=school_choices, default=0, help_text='带下拉框的int字段')

    score = fields.IntegerField(verbose_name='分数', default=100, help_text='普通int字段')

    class Meta:
        verbose_name = 'Integer字段'
        verbose_name_plural = 'Integer字段'

    def __str__(self):
        if self.school:
            return self.school_choices[self.school][1]


# 多对多 Select
class ManyToManyModel(models.Model):
    name = fields.CharField(max_length=128, verbose_name='名字', default='张三')
    many_to_many = fields.ManyToManyField(StudentManyToManyModel, blank=True, verbose_name='多对多字段')

    class Meta:
        verbose_name = '多对多 Select'
        verbose_name_plural = '多对多 Select'

    def many_to_many_display(self):
        # 多对多字段展示
        labels = []
        many = self.many_to_many.all()
        for m in many:
            # 读取字段名
            labels.append(m.f)

        return labels

    many_to_many_display.short_description = '多对多展示'

    def __str__(self):
        return self.name


# 一对一 Select

class OneToOneModel(models.Model):
    name = fields.CharField(max_length=128, verbose_name='名字', default='张三')
    one_to_one = fields.OneToOneField(StudentOneToOneModel, on_delete=models.SET_NULL, null=True, blank=True,
                                      verbose_name='一对一字段', filterable=True)

    class Meta:
        verbose_name = '一对一 Select'
        verbose_name_plural = '一对一 Select'

    def __str__(self):
        return self.name


# 穿梭框
class TransferManyToManyModel(models.Model):
    f = models.CharField(max_length=32, verbose_name='穿梭框多对多')

    def __str__(self):
        return self.f


class TransferModel(models.Model):
    name = fields.CharField(max_length=32, verbose_name='名字')

    transfer = fields.TransferField(TransferManyToManyModel, blank=True, verbose_name='穿梭框',
                                    help_text='基于many_to_many字段',
                                    filterable=True,  # 允许列表搜索
                                    placeholder='输入关键字搜索',  # 搜索框占位符
                                    titles=['待选', '已选'],  # 自定义穿梭框title
                                    button_texts=['往左', '往右']  # 自定义按钮文本
                                    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Transfer 穿梭框'
        verbose_name_plural = 'Transfer 穿梭框'


class Layer(models.Model):
    name = fields.CharField(max_length=32, verbose_name='名字')
    desc = fields.CharField(max_length=32, verbose_name='描述', null=True, blank=True)
    status = models.IntegerField(choices=((0, '默认'),
                                          (1, '其他')), verbose_name='状态', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Layer Action弹出框'
        verbose_name_plural = 'Layer Action弹出框'


def get_uuid():
    return uuid.uuid4().hex


class UUIDKeyModel(models.Model):
    uid = models.UUIDField(primary_key=True, verbose_name='uuid', default=get_uuid, editable=False)
    name = fields.CharField(max_length=32, verbose_name='名字')

    def __str__(self):
        return str(self.uid)

    class Meta:
        verbose_name = 'UUID支持'
        verbose_name_plural = 'UUID支持'


class AMapModel(models.Model):
    name = fields.CharField(verbose_name='名称', show_word_limit=True, null=True, blank=True, max_length=64)
    geo = fields.AMapField(max_length=32, verbose_name='经纬度', null=True, blank=True, help_text='点击地图获取经纬度')

    # pick_type 取值为 geo、address
    # geo 获取经纬度
    # address 获取地址
    address = fields.AMapField(max_length=128, verbose_name='地址', null=True, blank=True, help_text='点击地图获取地址',
                               pick_type='address')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '高德地图组件'
        verbose_name_plural = '高德地图组件'


# 从simplepro 5.0.0版本开始，支持视频播放组件
class VideoModel(models.Model):
    name = fields.CharField(verbose_name='名称', show_word_limit=True, null=True, blank=True, max_length=64)

    video = fields.VideoField(max_length=128, verbose_name='视频播放', null=True, blank=True, help_text='视频播放组件')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '视频播放组件'
        verbose_name_plural = '视频播放组件'


class CellActionModel(models.Model):
    name = fields.CharField(max_length=32, verbose_name='名字')
    desc = fields.CharField(max_length=32, verbose_name='描述', null=True, blank=True)
    status = models.BooleanField(verbose_name='状态', default=False)

    # 用户
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '单元格Action'
        verbose_name_plural = '单元格Action'


def _get_combobox_queryset(queryset):
    # 这里可以根据自己的需要过滤数据
    return queryset.all()


class TreeComboboxModel(models.Model):
    """
    树形下拉框，从simplepro 6.0.0版本开始支持
    """
    name = fields.CharField(max_length=32, verbose_name='名字')
    # 我们需要再model中加入simplepro的TreeCombobox组件
    parent = fields.TreeComboboxField('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='父级',
                                      strictly=True,  # 是否严格模式，严格模式只能选择叶子节点
                                      # 通过get_queryset方法获取数据
                                      queryset=_get_combobox_queryset,
                                      help_text="树形下拉框，选择父级")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '树形下拉框'
        verbose_name_plural = '树形下拉框'


class TreeTable(models.Model):
    """
    树形表格，从simplepro 6.0.0版本开始支持
    """
    name = fields.CharField(max_length=32, verbose_name='名称')

    # 这个字段，是用来处理树形表格的，有这个字段才能知道级联的关系
    # 在树形表格中，删除某一级，程序不会级联删除下面的所有子级，所以需要利用数据库的级联删除，设置on_delete=models.CASCADE
    parent = fields.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='父级')

    desc = fields.CharField(max_length=32, verbose_name='描述', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '树形表格'
        verbose_name_plural = '树形表格'


class TableSelection(models.Model):
    """
    表格复选框显示和隐藏，从simplepro 6.0.0版本开始支持
    """
    name = fields.CharField(max_length=32, verbose_name='名称')
    desc = fields.CharField(max_length=32, verbose_name='描述', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '表格复选框'
        verbose_name_plural = '表格复选框'
