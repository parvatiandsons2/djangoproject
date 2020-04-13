# Generated by Django 3.0.3 on 2020-04-07 16:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0018_auto_20200407_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 7, 22, 6, 13, 555133), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationindustry',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 7, 22, 6, 13, 553135), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationownership',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 7, 22, 6, 13, 554133), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationstatus',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 7, 22, 6, 13, 554133), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationtype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 7, 22, 6, 13, 553135), editable=False, verbose_name='Created On'),
        ),
    ]