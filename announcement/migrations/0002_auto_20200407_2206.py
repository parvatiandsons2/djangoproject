# Generated by Django 3.0.3 on 2020-04-07 16:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcementcategory',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcement.AnnouncementType'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 7, 22, 6, 13, 548148), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 7, 22, 6, 13, 548148), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='announcementcategory',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 7, 22, 6, 13, 548148), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='announcementtype',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 7, 22, 6, 13, 521220), editable=False, verbose_name='Created On'),
        ),
    ]