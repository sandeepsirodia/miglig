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







