# Generated by Django 3.0.3 on 2020-04-08 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0006_auto_20200408_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 20, 17, 250963), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 20, 17, 250963), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='announcementcategory',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 20, 17, 250963), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='announcementtype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 20, 17, 249966), editable=False, verbose_name='Created On'),
        ),
    ]
