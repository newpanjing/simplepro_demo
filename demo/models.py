import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.html import format_html


class Department(models.Model):
    name = models.CharField(max_length=128, verbose_name='部门名', help_text='一个部门的名字应该唯一', unique=True, db_index=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

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


class Image(models.Model):
    image = models.ImageField(verbose_name='图片')
    title = models.ForeignKey(Title, on_delete=models.SET_NULL, blank=False, null=True, )

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片管理'

    def __str__(self):
        return self.image.path


class Employe(models.Model):
    name = models.CharField(max_length=128, verbose_name='名称', help_text='员工的名字', null=False, blank=False,
                            db_index=True)

    gender_choices = (
        (0, '未知'),
        (1, '男'),
        (2, '女'),
    )

    gender = models.IntegerField(choices=gender_choices, verbose_name='性别', default=0)

    idCard = models.CharField(max_length=18, verbose_name='身份证号', help_text='18位的身份证号码', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='手机号')

    birthday = models.DateField(verbose_name='生日')
    time = models.TimeField(verbose_name='时间', auto_now=True)

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='部门',
                                   db_index=True)

    title = models.ForeignKey(Title, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='职务',
                              db_index=True)

    enable = models.BooleanField(verbose_name='状态', default=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

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
