from django.db import models
from django.contrib.auth import settings
from django.utils.timezone import datetime
from django.core.validators import FileExtensionValidator
# Create your models here.


class OrganizationType(models.Model):

    name = models.CharField(default='', max_length=200)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Organization Types"

    def __str__(self):
        return self.name


class OrganizationIndustry(models.Model):

    name = models.CharField(default='', max_length=200)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Organization Industries"

    def __str__(self):
        return self.name


class OrganizationOwnership(models.Model):

    name = models.CharField(default='', max_length=200)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Organization Ownerships"

    def __str__(self):
        return self.name


class OrganizationStatus(models.Model):

    name = models.CharField(default='', max_length=200)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Organization Status"

    def __str__(self):
        return self.name


class Organization(models.Model):

    name = models.CharField(default='', max_length=200)
    organization_type = models.ForeignKey(
        OrganizationType, on_delete=models.CASCADE)
    organization_industry = models.ForeignKey(
        OrganizationIndustry, on_delete=models.CASCADE)
    organization_status = models.ForeignKey(
        OrganizationStatus, on_delete=models.CASCADE)
    organization_ownership = models.ForeignKey(
        OrganizationOwnership, on_delete=models.CASCADE)
    mobile_no = models.CharField(default='', max_length=10)
    website = models.CharField(
        default='', max_length=100, null=True, blank=True)

    image = models.FileField(null=True, blank=True, upload_to='organization/', validators=[FileExtensionValidator(
        ['svg', 'png', 'jpg'])],
        verbose_name='Organization Logo', help_text='This image will show on Website')

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

    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Organization"

    def __str__(self):
        return self.name
