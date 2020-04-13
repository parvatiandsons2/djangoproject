from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings
from django.core.validators import FileExtensionValidator

# Create your models here.


class Slider(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)
    title = models.CharField(default='text <strong class=text-primary>Highlighted text </strong>text',
                             max_length=500, help_text="Please enter html tag with data")
    details = models.CharField(max_length=500)

    highlightedBtnText = models.CharField(verbose_name='Highlighted Button Text',
                                          max_length=500, help_text="Please enter html tag with text")
    highlightedBtnLink = models.CharField(
        verbose_name='Highlighted Button Link', max_length=500)

    regularBtnText = models.CharField(verbose_name='Regular Button Text',
                                      max_length=500, help_text="Please enter html tag with text")
    regularBtnLink = models.CharField(
        verbose_name='Regular Button Link', max_length=500)

    image = models.ImageField(upload_to='slider/',
                              verbose_name='Slider Image', help_text='This image will show on Website')
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Sliders"

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)

    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.name


class Alert(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)
    alertClass = models.CharField(max_length=200, help_text='Danger alert clas => <b>alert alert-danger bg-danger text-white</b> <br><br>'
                                  'Success alert clas => <b>alert alert-success bg-success text-white</b> <br><br>'
                                  'Primary alert clas => <b>alert alert-primary bg-primary text-white</b> <br><br>'
                                  'Warning alert clas => <b>alert alert-warning bg-warning text-white</b> ')
    message = models.TextField(
        max_length=1000, help_text='You can attach html tags in this box')

    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Alerts"

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=10)

    message = models.TextField(
        max_length=1000)

    is_active = models.BooleanField(
        verbose_name='Is Active', default=True, editable=False)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    # created_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.name


class TrustedBy(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=800)
    image = models.FileField(null=True, blank=True, upload_to='trusted/',
                             validators=[FileExtensionValidator(
                                 ['svg', 'png', 'jpg'])],
                             verbose_name='Brand Image', help_text='This image will show on Website')

    message = models.TextField(
        max_length=60)

    is_active = models.BooleanField(
        verbose_name='Is Active', default=True, editable=False)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Trusted By"

    def __str__(self):
        return self.name


class CompanyStats(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)
    customers = models.CharField(max_length=200)
    happy_clients = models.CharField(max_length=200)
    projects = models.CharField(max_length=200)
    enquiry = models.CharField(max_length=200)

    is_active = models.BooleanField(
        verbose_name='Is Active', default=True, editable=False)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Company Stats"

    def __str__(self):
        return self.name
