# Generated by Django 3.0.3 on 2020-04-09 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0048_auto_20200409_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 36, 47, 385449), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 36, 47, 384452), editable=False, verbose_name='Created On'),
        ),
    ]