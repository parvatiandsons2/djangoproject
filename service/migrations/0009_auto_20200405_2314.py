# Generated by Django 3.0.3 on 2020-04-05 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20200405_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 5, 23, 14, 54, 587211), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 5, 23, 14, 54, 586214), editable=False, verbose_name='Created On'),
        ),
    ]
