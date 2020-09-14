# Generated by Django 3.1 on 2020-08-21 16:23

from django.db import migrations, models
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_switchmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputNumberModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f', simplepro.components.fields.InputNumberField(default=1, help_text='继承自IntegerField', verbose_name='InputNumber计数器')),
            ],
            options={
                'verbose_name': 'InputNumber计数器',
                'verbose_name_plural': 'InputNumber计数器',
            },
        ),
    ]
