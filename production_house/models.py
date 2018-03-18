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
import cv2
import urllib.request
from PIL import Image
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from django.core.files import File as DjangoFile


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
    album = models.ForeignKey('Album', null = True, on_delete=models.CASCADE,)
    rating =  models.CharField(blank = True, null = True, max_length = 30)
    description =  models.CharField(blank = True, null = True, max_length = 700)
    genre =  models.ForeignKey('common.Genre', on_delete=models.CASCADE, blank = True, null = True)
    
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        super(Video, self).save(*args, **kwargs)
        self.title = self.video.name[6:][:-4]
        self.description = self.video.name[6:][:-4]
        if self.video:
            time = datetime.datetime.now()
            urllib.request.urlretrieve(self.video.url, os.path.join(BASE_DIR, self.video.name[6:]))
            vidcap = cv2.VideoCapture(os.path.join(BASE_DIR, self.video.name[6:] + time ) )
            vidcap.set(1,200)
            success,image = vidcap.read()
            success = True
            while success:
                cv2.imwrite(os.path.join(BASE_DIR, "frame_"+ self.video.name[6:][:-4] + time + ".jpg")  , image)     # save frame as JPEG file
                success,image = vidcap.read()
                
                f = DjangoFile(open(os.path.join(BASE_DIR, "frame_"+ self.video.name[6:][:-4] + time + ".jpg" ), "rb"), name = "frame_"+ self.video.name[6:][:-4] + time + ".jpg")
                self.logo = f
                break
            
            super(Video, self).save(*args, **kwargs)
            if os.path.exists(os.path.join(BASE_DIR, "frame_"+ self.video.name[6:][:-4] + time + ".jpg" )):
                os.remove(os.path.join(BASE_DIR, "frame_"+ self.video.name[6:][:-4] + time + ".jpg" ))
            if os.path.exists(os.path.join(BASE_DIR, self.video.name[6:] + time )):
                os.remove(os.path.join(BASE_DIR, self.video.name[6:] + time )) 


    class Meta:
        verbose_name_plural = "Video"



class Audio(models.Model):

    title = models.CharField(blank = True, null = True, max_length = 50)
    audio = models.FileField(blank = True, null = True, upload_to='audio')
    logo = models.ImageField(blank = True, null = True, upload_to='audio_logo')
    album = models.ForeignKey('Album', null = True, on_delete=models.CASCADE,)
    rating =  models.CharField(blank = True, null = True, max_length = 30)
    description =  models.CharField(blank = True, null = True, max_length = 700)
    genre =  models.ForeignKey('common.Genre', on_delete=models.CASCADE, blank = True, null = True)
    
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Audio"


