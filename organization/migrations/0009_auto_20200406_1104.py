# Generated by Django 3.0.3 on 2020-04-06 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0008_auto_20200405_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 11, 4, 27, 401944), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationindustry',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 11, 4, 27, 400946), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationownership',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 11, 4, 27, 401944), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationstatus',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 11, 4, 27, 401944), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationtype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 11, 4, 27, 400946), editable=False, verbose_name='Created On'),
        ),
    ]