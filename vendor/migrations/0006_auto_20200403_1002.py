# Generated by Django 3.0.3 on 2020-04-03 04:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_auto_20200403_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 3, 10, 2, 14, 516220), editable=False, verbose_name='Created On'),
        ),
    ]
