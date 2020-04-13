from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings
from django.core.validators import FileExtensionValidator

# Create your models here.


class BlogCategory(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default='', editable=False)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.name


class BlogSubCategory(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default='', editable=False)
    blog_category = models.ForeignKey(
        BlogCategory, on_delete=models.CASCADE, limit_choices_to={'is_active': True})

    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Blog Sub Categories"

    def __str__(self):
        return self.name


class Blog(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default='', editable=False)
    blog_category = models.ForeignKey(
        BlogCategory, on_delete=models.CASCADE, limit_choices_to={'is_active': True})
    blog_sub_category = models.ForeignKey(
        BlogSubCategory, on_delete=models.CASCADE, limit_choices_to={'is_active': True})

    total_shares = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)

    short_details = models.TextField(max_length=100, default='')
    max_details = models.TextField(default='')

    thumbnail = models.FileField(
        upload_to='blog/', validators=[FileExtensionValidator(
        ['svg', 'png', 'jpg'])], default='')

    banner = models.FileField(
        upload_to='blog/', validators=[FileExtensionValidator(
        ['svg', 'png', 'jpg'])], default='')

    is_active = models.BooleanField(verbose_name='Is Active', default=True, editable=False)
    created_on = models.DateField(
        verbose_name='Created On', default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, default=0)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.name

