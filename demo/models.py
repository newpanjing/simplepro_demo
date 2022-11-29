import datetime

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.html import format_html
from simplepro.components import fields
from simplepro.components.fields import SwitchField, TransferField
from simplepro.editor.fields import UETextField

User = get_user_model()


class Department(models.Model):
    name = fields.CharField(max_length=128, verbose_name='部门名', help_text='一个部门的名字应该唯一', unique=True,
                            db_index=True)
    create_time = fields.DateTimeField(verbose_name='创建时间', auto_now=True)

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门管理"

    """
        如果有__unicode__ 方法，将会优先调用，没有在调用__str__方法
    """

    def __unicode__(self):
        return '部门' + self.name

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=128, verbose_name='职务', null=True, blank=True)

    class Meta:
        verbose_name = '职务'
        verbose_name_plural = '职务管理'

    def get_absolute_url(self):
        return reverse('title-detail-view', args=(self.name,))

    def __str__(self):
        return self.name


class ExtInfo(models.Model):
    name1 = fields.CharField(max_length=128, verbose_name='字段1', null=True, blank=True)
    name2 = fields.CharField(max_length=128, verbose_name='字段2', null=True, blank=True)
    name3 = fields.CharField(max_length=128, verbose_name='字段3', null=True, blank=True)
    name4 = fields.CharField(max_length=128, verbose_name='字段4', null=True, blank=True)
    name5 = fields.DateField(verbose_name="日期", null=True, blank=True)
    name6 = fields.DateTimeField(verbose_name="日期", null=True, blank=True)
    name7 = fields.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True, )
    name8 = fields.SwitchField(blank=False, null=True, default=True)

    title = fields.ForeignKey(Title, on_delete=models.SET_NULL, blank=False, null=True, )


class Image(models.Model):
    image = models.ImageField(verbose_name='图片')
    title = models.ForeignKey(Title, on_delete=models.SET_NULL, blank=False, null=True, )

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片管理'

    def __str__(self):
        return self.image.path


class Employe(models.Model):
    name = fields.CharField(max_length=128, verbose_name='名称', help_text='员工的名字', null=False, blank=False,
                            db_index=True)

    avatar_img = fields.ImageField(verbose_name='照片', null=True, blank=False,
                                   help_text='员工的照片，在列表会默认显示为图片')

    gender_choices = (
        (0, '未知'),
        (1, '男'),
        (2, '女'),
    )
    # images = fields.ManyToManyField(Image,  blank=True, verbose_name='照片列表')

    gender = fields.IntegerField(choices=gender_choices, verbose_name='性别', default=0)

    idCard = fields.CharField(max_length=18, verbose_name='身份证号', help_text='18位的身份证号码', blank=True,
                              null=True)
    phone = fields.CharField(max_length=11, verbose_name='手机号')

    birthday = fields.DateField(verbose_name='生日')
    time = fields.TimeField(verbose_name='时间', auto_now=True)

    department = fields.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='部门',
                                   db_index=True)

    title = fields.ForeignKey(Title, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='职务',
                              db_index=True)

    enable = fields.SwitchField(verbose_name='状态', default=True)
    create_time = fields.DateTimeField(verbose_name='创建时间', auto_now=True)

    update_time = fields.DateTimeField(verbose_name='更新时间', auto_now=True)

    def test1(self):
        return format_html('<img src="{}" height="50" width="50">', 'https://www.88cto.com/static/images/logo.png')

    def test2(self):
        if self.title:
            return format_html('<span style="color:red;">{}</span>', self.title.name)
        else:
            if self.department:
                return format_html('<span style="color:red;">{}</span>', self.department.name)

    def department_id(self):
        if self.department:
            return self.department.id

        return ""

    department_id.short_description = '部门id'
    test2.short_description = '测试'

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = "员工管理"
        permissions = (
            ('test', 'test111'),
            ('test2', 'test222'),
            ('Simpleui', 'simpleui')
        )

    def __str__(self):
        return self.name


class Customers(models.Model):
    """
    客户表，自定义主键
    """
    CS_STATUS = (
        (1, '合作'),
        (2, '终止'),
        (3, '开发'),
    )
    CS_TYPE = (
        (1, '采购商'),
        (2, '供应商'),
        (3, '采购&供应'),
    )
    type = models.IntegerField('客户类别', choices=CS_TYPE)
    name = models.CharField('公司名称', max_length=100, default='选填')
    lite_name = models.CharField(
        '公司简称', max_length=20, primary_key=True, help_text='如无公司则填联系人或CEO名称')
    address = models.CharField('公司地址', max_length=200, default='选填')
    phone = models.CharField('公司电话', max_length=40, default='选填')
    website = models.URLField('网址', max_length=200, default='example.com')
    business = models.CharField('主营业务', max_length=64)
    ceo = models.CharField('CEO', max_length=50, default='选填')
    email = models.EmailField('CEO邮箱', max_length=100,
                              default='example@email.com')
    ceo_phone = models.CharField('CEO电话', max_length=20, default='选填')
    contact_name = models.CharField('联系人', max_length=100)
    contact_email = models.EmailField('联系人邮箱', max_length=100)
    contact_phone = models.CharField('联系人电话', max_length=50)
    status = models.IntegerField('合作状态', choices=CS_STATUS)
    sales = models.ForeignKey(User, verbose_name='业务',
                              on_delete=models.CASCADE, null=True, blank=True)
    line_credits = models.DecimalField(
        '信用额度', default=0, max_digits=10, decimal_places=2)
    input_time = models.DateField('添加日期', default=datetime.datetime.now)
    text = models.CharField('备注', max_length=480, default='选填')
    # 让模型代码用objects能自动补全
    objects = models.Manager()

    class Meta:
        verbose_name = '客户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.lite_name


