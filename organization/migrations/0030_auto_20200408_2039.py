# Generated by Django 3.0.3 on 2020-04-08 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0029_auto_20200408_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 39, 45, 989033), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationindustry',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 39, 45, 988035), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationownership',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 39, 45, 988035), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationstatus',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 39, 45, 988035), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='organizationtype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 39, 45, 987038), editable=False, verbose_name='Created On'),
        ),
    ]
