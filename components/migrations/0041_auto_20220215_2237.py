# Generated by Django 3.2 on 2022-02-15 14:37

from django.db import migrations
import simplepro.components.fields
import simplepro.editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0040_auto_20211030_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='ueditormodel',
            name='detail',
            field=simplepro.editor.fields.UETextField(blank=True, default=None, max_length=1024, null=True, verbose_name='详情'),
        ),
        migrations.AddField(
            model_name='ueditormodel',
            name='title',
            field=simplepro.components.fields.CharField(blank=True, max_length=128, null=True, verbose_name='标题'),
        ),
    ]
