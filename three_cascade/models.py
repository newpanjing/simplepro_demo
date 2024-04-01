from django.db import models

from simplepro.components import fields


# Create your models here.
# 过滤数据
def _get_combobox_queryset(queryset):
    # 这里可以根据自己的需要过滤数据
    return queryset.all()


class Area(models.Model):
    name = fields.CharField(max_length=32, verbose_name='名字')
    # 我们需要再model中加入simplepro的TreeCombobox组件
    parent = fields.TreeComboboxField('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='父级',
                                      strictly=True,  # 是否严格模式，严格模式只能选择叶子节点
                                      # 通过get_queryset方法获取数据
                                      queryset=_get_combobox_queryset,
                                      help_text="树形下拉框，选择父级")
    code = fields.CharField(max_length=32, verbose_name='行政区编码', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '地区'
        verbose_name_plural = verbose_name


class Person(models.Model):
    name = fields.CharField(max_length=32, verbose_name='名字')
    # 我们需要再model中加入simplepro的TreeCombobox组件
    area = fields.TreeComboboxField(Area, on_delete=models.CASCADE, null=True, blank=True, verbose_name='地区')

    address = fields.CharField(max_length=32, verbose_name='详细地址', null=True, blank=True)

    def __str__(self):
        return self.name
