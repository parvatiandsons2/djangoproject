# Generated by Django 3.0.3 on 2020-04-10 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20200410_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 10, 22, 42, 29, 447121), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='leadsource',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 10, 22, 42, 29, 446125), editable=False, verbose_name='Created On'),
        ),
    ]
