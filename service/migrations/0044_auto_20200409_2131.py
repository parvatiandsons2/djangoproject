# Generated by Django 3.0.3 on 2020-04-09 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0043_auto_20200409_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 31, 27, 880319), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 31, 27, 879321), editable=False, verbose_name='Created On'),
        ),
    ]
