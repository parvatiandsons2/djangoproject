# Generated by Django 3.0.3 on 2020-04-03 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_auto_20200402_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 3, 9, 36, 13, 506154), editable=False, verbose_name='Created On'),
        ),
    ]
