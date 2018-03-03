import hashlib

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
from .serializers import *

class ProductionHouseViewSet(viewsets.ViewSet):
	
	@list_route(methods = ['get'])
	def main_video(self, request):
			
		response = {}
		password = request.data["pk"]
		videos = Video.objects.filter(pk = id)

		serializer = VideoSerializer(videos, many = False).data

		response["result"] = 1
		response["data"] = serializer

		return Response(response, status=status.HTTP_200_OK)


	@list_route(methods = ['get'])
	def video(self, request):
			
		response = {}

		videos = Video.objects.all()

		serializer = VideoSerializer(videos, many = True).data

		response["result"] = 1
		response["data"] = serializer

		return Response(response, status=status.HTTP_200_OK)


	@list_route(methods = ['get'])
	def audio(self, request):
			
		response = {}

		audio = Audio.objects.all()

		serializer = AudioSerializer(audio, many = True).data

		response["result"] = 1
		response["data"] = serializer

		return Response(response, status=status.HTTP_200_OK)

