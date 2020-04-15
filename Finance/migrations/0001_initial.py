# Generated by Django 3.0.5 on 2020-04-15 18:20

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0051_auto_20200411_2353'),
        ('customers', '0006_auto_20200411_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeExpeseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('description', models.TextField()),
                ('receipt', models.FileField(blank=True, null=True, upload_to='income/', validators=[django.core.validators.FileExtensionValidator(['svg', 'png', 'jpg'])])),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finance.IncomeExpeseCategory')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.Vendor')),
            ],
            options={
                'verbose_name_plural': 'Income',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('description', models.TextField()),
                ('receipt', models.FileField(blank=True, null=True, upload_to='expense/', validators=[django.core.validators.FileExtensionValidator(['svg', 'png', 'jpg'])])),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finance.IncomeExpeseCategory')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
                ('created_by', models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.Vendor')),
            ],
            options={
                'verbose_name_plural': 'Expense',
            },
        ),
    ]
