# Generated by Django 3.0.3 on 2020-04-05 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200405_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 5, 23, 15, 6, 205140), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 5, 23, 15, 6, 232042), editable=False, verbose_name='Created On'),
        ),
    ]