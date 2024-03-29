# Generated by Django 4.1.4 on 2023-03-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_alter_record_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicDisplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('money', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='金额')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='时间')),
                ('type', models.IntegerField(choices=[(0, '收入'), (1, '支出')], verbose_name='类型')),
            ],
            options={
                'verbose_name': '动态显示',
                'verbose_name_plural': '动态显示',
            },
        ),
    ]
