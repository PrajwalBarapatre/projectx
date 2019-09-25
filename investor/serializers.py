from rest_framework import serializers
from .models import Investor, IndividualInvestor, CompanyInvestor

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = '__all__'

class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualInvestor
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInvestor
        fields = '__all__'