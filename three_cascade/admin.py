from django.contrib import admin

from three_cascade.models import Area, Person


# Register your models here.

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

    # 显示为树形
    list_display_tree_cascade = 'parent'

    # 展开状态，默认不展开
    list_display_tree_expand_all = False


# 注册 Person
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'address')
