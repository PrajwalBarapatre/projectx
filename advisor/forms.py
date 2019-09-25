from django import forms
from .models import Advisor, BusinessAdvisor, StartupAdvisor



Incubators = 'Incubators'
Accelerators = 'Accelerators'
Mentors = 'Mentors'
Institutions = 'Institutions'
Legal_Advisor = 'StartUp Legal Advisor'
SELLER_CHOICES = (
	(Incubators, 'Incubators'),
	(Accelerators, 'Accelerators'),
	(Mentors, 'Mentors'),
	(Institutions, 'Institutions'),
	(Legal_Advisor, 'StartUp Legal Advisor'),
)



class AdvisorForm(forms.ModelForm):


    about_seller = forms.ChoiceField(choices=SELLER_CHOICES, widget=forms.RadioSelect, initial=SELLER_CHOICES[0])

    class Meta:
        model = Advisor
        fields ='__all__'

class AdvisorUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])
    about_seller = forms.ChoiceField(choices=SELLER_CHOICES, widget=forms.RadioSelect, initial=SELLER_CHOICES[0])

    class Meta:
        model = Advisor
        fields ='__all__'

class BusinessForm(forms.ModelForm):


    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = BusinessAdvisor
        fields ='__all__'

class BusinessUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = BusinessAdvisor
        fields ='__all__'

class StartupForm(forms.ModelForm):


    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = StartupAdvisor
        fields ='__all__'

class StartupUpdateForm(forms.ModelForm):
    # asset_type = forms.ChoiceField(choices=ASSET_CHOICES, widget=forms.Select, initial=ASSET_CHOICES[0])

    class Meta:
        model = StartupAdvisor
        fields ='__all__'
