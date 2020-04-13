from django.db import models
from organization.models import Organization
from django.contrib.auth import settings
from django.utils.timezone import datetime

# Create your models here.


class LeadSource(models.Model):

    name = models.CharField(default='', max_length=200)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Lead Source"

    def __str__(self):
        return self.name


class Customer(models.Model):
    objects = models.manager.Manager()

    name = models.CharField(max_length=200)
    designation = models.CharField(
        max_length=200, help_text='Organization Designation')
    code = models.CharField(max_length=200, default='',
                            editable=False, blank=True, null=True)
    email = models.EmailField(
        max_length=200, default='', blank=True, null=True)
    password = models.CharField(
        max_length=20, default='', blank=True, null=True)

    mobile = models.CharField(max_length=10, default='', unique=True)
    alternate_mobile = models.CharField(
        max_length=10, default='', blank=True, null=True)

    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, limit_choices_to={'is_active': True})

    lead_source = models.ForeignKey(
        LeadSource, on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'is_active': True})

    billing_street = models.CharField(
        default='', max_length=200, null=True, blank=True)
    billing_city = models.CharField(
        default='', max_length=200, null=True, blank=True)
    billing_state = models.CharField(
        default='', max_length=200, null=True, blank=True)
    billing_code = models.CharField(
        default='', max_length=200, null=True, blank=True)
    billing_country = models.CharField(
        default='', max_length=200, null=True, blank=True)

    shipping_street = models.CharField(
        default='', max_length=200, null=True, blank=True)
    shipping_city = models.CharField(
        default='', max_length=200, null=True, blank=True)
    shipping_state = models.CharField(
        default='', max_length=200, null=True, blank=True)
    shipping_code = models.CharField(
        default='', max_length=200, null=True, blank=True)
    shipping_country = models.CharField(
        default='', max_length=200, null=True, blank=True)

    description = models.TextField(
        default='', max_length=200, null=True, blank=True)

    is_active = models.BooleanField(verbose_name='Is Active', default=True, editable=False)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name
