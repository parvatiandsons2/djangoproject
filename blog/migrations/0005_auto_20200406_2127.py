# Generated by Django 3.0.3 on 2020-04-06 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200406_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 21, 27, 57, 387343), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 21, 27, 57, 360415), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='blogsubcategory',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 21, 27, 57, 387343), editable=False, verbose_name='Created On'),
        ),
    ]
