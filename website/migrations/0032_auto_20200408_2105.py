# Generated by Django 3.0.3 on 2020-04-08 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_auto_20200408_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 21, 5, 42, 525133), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 21, 5, 42, 526130), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 21, 5, 42, 524136), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 21, 5, 42, 525133), editable=False, verbose_name='Created On'),
        ),
    ]