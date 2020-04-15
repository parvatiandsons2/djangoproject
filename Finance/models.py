from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings
from django.core.validators import FileExtensionValidator
from vendor.models import Vendor
from customers.models import Customer

# Create your models here.


class IncomeExpeseCategory(models.Model):
    objects = models.manager

    name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Income(models.Model):
    objecs = models.manager

    amount = models.DecimalField(
        default=0.00, max_digits=20, decimal_places=2)

    date = models.DateField(default=datetime.now)

    description = models.TextField()

    receipt = models.FileField(
        upload_to='income/', validators=[FileExtensionValidator(
        ['svg', 'png', 'jpg'])], blank=True, null=True)

    category = models.ForeignKey(IncomeExpeseCategory, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Income"

    def __str__(self):
        return self.amount


class Expense(models.Model):
    objecs = models.manager

    amount = models.DecimalField(
        default=0.00, max_digits=20, decimal_places=2)

    date = models.DateField(default=datetime.now)

    description = models.TextField(blank=True, null=True)

    receipt = models.FileField(
        upload_to='expense/', validators=[FileExtensionValidator(
        ['svg', 'png', 'jpg'])], blank=True, null=True)

    category = models.ForeignKey(IncomeExpeseCategory, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)

    is_active = models.BooleanField(default=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Expense"

    def __str__(self):
        return self.amount

