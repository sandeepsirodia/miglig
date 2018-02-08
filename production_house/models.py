import os
import random
import datetime

from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator

from common.models import Genre



class Company(models.Model):

    name = models.CharField(blank = True, null = True, max_length = 50)
    logo = models.ImageField(blank = True, null = True)
    email =  models.CharField(blank = True, null = True, max_length = 30)
    contact_name =  models.CharField(blank = True, null = True, max_length = 20)
    contact_mobile =  models.IntegerField(blank = True, null = True)
    landline = models.IntegerField(blank = True, null = True)
    video_count = models.IntegerField(blank = True, null = True)
    
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Company"


class Album(models.Model):

    name = models.CharField(blank = True, null = True, max_length = 50)
    logo = models.ImageField(blank = True, null = True)
    rating =  models.CharField(blank = True, null = True, max_length = 30)
    description =  models.CharField(blank = True, null = True, max_length = 700)
    genre =  models.ForeignKey('common.Genre', on_delete=models.CASCADE, blank = True, null = True)
    
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Album"



class Video(models.Model):

    title = models.CharField(blank = True, null = True, max_length = 50)
    video = models.CharField(blank = True, null = True, max_length = 50)
    logo = models.ImageField(blank = True, null = True)
    rating =  models.CharField(blank = True, null = True, max_length = 30)
    description =  models.CharField(blank = True, null = True, max_length = 700)
    genre =  models.ForeignKey('common.Genre', on_delete=models.CASCADE, blank = True, null = True)
    
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Video"



class Audio(models.Model):

    title = models.CharField(blank = True, null = True, max_length = 50)
    audio = models.CharField(blank = True, null = True, max_length = 50)
    logo = models.ImageField(blank = True, null = True)
    rating =  models.CharField(blank = True, null = True, max_length = 30)
    description =  models.CharField(blank = True, null = True, max_length = 700)
    genre =  models.ForeignKey('common.Genre', on_delete=models.CASCADE, blank = True, null = True)
    
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Video"


