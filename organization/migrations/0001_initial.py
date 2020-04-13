# Generated by Django 3.0.3 on 2020-04-03 04:09

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
            name='OrganizationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_on', models.DateField(default=datetime.datetime(2020, 4, 3, 9, 39, 44, 475730), editable=False, verbose_name='Created On')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Organization Types',
            },
        ),
        migrations.CreateModel(
            name='OrganizationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_on', models.DateField(default=datetime.datetime(2020, 4, 3, 9, 39, 44, 506970), editable=False, verbose_name='Created On')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Organization Status',
            },
        ),
        migrations.CreateModel(
            name='OrganizationOwnership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_on', models.DateField(default=datetime.datetime(2020, 4, 3, 9, 39, 44, 506970), editable=False, verbose_name='Created On')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Organization Ownerships',
            },
        ),
        migrations.CreateModel(
            name='OrganizationIndustry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_on', models.DateField(default=datetime.datetime(2020, 4, 3, 9, 39, 44, 506970), editable=False, verbose_name='Created On')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Organization Industries',
            },
        ),
    ]
