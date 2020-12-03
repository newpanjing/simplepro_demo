# Generated by Django 3.1 on 2020-12-03 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0028_layer'),
    ]

    operations = [
        migrations.CreateModel(
            name='UUIDModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default='0316162fe6ce46e8aa327c70a07ce116', editable=False, verbose_name='uuid')),
            ],
            options={
                'verbose_name': 'UUID支持',
                'verbose_name_plural': 'UUID支持',
            },
        ),
    ]
