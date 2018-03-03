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
from miglig.settings import BASE_DIR
# import cv2
# import urllib.request


class Company(models.Model):

    name = models.CharField(blank = True, null = True, max_length = 50)
    logo = models.ImageField(blank = True, null = True, upload_to='company_logo')
    email =  models.CharField(blank = True, null = True, max_length = 30)
    contact_name =  models.CharField(blank = True, null = True, max_length = 20)
    contact_mobile =  models.CharField(blank = True, null = True, max_length = 15)
    landline = models.CharField(blank = True, null = True, max_length = 18)
    video_count = models.IntegerField(blank = True, null = True)
    
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Company"


class Album(models.Model):

    name = models.CharField(blank = True, null = True, max_length = 50)
    logo = models.ImageField(blank = True, null = True, upload_to='album_logo')
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
    video = models.FileField(blank = True, null = True, upload_to='video')
    logo = models.ImageField(blank = True, null = True, upload_to='video_logo')
    rating =  models.CharField(blank = True, null = True, max_length = 30)
    description =  models.CharField(blank = True, null = True, max_length = 700)
    genre =  models.ForeignKey('common.Genre', on_delete=models.CASCADE, blank = True, null = True)
    
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)

    def __str__(self):
        return str(self.pk)

    # def save(self, *args, **kwargs):
    #     urllib.request.urlretrieve(self.video.url, ".r")
    #     print(cv2.__version__)
    #     vidcap = cv2.VideoCapture(self.video.url)
    #     success,image = vidcap.read()
    #     success = True
    #     while success:
    #         cv2.imwrite("frame%d.jpg" , image)     # save frame as JPEG file
    #         success,image = vidcap.read()
    #         print ('Read a new frame: ', success)
    #         self.logo = image
    #         break

    #     super(Video, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = "Video"



class Audio(models.Model):

    title = models.CharField(blank = True, null = True, max_length = 50)
    audio = models.FileField(blank = True, null = True, upload_to='audio')
    logo = models.ImageField(blank = True, null = True, upload_to='audio_logo')
    rating =  models.CharField(blank = True, null = True, max_length = 30)
    description =  models.CharField(blank = True, null = True, max_length = 700)
    genre =  models.ForeignKey('common.Genre', on_delete=models.CASCADE, blank = True, null = True)
    
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Audio"


