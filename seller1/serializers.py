from rest_framework import serializers
from seller1.models import Seller1,Ablumfiles, SellBusiness, RevenueModel,\
    SellAsset, SellEquity, RaiseLoan, SellStartup, SellApp, SellIpcode, SellFranchise, Supplier




class AblumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ablumfiles
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller1
        fields = '__all__'

class SellBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellBusiness
        fields = '__all__'

class SellAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellAsset
        fields = '__all__'


class SellEquitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SellEquity
        fields = '__all__'


class RaiseLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaiseLoan
        fields = '__all__'


class SellAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellApp
        fields = '__all__'

class SellIpcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellIpcode
        fields = '__all__'

class RevenueModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueModel
        fields = '__all__'

class SellStartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellStartup
        fields = '__all__'


class SellFranchiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellFranchise
        fields = '__all__'


class SellSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

serializer_list ={
    'Business': SellBusinessSerializer,
    'Asset': SellAssetSerializer,
    'Loan': RaiseLoanSerializer,
    'Equity': SellEquitySerializer,
    'Startup': SellStartupSerializer,
    'Ipcode': SellIpcodeSerializer,
    'Application': SellAppSerializer,
    'Franchise': SellFranchiseSerializer,
    'Supplier': SellSupplierSerializer,
}
