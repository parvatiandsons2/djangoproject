# Generated by Django 3.0.3 on 2020-04-08 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200408_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 20, 40, 956774), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 20, 40, 955777), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='blogsubcategory',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 20, 40, 956774), editable=False, verbose_name='Created On'),
        ),
    ]
