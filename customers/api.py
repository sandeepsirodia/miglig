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
from .models import *

class CustomerViewSet(viewsets.ViewSet):

	@list_route(methods = ['post'])
	def login(self, request):
		"""
		---
		parameters:
				- name: mobile
				  description: mobile
				  required: false
				  type: string
				  paramType: form
				- name: email
				  description: email
				  required: false
				  type: string
				  paramType: form
				- name: password
				  description: password
				  required: true
				  type: string
				  paramType: form
				
		"""
		
		response = {}

		password = request.data["password"]
		hashed_password = hashlib.md5(password.encode()).hexdigest()

		if "email" in request.data:
			if CustomerPassword.objects.filter(password = hashed_password, user__email = request.data["email"], is_deleted = False).exists():
				customer = CustomerPassword.objects.get(password = hashed_password, user__email = request.data["email"], is_deleted = False).user
			else:
				response["result"] = 0
				response["errors"] = ["Password and user details doesn't matched"]
				return Response(response, status=status.HTTP_200_OK)

		elif "mobile" in request.data:	
			if CustomerPassword.objects.filter(password = hashed_password, user__mobile = request.data["mobile"], is_deleted = False).exists():
				customer = CustomerPassword.objects.get(password = hashed_password, user__mobile = request.data["mobile"], is_deleted = False).user	
			else:
				response["result"] = 0
				response["errors"] = ["Password and user details doesn't matched"]
				return Response(response, status=status.HTTP_200_OK)
		else:
			response["result"] = 0
			response["errors"] = ["submit complete form"]
			return Response(response, status=status.HTTP_200_OK)


		customer_token = CustomerToken(user = customer)
		customer_token.save()

		serializer = CustomerSerializer(customer, many = False).data

		response["result"] = 1
		response["token"] = customer_token.token
		response["data"] = serializer

		return Response(response, status=status.HTTP_200_OK)


	@list_route(methods = ['post'])
	def verify_customer(self, request):
		"""
		---
		parameters:
				- name: token
				  description: Transporter access token
				  required: true
				  type: string
				  paramType: form
				
		"""
		
		response = {}

		token = request.data["token"]

		if CustomerToken.objects.filter(token = token).exists():
			customer = CustomerToken.objects.get(token = token).user
			serializer = CustomerSerializer(customer, many = False).data
			response["result"] = 1
			response["token"] = token
			response["data"] = serializer
			return Response(response, status=status.HTTP_200_OK)
		else:
			response["result"] = 0
			response["errors"] = ["Invalid token"]
			return Response(response, status=status.HTTP_200_OK)	


	@list_route(methods = ['post'])
	def verify_mobile(self, request):
		"""
		---
		parameters:
				- name: mobile
				  description: mobile
				  required: true
				  type: string
				  paramType: form
				- name: email
				  description:email
				  required: true
				  type: string
				  paramType: form
				
		"""
		
		response = {}

		email = request.data["email"]
		mobile = request.data["mobile"]

		if not Customer.objects.filter(mobile = mobile, is_deleted = False).exists():
			# write finction to send sms
		else:
			response["result"] = 0
			response["errors"] = ["Mobile already exists"]
			return Response(response, status=status.HTTP_200_OK)
		return Response(response, status=status.HTTP_200_OK)


	@list_route(methods = ['post'])
	def register(self, request):
		"""
		---
		parameters:
				- name: name
				  description: name
				  required: true
				  type: string
				  paramType: form
				- name: email
				  description: email
				  required: true
				  type: string
				  paramType: form
				- name: mobile
				  description: mobile
				  required: true
				  type: string
				  paramType: form
				- name: password
				  description: password
				  required: true
				  type: string
				  paramType: form
				- name: re_password
				  description: password
				  required: true
				  type: string
				  paramType: form
				
		"""
		
		response = {}

		name = request.data["name"]
		email = request.data["email"]
		mobile = request.data["mobile"]
		password = request.data["password"]
		re_password = request.data["re_password"]

		if password == re_password:
			if not Customer.objects.filter(mobile = mobile, is_deleted = False).exists():
				if not Customer.objects.filter(email = email, is_deleted = False).exists():
					customer = Customer(name = name, email = email, mobile = mobile)
					customer.save()
					customer_password = CustomerPassword(user = customer)
					customer_password.password_open = password
					customer_password.save()

					customer_token = CustomerToken(user = customer)
					customer_token.save()

					serializer = CustomerSerializer(customer, many = False).data

					response["result"] = 1
					response["token"] = customer_token.token
					response["data"] = serializer

				else:
					response["result"] = 0
					response["errors"] = ["Email already exists"]
					return Response(response, status=status.HTTP_200_OK)
			else:
				response["result"] = 0
				response["errors"] = ["Mobile already exists"]
				return Response(response, status=status.HTTP_200_OK)
		else:
			response["result"] = 0
			response["errors"] = ["Password doesn't matched"]
			return Response(response, status=status.HTTP_200_OK)

