from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer():
    class Meta:
        menu = Menu
        fields = '__all__'