# Generated by Django 3.1 on 2020-08-21 15:55

from django.db import migrations, models
import simplepro.components.fields
import simplepro.editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckBoxModelTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f', simplepro.components.fields.CheckboxField(default=0, help_text='继承自CharField，逗号分隔', max_length=128, verbose_name='复选框')),
            ],
            options={
                'verbose_name': 'Checkbox复选框',
                'verbose_name_plural': 'Checkbox复选框',
            },
        ),
        migrations.CreateModel(
            name='MeditorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('md', simplepro.editor.fields.MDTextField(max_length=1024, verbose_name='Markdown')),
            ],
            options={
                'verbose_name': 'markdown',
                'verbose_name_plural': 'markdown 编辑器',
            },
        ),
        migrations.CreateModel(
            name='RadioModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f', simplepro.components.fields.RadioField(choices=[(0, '选项1'), (1, '选项2'), (2, '选项3'), (3, '选项4')], default=0, help_text='继承自IntegerField', verbose_name='单选框')),
            ],
            options={
                'verbose_name': 'Radio单选框',
                'verbose_name_plural': 'Radio单选框',
            },
        ),
        migrations.CreateModel(
            name='UeditorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', simplepro.editor.fields.UETextField(max_length=1024, verbose_name='Ueditor')),
            ],
            options={
                'verbose_name': 'Ueditor',
                'verbose_name_plural': 'Ueditor 编辑器',
            },
        ),
    ]