class demo1(models.Model):
    name = models.CharField(
        max_length=10,
        verbose_name='姓名'

    )
    age = models.SmallIntegerField(
        verbose_name='年龄'
    )

    def __str__(self):
        return '姓名：{},　年龄：{}'.format(self.name, self.age)

    class Meta:
        verbose_name = 'demo1'
        verbose_name_plural = verbose_name
        ordering = ('name',)


class demo2(demo1):
    class Meta:
        verbose_name = 'demo2'
        verbose_name_plural = verbose_name
        ordering = ('name',)


import uuid


def get_id():
    return str(uuid.uuid4())


class demo3(models.Model):
    """
    多字段测试
    """
    f1 = models.CharField(default=get_id, max_length=32, primary_key=True)
    f2 = models.IntegerField(default=0, null=True, blank=True)
    f3 = models.IntegerField(default=0, null=True, blank=True)
    f4 = models.IntegerField(default=0, null=True, blank=True)
    f5 = models.IntegerField(default=0, null=True, blank=True)
    f6 = models.IntegerField(default=0, null=True, blank=True)
    f7 = models.IntegerField(default=0, null=True, blank=True)
    f8 = models.IntegerField(default=0, null=True, blank=True)
    f9 = models.IntegerField(default=0, null=True, blank=True)
    f10 = models.IntegerField(default=0, null=True, blank=True)
    f11 = models.IntegerField(default=0, null=True, blank=True)
    f12 = models.IntegerField(default=0, null=True, blank=True)
    f13 = models.IntegerField(default=0, null=True, blank=True)
    f14 = models.IntegerField(default=0, null=True, blank=True)
    f15 = models.IntegerField(default=0, null=True, blank=True)
    f16 = models.IntegerField(default=0, null=True, blank=True)
    f17 = models.IntegerField(default=0, null=True, blank=True)
    f18 = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = 'demo3'
        verbose_name_plural = verbose_name
        ordering = ('pk',)
        permissions = (
            ('batchSettings', '批量设置'),
        )


class ScoreModel(models.Model):
    choices = (
        ('A', '优'),
        ('B', '良'),
        ('C', '中'),
        ('D', '差'),
    )
    name = models.CharField(choices=choices, max_length=128, verbose_name='name')

    def __str__(self):
        return self.name


class ManyToManyTestModel(models.Model):
    name = models.CharField(max_length=128, verbose_name='name')

    score = fields.ManyToManyField(ScoreModel, blank=True, verbose_name='分数')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '多对多测试'
        verbose_name_plural = verbose_name


class BaseModel(models.Model):
    """
    基类
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    create_name = models.UUIDField(null=True, blank=True, verbose_name=('创建人ID'))
    client_id = models.CharField(max_length=100, default='1', verbose_name=('ClientId'))
    client_secret = models.CharField(max_length=100, default='1', verbose_name=('ClientSecret'))
    user = models.UUIDField(verbose_name=('用户ID'), null=True, blank=True)
    deleted = SwitchField(default=False, verbose_name='删除标记')

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class ProductCategory(BaseModel):
    name = models.CharField(max_length=100, verbose_name=('商品分类'))

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Product(BaseModel):
    """
    商品
    """
    name = models.CharField(max_length=100, verbose_name='商品名称')

    category = fields.ForeignKey(ProductCategory, null=True, blank=True, verbose_name='商品品类',
                                 on_delete=models.CASCADE)
    desc = UETextField(null=True, blank=True, verbose_name='商品详情')

    hot = SwitchField(default=False, verbose_name='热门')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('商品')
        verbose_name_plural = verbose_name


class ProductTag(BaseModel):
    """
    商品标签
    这个是为了测试TabularInline的
    """
    num = fields.IntegerField(verbose_name="数字")
    name = fields.CharField(verbose_name="标签名", max_length=64)

    product = fields.ForeignKey(Product, null=True, blank=True, verbose_name=('商品'),
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = '商品标签'
        verbose_name_plural = '商品标签'

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    name = fields.CharField(verbose_name='名称', show_word_limit=True, null=True, blank=True, max_length=64)

    class Meta:
        abstract = True


class Native(BaseModel):
    class Meta:
        verbose_name = '原生页面'
        verbose_name_plural = verbose_name


class FilterMultiple(BaseModel):
    category = fields.ForeignKey(ProductCategory, null=True, blank=True, verbose_name=('商品品类'),
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = '下拉框多选'
        verbose_name_plural = verbose_name


class SupplierInfo(models.Model):
    name = fields.CharField(verbose_name='供应商名称', max_length=50, default='')
    add = fields.CharField(verbose_name='供应商地址', max_length=100, default='', null=True, blank=True)
    contact = fields.CharField(verbose_name='联系人', max_length=10, default='')
    phone = fields.CharField(verbose_name='联系人电话', max_length=20, default='', unique=True)
    compType = (
        (1, '对公账户'),
        (0, '非对公账户'),
    )
    isComp = fields.RadioField(verbose_name='属性', choices=compType, default=0)
    owner = models.ForeignKey(verbose_name='负责人', to=User, on_delete=models.SET_NULL, null=True, blank=True,
                              editable=False)

    class Meta:
        verbose_name = '供应商管理'
        verbose_name_plural = verbose_name


class ApiGroup(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID"
    )
    name = fields.CharField(max_length=16, null=True, blank=True, verbose_name="分组名称")

    class Meta:
        verbose_name = "API分组"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ApiList(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID"
    )
    name = fields.CharField(max_length=16, null=True, blank=True, verbose_name="分组名称")
    group = fields.ForeignKey(to="ApiGroup", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="所厲分组")

    class Meta:
        verbose_name = "API列表"
        verbose_name_plural = verbose_name
