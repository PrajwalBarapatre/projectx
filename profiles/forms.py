from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.contrib.auth import authenticate, login
from .models import Profile, Feedback


class UserRegisterForm(forms.ModelForm):

    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        username = User.objects.get(email=email.lower()).username

        if email and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            # if not user.is_active:
            #     raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class ProfileForm(forms.ModelForm):
    contact_number = forms.IntegerField()
    country_code_primary = forms.CharField()
    class Meta:
        model = Profile
        exclude = ['user', 'created_at']

subscription_options = [
    ('1-month', '1-Month subscription ($10 USD/Mon)'),
    ('trial', 'Free Trial Period for 1 Month'),
    ('6-month', '6-Month subscription Save $10 ($50 USD/Mon)'),
    ('1-year', '1-Year subscription Save $30 ($90 USD/Mon)'),
]

class FeedbackForm(forms.ModelForm):
    # contact_number = forms.IntegerField()
    class Meta:
        model = Feedback
        exclude = ['created_at']

class SubscriptionForm(forms.Form):
    plans = forms.ChoiceField(choices=subscription_options)

