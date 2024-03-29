# Generated by Django 4.1.3 on 2022-12-18 14:48

from django.db import migrations, models
import simplepro.components.fields


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0033_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=128, unique=True, verbose_name='编号')),
                ('status', simplepro.components.fields.RadioField(choices=[(101, '待支付'), (102, '已取消'), (201, '待发货')], verbose_name='状态')),
            ],
            options={
                'verbose_name': '测试订单',
                'verbose_name_plural': '测试订单',
                'db_table': 'trade_order',
            },
        ),
    ]
