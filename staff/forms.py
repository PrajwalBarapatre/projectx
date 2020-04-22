from django import forms
from .models import Task

SELL = 'Sell'
ADVISE = 'Advise'
INVEST = 'Invest'
Listing_CHOICES = (
	(SELL, 'Sell'),
	# (ADVISE, 'Advise'),
	# (INVEST, 'Invest')
)

BUSINESS = 'Business'
BUSINESS_ADVISE = 'Business_Advisor'
ASSET = 'Asset'
EQUITY = 'Equity'
LOAN = 'Loan'
SUPPLIER = 'Supplier'
FRANCHISE = 'Franchise'
STARTUP = 'Startup'
STARTUP_ADVISE = 'Startup_Advisor'
IP_CODES = 'IP_Codes'
APP = 'Application'
INDIVIDUAL_INVEST = 'Individual'
COMPANY_INVEST = 'Company'
Lead_CHOICES = (
	(BUSINESS, 'Business'),
	(ASSET, 'Asset'),
	(EQUITY, 'Equity'),
    (LOAN, 'Loan'),
    (SUPPLIER, 'Supplier'),
    (FRANCHISE, 'Franchise'),
    (STARTUP, 'Startup'),
    (IP_CODES, 'IP_Codes'),
    (APP, 'Application'),
    # (BUSINESS_ADVISE, 'Business_Advisor'),
    # (STARTUP_ADVISE, 'Startup_Advisor'),
    # (INDIVIDUAL_INVEST, 'Individual_Investor'),
    # (COMPANY_INVEST, 'Company_Investor'),
)

class TaskForm(forms.ModelForm):

    listing_type = forms.ChoiceField(choices=Listing_CHOICES, widget=forms.RadioSelect, initial=Listing_CHOICES[0],
                                     required=True)
    lead_type = forms.ChoiceField(choices=Lead_CHOICES, widget=forms.RadioSelect, initial=Lead_CHOICES[0],
                                     required=True)
    client_email = forms.EmailField(required=True)
    # phone_number = forms.IntegerField()
    name = forms.CharField(required=True, max_length=255)
    class Meta:
        model = Task
        exclude = ['created_at', 'completed', 'task_enc',
                   'task_hash', 'sell', 'advise', 'invest', 'task_id', 'user', 'client', 'expires']