from django.contrib.auth.models import User

from django.contrib.auth import login as django_login
from django.utils.decorators import method_decorator

from django.contrib.auth import logout as auth_logout

from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission

from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import viewsets
	

class CustomerViewSet(viewsets.ViewSet):


	@list_route(methods = ['post'])
	def login(self, request):
		"""
		---
		parameters:
				- name: token
				  description: Transporter access token
				  required: true
				  type: string
				  paramType: form
				- name: pk
				  description: pk of transporter
				  required: true
				  type: string
				  paramType: form
				
		"""
		
		response = {}
		
		return Response(response, status=status.HTTP_200_OK)

