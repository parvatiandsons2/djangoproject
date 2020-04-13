# Generated by Django 3.0.3 on 2020-04-10 05:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20200410_1046'),
        ('project', '0029_auto_20200410_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='customer',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='customers.Customer'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 10, 10, 46, 20, 723616), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 10, 10, 46, 20, 723616), editable=False, verbose_name='Created On'),
        ),
    ]
