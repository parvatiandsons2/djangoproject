# Generated by Django 3.0.3 on 2020-04-08 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20200408_1923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectspecification',
            options={'verbose_name_plural': 'Project Specifications'},
        ),
        migrations.AddField(
            model_name='projectspecification',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 19, 38, 7, 442638), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 19, 38, 7, 442638), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='projectspecification',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 19, 38, 7, 443634), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='projectspecification',
            name='is_active',
            field=models.BooleanField(default=True, editable=False, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 8, 19, 38, 7, 416679), editable=False, verbose_name='Created On'),
        ),
    ]