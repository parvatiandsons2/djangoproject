# Generated by Django 3.0.3 on 2020-04-09 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0023_auto_20200409_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 31, 27, 869348), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 31, 27, 869348), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='announcementcategory',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 31, 27, 869348), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='announcementtype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 31, 27, 868351), editable=False, verbose_name='Created On'),
        ),
    ]
