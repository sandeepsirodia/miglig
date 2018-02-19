from rest_framework import serializers

from production_house.models import *


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('pk', 'title', 'video', 'logo', 'rating', 'description', 'genre')


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('pk', 'title', 'audio', 'logo', 'rating', 'description', 'genre')

