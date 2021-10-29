
from rest_framework import serializers
from ..models import CustomerUser


class CustomerUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['username', 'password']

