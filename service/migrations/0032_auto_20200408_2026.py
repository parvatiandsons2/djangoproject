# Generated by Django 3.0.3 on 2020-04-08 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0031_auto_20200408_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 26, 29, 719631), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 26, 29, 718634), editable=False, verbose_name='Created On'),
        ),
    ]
