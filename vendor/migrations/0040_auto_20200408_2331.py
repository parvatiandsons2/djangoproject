# Generated by Django 3.0.3 on 2020-04-08 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0039_auto_20200408_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 23, 31, 25, 275089), editable=False, verbose_name='Created On'),
        ),
    ]
