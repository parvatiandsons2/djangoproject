# Generated by Django 3.0.3 on 2020-04-08 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0035_auto_20200408_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 49, 48, 766142), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 49, 48, 766142), editable=False, verbose_name='Created On'),
        ),
    ]
