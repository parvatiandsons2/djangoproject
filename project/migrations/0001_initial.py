# Generated by Django 3.0.5 on 2020-04-16 11:55

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0006_auto_20200411_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(default='', editable=False, max_length=200)),
                ('max_details', models.TextField(blank=True, default='', null=True)),
                ('is_active', models.BooleanField(default=True, editable=False, verbose_name='Is Active')),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False, verbose_name='Created On')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
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
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(default='', editable=False, max_length=200)),
                ('Link', models.CharField(default='#', max_length=1000)),
                ('specification1', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('specification2', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('specification3', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('specification4', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('max_details', models.TextField(default='', max_length=150)),
                ('start_date', models.DateField(default=datetime.datetime.now)),
                ('due_date', models.DateField(default=datetime.datetime.now)),
                ('thumbnail', models.FileField(default='', upload_to='project/', validators=[django.core.validators.FileExtensionValidator(['svg', 'png', 'jpg'])])),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False, verbose_name='Created On')),
                ('category', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='project.Category')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
                ('priority', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='project.Priority')),
                ('status', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='project.Status')),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
