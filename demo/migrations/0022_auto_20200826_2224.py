# Generated by Django 3.1 on 2020-08-26 14:24

from django.db import migrations
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0021_auto_20200826_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manytomanytestmodel',
            name='score',
            field=simplepro.components.fields.ManyToManyField(blank=True, to='demo.ScoreModel', verbose_name='分数'),
        ),
    ]
