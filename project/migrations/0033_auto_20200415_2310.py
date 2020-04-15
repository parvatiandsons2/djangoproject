# Generated by Django 3.0.5 on 2020-04-15 17:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0032_auto_20200412_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(default='', editable=False, max_length=200)),
                ('is_active', models.BooleanField(default=True, editable=False, verbose_name='Is Active')),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False, verbose_name='Created On')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Project Status',
            },
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(default='', editable=False, max_length=200)),
                ('is_active', models.BooleanField(default=True, editable=False, verbose_name='Is Active')),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False, verbose_name='Created On')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Project Priority',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='project.Priority'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='project.Status'),
        ),
    ]