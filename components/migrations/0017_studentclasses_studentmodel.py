# Generated by Django 3.1 on 2020-08-25 07:36

from django.db import migrations, models
import django.db.models.deletion
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0016_auto_20200824_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', simplepro.components.fields.CharField(max_length=32, verbose_name='班级名')),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', simplepro.components.fields.CharField(default='张三', max_length=128, verbose_name='名字')),
                ('sex', simplepro.components.fields.RadioField(choices=[(0, '男'), (1, '女'), (2, '未知')], default=0, verbose_name='性别')),
                ('star', simplepro.components.fields.RateField(default=5, help_text='给用户评级', verbose_name='评价')),
                ('money', simplepro.components.fields.InputNumberField(default=0, verbose_name='存款')),
                ('score', simplepro.components.fields.SliderField(default=100, verbose_name='考试分数')),
                ('school', models.IntegerField(choices=[(0, '北大'), (1, '清华'), (2, '复旦'), (3, '交大'), (4, '厦大'), (5, '深大'), (6, '中山大学'), (7, '东南大学'), (8, '南开大学')], default=0, verbose_name='学校')),
                ('classes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='components.studentclasses', verbose_name='班级')),
            ],
            options={
                'verbose_name': 'Select下拉框',
                'verbose_name_plural': 'Select下拉框',
            },
        ),
    ]
