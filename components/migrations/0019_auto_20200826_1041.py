# Generated by Django 3.1 on 2020-08-26 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0018_auto_20200826_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentManyToManyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f', models.CharField(max_length=32, verbose_name='多对多')),
            ],
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='one_to_many',
            field=models.ManyToManyField(blank=True, null=True, to='components.StudentManyToManyModel', verbose_name='多对多字段'),
        ),
    ]
