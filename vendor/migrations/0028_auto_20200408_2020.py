# Generated by Django 3.0.3 on 2020-04-08 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0027_auto_20200408_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 20, 17, 258941), editable=False, verbose_name='Created On'),
        ),
    ]
