import hashlib
import random

from django.contrib import admin
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin

from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from customers.models import *

from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage



        
class CustomerAdmin(SuperModelAdmin, SummernoteModelAdmin):
    model = Customer
    list_display = ['pk', 'name', 'photo', 'email', 'mobile', 'old_mobile']

        
class CustomerTokenAdmin(SuperModelAdmin, SummernoteModelAdmin):
    model = CustomerToken
    list_display = ['pk', 'user', 'token']

        
class CustomerOtpAdmin(SuperModelAdmin, SummernoteModelAdmin):
    model = CustomerOtp
    list_display = ['pk', 'user', 'code', 'valid']


        
class CustomerPasswordAdmin(SuperModelAdmin, SummernoteModelAdmin):
    model = CustomerPassword
    list_display = ['pk', 'user', 'password_open']



admin.site.register(Customer)
