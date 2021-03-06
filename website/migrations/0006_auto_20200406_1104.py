# Generated by Django 3.0.3 on 2020-04-06 05:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0005_auto_20200405_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='alertClass',
            field=models.CharField(help_text='Danger alert clas => <b>alert alert-danger bg-danger text-white</b> <br><br>Success alert clas => <b>alert alert-success bg-success text-white</b> <br><br>Primary alert clas => <b>alert alert-primary bg-primary text-white</b> <br><br>Warning alert clas => <b>alert alert-warning bg-warning text-white</b> ', max_length=200),
        ),
        migrations.AlterField(
            model_name='alert',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 11, 4, 27, 399949), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 11, 4, 27, 372024), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 6, 11, 4, 27, 398952), editable=False, verbose_name='Created On'),
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', models.CharField(max_length=10)),
                ('message', models.TextField(help_text='You can attach html tags in this box', max_length=1000)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_on', models.DateField(default=datetime.datetime(2020, 4, 6, 11, 4, 27, 399949), editable=False, verbose_name='Created On')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
