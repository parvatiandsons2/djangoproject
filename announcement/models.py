from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings
from django.core.validators import FileExtensionValidator
# Create your models here.


class AnnouncementType(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='announcementType/', default='', validators=[FileExtensionValidator(['svg','png','jpg'])])
    url = models.CharField(max_length=200, default='', editable=False)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Announcement Types"

    def __str__(self):
        return self.name


class Announcement(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default='', editable=False)

    type = models.ForeignKey(
        AnnouncementType, on_delete=models.CASCADE)

    date = models.DateField(
        verbose_name='Date', default=datetime.now)

    max_details = models.TextField(default='')

    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Announcements"

    def __str__(self):
        return self.name
