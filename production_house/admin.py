import hashlib
import random

from django.contrib import admin
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin

from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from production_house.models import *

from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage



        
class CompanyAdmin(SuperModelAdmin, SummernoteModelAdmin):
    model = Company
    list_display = ['pk', 'name', 'email', 'contact_name', 'contact_mobile', 'video_count', 'created_at']

 

admin.site.register(Company, CompanyAdmin)
