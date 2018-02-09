from rest_framework import serializers

from customers.models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk', 'name', 'photo', 'email', 'mobile')

