# Generated by Django 3.0.3 on 2020-04-09 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_auto_20200409_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 27, 44, 734266), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 27, 44, 762191), editable=False, verbose_name='Created On'),
        ),
    ]