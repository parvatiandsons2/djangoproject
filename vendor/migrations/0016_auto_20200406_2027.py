# Generated by Django 3.0.3 on 2020-04-06 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0015_auto_20200406_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 20, 27, 58, 561939), editable=False, verbose_name='Created On'),
        ),
    ]
