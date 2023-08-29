from user.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = Promotion
         fields = '__all__'
class UserSerializer_1(serializers.ModelSerializer):
     class Meta:
         model = Collection
         fields = '__all__'