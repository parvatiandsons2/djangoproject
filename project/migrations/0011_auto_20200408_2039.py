# Generated by Django 3.0.3 on 2020-04-08 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20200408_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 39, 45, 977064), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 39, 45, 977064), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='projectspecification',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 39, 45, 981054), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 20, 39, 45, 950137), editable=False, verbose_name='Created On'),
        ),
    ]