# Generated by Django 3.0.3 on 2020-04-09 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_auto_20200409_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 28, 40, 224006), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 28, 40, 249937), editable=False, verbose_name='Created On'),
        ),
    ]