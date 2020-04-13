# Generated by Django 3.0.3 on 2020-04-11 05:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0004_auto_20200411_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supportcategory',
            name='image',
        ),
        migrations.AlterField(
            model_name='supportcategory',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 11, 11, 29, 42, 346332), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='supporttype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 11, 11, 29, 42, 315089), editable=False, verbose_name='Created On'),
        ),
    ]