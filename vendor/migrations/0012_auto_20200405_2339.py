# Generated by Django 3.0.3 on 2020-04-05 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0011_auto_20200405_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 5, 23, 39, 18, 937393), editable=False, verbose_name='Created On'),
        ),
    ]
