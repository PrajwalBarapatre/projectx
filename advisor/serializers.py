from rest_framework import serializers
from .models import Advisor, BusinessAdvisor, StartupAdvisor

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessAdvisor
        fields = '__all__'

class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupAdvisor
        fields = '__all__'