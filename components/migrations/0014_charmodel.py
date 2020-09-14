# Generated by Django 3.1 on 2020-08-24 08:44

from django.db import migrations, models
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0013_datetimemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', simplepro.components.fields.CharField(max_length=128, verbose_name='基础输入框')),
                ('f2', simplepro.components.fields.CharField(max_length=128, verbose_name='基础输入框')),
                ('f3', simplepro.components.fields.CharField(max_length=128, verbose_name='基础输入框')),
                ('f4', simplepro.components.fields.CharField(max_length=128, verbose_name='基础输入框')),
                ('f5', simplepro.components.fields.CharField(max_length=128, verbose_name='基础输入框')),
                ('f6', simplepro.components.fields.CharField(max_length=128, verbose_name='基础输入框')),
            ],
            options={
                'verbose_name': 'Char文本输入框',
                'verbose_name_plural': 'Char文本输入框',
            },
        ),
    ]
