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

    # body_type =  models.ForeignKey(BodyType, blank = True, null = True)


class Customer(models.Model):

    name = models.CharField(blank = True, null = True, max_length = 50, verbose_name = "Truck RC number")
    photo = models.ImageField(blank = True, null = True)
    email =  models.CharField(blank = True, null = True, max_length = 30)
    mobile =  models.FloatField(blank = True, null = True, max_length = 20)
    old_mobile = models.CharField(blank = True, null = True, max_length = 20)
    
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Customer"
