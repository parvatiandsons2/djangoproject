from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings
from customers.models import Customer
from django.core.validators import FileExtensionValidator
# Create your models here.


class Category(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default='', editable=False)
    max_details = models.TextField(default='', blank=True, null=True)

    is_active = models.BooleanField(
        verbose_name='Is Active', default=True, editable=False)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Project(models.Model):

    objects = models.Manager
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default='', editable=False)
    Link = models.CharField(max_length=1000, default='#')

    specification1 = models.CharField(
        max_length=1000, default='', blank=True, null=True)
    specification2 = models.CharField(
        max_length=1000, default='', blank=True, null=True)
    specification3 = models.CharField(
        max_length=1000, default='', blank=True, null=True)
    specification4 = models.CharField(
        max_length=1000, default='', blank=True, null=True)

    max_details = models.TextField(default='', max_length=150)

    thumbnail = models.FileField(
        upload_to='project/', validators=[FileExtensionValidator(
            ['svg', 'png', 'jpg'])], default='')

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, limit_choices_to={'is_active': True})

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, limit_choices_to={'is_active': True})

    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name
