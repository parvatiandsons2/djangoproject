# Generated by Django 3.0.3 on 2020-04-02 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 2, 15, 36, 48, 382282), editable=False, verbose_name='Created On'),
        ),
    ]