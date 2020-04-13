from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings
# Create your models here.


class Vendor(models.Model):
    name = models.CharField(default='', max_length=200)
    mobile_no = models.CharField(
        verbose_name='Mobile No. ', default='', null=True, blank=True, max_length=10)
    email = models.EmailField(
        verbose_name='Email', default='', null=True, blank=True, max_length=100)
    address = models.CharField(
        verbose_name='Address', default='', null=True, blank=True, max_length=500)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    def __str__(self):
        return self.name
