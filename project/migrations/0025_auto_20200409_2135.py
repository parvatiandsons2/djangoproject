# Generated by Django 3.0.3 on 2020-04-09 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_auto_20200409_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 35, 1, 414152), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 35, 1, 441080), editable=False, verbose_name='Created On'),
        ),
    ]
