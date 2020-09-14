from django.contrib import admin

# Register your models here.
from components.models import *


@admin.register(CharModel)
class CharModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8')


@admin.register(MeditorModel)
class MeditorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'md')


@admin.register(UeditorModel)
class UeditorModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'html')


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
    search_fields = ('pk',)
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
    autocomplete_fields = ('classes',)
    list_display = ('pk', 'name', 'sex', 'star', 'money', 'score', 'classes')


# 一对一

@admin.register(OneToOneModel)
class OneToOneModelAdmin(admin.ModelAdmin):
    # 可以开启远程搜索，要指定对象在admin中的search_fields
    autocomplete_fields = ('one_to_one',)


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


# Intger字段
@admin.register(IntegerModel)
class IntegerModelAdmin(admin.ModelAdmin):
    pass
