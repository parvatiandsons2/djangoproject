# Generated by Django 3.0.3 on 2020-04-06 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20200406_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 21, 27, 57, 389338), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 21, 27, 57, 389338), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 21, 27, 57, 388340), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 21, 27, 57, 389338), editable=False, verbose_name='Created On'),
        ),
    ]
