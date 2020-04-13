from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings
from django.core.validators import FileExtensionValidator
from vendor.models import Vendor
# Create your models here.


class ServiceType(models.Model):
    name = models.CharField(default='', max_length=200)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Service Type"

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(default='', max_length=200)
    code = models.CharField(default='', max_length=200,
                            verbose_name='Service Code')
    service_type = models.ForeignKey(
        ServiceType, on_delete=models.CASCADE, verbose_name='Service Type')
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, verbose_name='Vendor')
    image = models.FileField(null=True, blank=True, upload_to='service/',
                             validators=[FileExtensionValidator(
                                 ['svg', 'png', 'jpg'])],
                             verbose_name='Service Image', help_text='This image will show on Website')
    description = models.TextField(
        null=True, blank=True, max_length=500, default='')
    price = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    commission_rate = models.DecimalField(
        verbose_name='Commission Rate', default=0.00, max_digits=20, decimal_places=2)
    is_taxable = models.BooleanField(verbose_name='Is Taxable', default=True)
    tax = models.DecimalField(
        verbose_name='Tax', default=0.00, max_digits=20, decimal_places=2, help_text='Tax should be in percentage''Do not use % in text box')
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Service"

    def __str__(self):
        return self.name
