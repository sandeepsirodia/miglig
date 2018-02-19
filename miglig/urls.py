"""miglig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from customers.api import *
from production_house.api import *
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r'user', CustomerViewSet, "user")
router.register(r'content', ProductionHouseViewSet, "content")


urlpatterns = [
	url(r'^jet/', include('jet.urls', 'jet')),
	url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
	url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
	path('admin/', admin.site.urls),
    url(r'^docs/', views.schema_view),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls)),
]

