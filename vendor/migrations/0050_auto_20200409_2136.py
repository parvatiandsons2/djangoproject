# Generated by Django 3.0.3 on 2020-04-09 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0049_auto_20200409_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 36, 47, 384452), editable=False, verbose_name='Created On'),
        ),
    ]
