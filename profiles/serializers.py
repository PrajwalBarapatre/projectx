from rest_framework import serializers
from .models import User, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

