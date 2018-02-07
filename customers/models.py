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

    name = models.CharField(blank = True, null = True, max_length = 50)
    photo = models.ImageField(blank = True, null = True)
    email =  models.CharField(blank = True, null = True, max_length = 30)
    mobile =  models.IntegerField(blank = True, null = True)
    old_mobile = models.IntegerField(blank = True, null = True)
    
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Customer"



class CustomerPassword(models.Model):
    """(OtpVerification description)"""
    
    user = models.ForeignKey('Customer', on_delete=models.CASCADE,)
    password = models.CharField(blank = True, max_length = 100)
    password_open = models.CharField(blank = False, max_length = 100)
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)
    
    def save(self, *args, **kwargs):
        self.password = hashlib.md5(self.password_open.encode()).hexdigest()

        super(CustomerPassword, self).save(*args, **kwargs)

class CustomerOtp(models.Model):
    """(OtpVerification description)"""
    
    user = models.ForeignKey('Customer', on_delete=models.CASCADE,)
    code = models.CharField(blank = True, max_length = 100)
    valid = models.DateTimeField(blank = True, null = True  ) 
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)
    
    def save(self, *args, **kwargs):
        self.code = "".join([random.choice("1234567890") for i in range(6)])
        self.valid = (datetime.datetime.now() + datetime.timedelta(minutes = 5))
        super(CustomerOtp, self).save(*args, **kwargs)


class CustomerPasswordResetCode(models.Model):
    """
    Codes for users to recover their accounts
    """
    user = models.ForeignKey('Customer', on_delete=models.CASCADE,)
    reset_code = models.CharField(blank = True, max_length = 100)
    expiry_date = models.DateField()
    created_at = models.DateTimeField(null = True, blank = True, default = datetime.datetime.now)
    
    def set_expiry_date(self):
        return timezone.now()+timedelta(days = 1)
        
    def create_hash_code(self):
        return "".join([random.choice("1234567890") for i in range(6)])
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.expiry_date = self.set_expiry_date()
            self.reset_code = self.create_hash_code()
        super(CustomerPasswordResetCode, self).save(*args, **kwargs)
                

class CustomerToken(models.Model):
    """(Tokens reside here)"""
    user = models.ForeignKey('Customer', on_delete=models.CASCADE,)
    token  = models.CharField(blank = True, max_length = 100)
    created_at = models.DateTimeField(null=True, blank = True, default = datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.token = "".join([random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for i in range(32)])
        super(CustomerToken, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.token

    class Meta:
        verbose_name_plural = "Tokens"





