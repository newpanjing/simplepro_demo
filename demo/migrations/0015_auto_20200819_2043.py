# Generated by Django 3.1 on 2020-08-19 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0014_expert_expertcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demo3',
            options={'ordering': ('name',), 'permissions': (('batchSettings', '批量设置'),), 'verbose_name': 'demo2', 'verbose_name_plural': 'demo2'},
        ),
    ]
