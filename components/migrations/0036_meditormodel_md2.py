# Generated by Django 3.2.6 on 2021-08-18 07:37

from django.db import migrations
import simplepro.editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0035_auto_20210816_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='meditormodel',
            name='md2',
            field=simplepro.editor.fields.MDTextField(blank=True, default=None, max_length=1024, null=True, verbose_name='编辑框2'),
        ),
    ]
