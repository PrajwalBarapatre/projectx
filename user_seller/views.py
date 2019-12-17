from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.conf import settings
from sorl.thumbnail import get_thumbnail
from django.core.files.uploadedfile import UploadedFile
import json
import requests
from django.urls import reverse
from rest_framework.response import Response
from metadata.views import business_sector, companies,codedata,yeardata
from seller1.models import Seller1,Ablumfiles, SellBusiness, RevenueModel,\
    SellAsset, SellEquity, RaiseLoan, SellStartup, SellApp, SellIpcode
from seller1.forms import \
    SellerForm, BusinessForm, SellerUpdateForm, BusinessUpdateForm, \
    RevenueModelForm, RevenueModelUpdateForm, AssetForm, AssetUpdateForm,\
    EquityForm, EquityUpdateForm, LoanForm, LoanUpdateForm,\
    StartupForm, StartupUpdateForm, AppForm, AppUpdateForm, IpcodeForm, IpcodeUpdateForm
from album.models import File
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from album.models import KAlbumForFile, File
import os, shutil, errno
import glob
from django.conf import settings
from seller1.serializers import AblumSerializer
from album.models import KAlbumForFile
from album.serializers import KAblumSerializer, FileSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Sell, Invest, Advise, Advisor, Investor

User = get_user_model()


model_list = {
    'Business': SellBusiness(),
    'Asset': SellAsset(),
    'Loan': RaiseLoan(),
    'Equity': SellEquity(),
    'Startup': SellEquity(),
    'Ipcode': SellIpcode(),
    'Application': SellApp()
}

def make_sell(seller_id):
    seller = Seller1.objects.get(business_id=seller_id)
    sell = Sell()
    sell.seller = seller
    sell.save()
    print(sell.type)
    return sell

def make_invest(investor_id):
    investor = Investor.objects.get(investor_id=investor_id)
    invest = Invest()
    invest.investor = investor
    invest.save()
    print(invest.type)
    return invest


def make_advise(advisor_id):
    advisor = Advisor.objects.get(advisor_id=advisor_id)
    advise = Advise()
    advise.advisor = advisor
    advise.save()
    print(advise.type)
    return advise



