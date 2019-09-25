from .models import File
from django import forms

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
        widgets = {

            'file': forms.ClearableFileInput(attrs={'multiple': True})
        }

