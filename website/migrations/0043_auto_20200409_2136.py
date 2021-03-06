# Generated by Django 3.0.3 on 2020-04-09 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0042_auto_20200409_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 36, 47, 379465), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 36, 47, 380463), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 36, 47, 378468), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 36, 47, 379465), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='trustedby',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 36, 47, 380463), editable=False, verbose_name='Created On'),
        ),
    ]
