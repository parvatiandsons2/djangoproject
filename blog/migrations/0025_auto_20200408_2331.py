# Generated by Django 3.0.3 on 2020-04-08 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20200408_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 23, 31, 25, 269231), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 23, 31, 25, 268233), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='blogsubcategory',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 23, 31, 25, 268233), editable=False, verbose_name='Created On'),
        ),
    ]
