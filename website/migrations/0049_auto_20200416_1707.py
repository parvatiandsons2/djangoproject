# Generated by Django 3.0.5 on 2020-04-16 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0048_auto_20200416_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companystats',
            name='created_by',
            field=models.ForeignKey(default=0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
