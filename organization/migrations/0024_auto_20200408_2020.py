# Generated by Django 3.0.3 on 2020-04-08 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0023_auto_20200408_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 20, 17, 257944), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationindustry',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 20, 17, 255950), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationownership',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 20, 17, 256947), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationstatus',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 20, 17, 256947), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationtype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 20, 17, 255950), editable=False, verbose_name='Created On'),
        ),
    ]
