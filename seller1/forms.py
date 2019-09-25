from django import forms
from .models import Seller1, SellBusiness, RevenueModel, SellAsset,\
    SellEquity, RaiseLoan, SellStartup, SellApp, SellIpcode, SellFranchise, Supplier
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from metadata.views import business_sector, companies,codedata,yeardata

# category1 = ()
# sectors = business_sector()
# print(sectors)
# i=0
# for x in sectors:
#     r=x['sectors']
#     category1[i]=(r, x['sectors'])

OWNER = 'Owner'
BROKER = 'Broker'
SELLER_CHOICES = (
	(OWNER, 'Owner'),
	(BROKER, 'Broker')
)

Ip = 'Intellectual_Property'
Code = 'Software_Code'
Ip_CHOICES = (
	(Ip, 'Intellectual Property'),
	(Code, 'Software Code')
)

App = 'Mobile Application'
Web = 'Early Stage Website'
eWeb = 'Established Website'
Domain = 'Domain'
App_CHOICES = (
	(App, 'Mobile Application'),
	(Web, 'Early Stage Website'),
    (eWeb,'Established Website'),
    (Domain, 'Domain'),
)



# ASSET = 'Furniture and assets'
# BUSINESS = 'Land'
# ASSET = 'Building'
# BUSINESS = 'Land'
# ASSET = 'Furniture and assets'
# BUSINESS = 'Land'
# ASSET = 'Furniture and assets'

# ASSET_CHOICES = (
# 	(ASSET, 'Asset Type'),
# 	(BUSINESS, 'Business Seller')
# )

BF='Business_Franchise'
PF='Product_Franchise'
MF='Manufacturing_Franchise'
FRANCHISE_CHOICES = (
	(BF, 'Business Franchise'),
	(PF, 'Product Franchise'),
    (MF, 'Manufacturing Franchise')
)

BF='MANUFACTURERS AND VENDORS'
PF='WHOLESALERS AND DISTRIBUTORS'
MF='INDEPENDENT AND TRADE SHOW REPS'
DF='IMPORTERS'

SUPPLIER_CHOICES = (
	(BF, 'MANUFACTURERS AND VENDORS'),
	(PF, 'WHOLESALERS AND DISTRIBUTORS'),
    (MF, 'INDEPENDENT AND TRADE SHOW REPS'),
    (DF, 'IMPORTERS'),
)

OWNER = 'Owner'
BROKER = 'Broker or Third Party'
STARTUP_CHOICES = (
	(OWNER, 'Owner'),
	(BROKER, 'Broker or Third Party')
)


class SellerForm(forms.ModelForm):

    phone_number_primary = forms.IntegerField()
    about_seller = forms.ChoiceField(choices=SELLER_CHOICES, widget=forms.RadioSelect, initial=SELLER_CHOICES[0], required=False)

    class Meta:
        model = Seller1
        exclude = ['completed', 'user']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = SellBusiness
        fields ='__all__'

class RevenueModelForm(forms.ModelForm):
    class Meta:
        model = RevenueModel
        fields ='__all__'



class SellerUpdateForm(forms.ModelForm):
    phone_number_primary = forms.IntegerField()
    # category1 = forms.ChoiceField(choices=category1)
    about_seller = forms.ChoiceField(choices=SELLER_CHOICES, widget=forms.RadioSelect, initial=SELLER_CHOICES[0], required=False)

    class Meta:
        model = Seller1
        exclude = ['completed', 'user']

class BusinessUpdateForm(forms.ModelForm):
    class Meta:
        model = SellBusiness
        fields ='__all__'

class RevenueModelUpdateForm(forms.ModelForm):
    class Meta:
        model = RevenueModel
        fields ='__all__'

class AssetForm(forms.ModelForm):


    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = SellAsset
        fields ='__all__'

class AssetUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = SellAsset
        fields ='__all__'

class EquityForm(forms.ModelForm):


    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = SellEquity
        fields ='__all__'

class EquityUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = SellEquity
        fields ='__all__'


class LoanForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = RaiseLoan
        fields ='__all__'

class LoanUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = RaiseLoan
        fields ='__all__'


class StartupForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = SellStartup
        fields ='__all__'

class StartupUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = SellStartup
        fields ='__all__'


class AppForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])
    startup_type = forms.ChoiceField(choices=App_CHOICES, widget=forms.RadioSelect, initial=App_CHOICES[0])
    date_established = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


    class Meta:
        model = SellApp
        fields ='__all__'

class AppUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])
    startup_type = forms.ChoiceField(choices=App_CHOICES, widget=forms.RadioSelect, initial=App_CHOICES[0])
    date_established = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = SellApp
        fields ='__all__'

class IpcodeForm(forms.ModelForm):
    startup_type = forms.ChoiceField(choices=Ip_CHOICES, widget=forms.RadioSelect, initial=Ip_CHOICES[0])

    class Meta:
        model = SellIpcode
        fields ='__all__'

class IpcodeUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])
    startup_type = forms.ChoiceField(choices=Ip_CHOICES, widget=forms.RadioSelect, initial=Ip_CHOICES[0])

    class Meta:
        model = SellIpcode
        fields ='__all__'


class SellFranchiseForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])
    franchise_type = forms.ChoiceField(choices=FRANCHISE_CHOICES, widget=forms.RadioSelect, initial=FRANCHISE_CHOICES[0])
    class Meta:
        model = SellFranchise
        fields ='__all__'

class FranchiseUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])
    franchise_type = forms.ChoiceField(choices=FRANCHISE_CHOICES, widget=forms.RadioSelect, initial=FRANCHISE_CHOICES[0])
    class Meta:
        model = SellFranchise
        fields ='__all__'


class SupplierForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])
    supplier_type = forms.ChoiceField(choices=SUPPLIER_CHOICES, widget=forms.RadioSelect, initial=SUPPLIER_CHOICES[0])
    class Meta:
        model = Supplier
        fields ='__all__'


class SupplierUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])
    supplier_type = forms.ChoiceField(choices=SUPPLIER_CHOICES, widget=forms.RadioSelect, initial=SUPPLIER_CHOICES[0])
    class Meta:
        model = Supplier
        fields ='__all__'
