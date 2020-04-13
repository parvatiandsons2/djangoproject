# Generated by Django 3.0.3 on 2020-04-07 15:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(default='', editable=False, max_length=200)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_on', models.DateField(default=datetime.datetime(2020, 4, 7, 21, 22, 50, 132375), editable=False, verbose_name='Created On')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Announcement Types',
            },
        ),
        migrations.CreateModel(
            name='AnnouncementCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(default='', editable=False, max_length=200)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_on', models.DateField(default=datetime.datetime(2020, 4, 7, 21, 22, 50, 105447), editable=False, verbose_name='Created On')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Announcement Categories',
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(default='', editable=False, max_length=200)),
                ('date', models.DateField(default=datetime.datetime(2020, 4, 7, 21, 22, 50, 132375), verbose_name='Date')),
                ('max_details', models.TextField(default='')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_on', models.DateField(default=datetime.datetime(2020, 4, 7, 21, 22, 50, 132375), editable=False, verbose_name='Created On')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcement.AnnouncementCategory')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcement.AnnouncementType')),
            ],
            options={
                'verbose_name_plural': 'Announcements',
            },
        ),
    ]