from django import forms
from .models import IndividualInvestor, Investor, CompanyInvestor


nbfc = 'NBFC'
Financier = 'Financier'
Equity = 'Private_Equity'
Vc = 'VC'
Investment_Bank = 'Investment_Bank'
Banks = 'Banks'
SELLER_CHOICES = (
	(nbfc, 'NBFC'),
	(Financier, 'Financier'),
    (Equity, 'Private Equity'),
	(Vc, 'VC'),
	(Investment_Bank, 'Investment Bank'),
	(Banks, 'Banks'),
)


class InvestorForm(forms.ModelForm):
    about_seller = forms.ChoiceField(choices=SELLER_CHOICES, widget=forms.RadioSelect, initial=SELLER_CHOICES[0])

    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = Investor
        fields ='__all__'

class InvestorUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])
    about_seller = forms.ChoiceField(choices=SELLER_CHOICES, widget=forms.RadioSelect, initial=SELLER_CHOICES[0])
    class Meta:
        model = Investor
        fields ='__all__'

class IndividualForm(forms.ModelForm):


    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = IndividualInvestor
        fields ='__all__'

class IndividualUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = IndividualInvestor
        fields ='__all__'

class CompanyForm(forms.ModelForm):


    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = CompanyInvestor
        fields ='__all__'

class CompanyUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = CompanyInvestor
        fields ='__all__'
