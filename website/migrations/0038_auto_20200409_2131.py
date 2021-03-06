# Generated by Django 3.0.3 on 2020-04-09 16:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0037_auto_20200409_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trusted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=800)),
                ('image', models.ImageField(blank=True, help_text='This image will show on Website', null=True, upload_to='trusted/', verbose_name='Brand Image')),
                ('message', models.TextField(max_length=60)),
                ('is_active', models.BooleanField(default=True, editable=False, verbose_name='Is Active')),
                ('created_on', models.DateField(default=datetime.datetime(2020, 4, 9, 21, 31, 27, 874335), editable=False, verbose_name='Created On')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Trusted By',
            },
        ),
        migrations.AlterField(
            model_name='alert',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 31, 27, 873337), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 31, 27, 874335), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 31, 27, 872340), editable=False, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2020, 4, 9, 21, 31, 27, 873337), editable=False, verbose_name='Created On'),
        ),
        migrations.DeleteModel(
            name='TrustedBy',
        ),
    ]
