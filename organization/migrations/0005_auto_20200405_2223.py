# Generated by Django 3.0.3 on 2020-04-05 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20200405_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 5, 22, 23, 49, 338254), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationindustry',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 5, 22, 23, 49, 337257), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationownership',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 5, 22, 23, 49, 337257), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationstatus',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 5, 22, 23, 49, 338254), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationtype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 5, 22, 23, 49, 337257), editable=False, verbose_name='Created On'),
        ),
    ]
