from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
import random
import pdf2image
from datetime import datetime
from profiles.models import Search_log, View_log
# from PIL import Image
from django.conf import settings
from django.core.paginator import Paginator
from profiles.models import Profile
from itertools import chain
from sorl.thumbnail import get_thumbnail
from django.core.files.uploadedfile import UploadedFile
import json
from user_seller.views import make_invest, make_sell, make_advise
from investor.serializers import IndividualSerializer, CompanySerializer, InvestorSerializer
import requests
from django.urls import reverse
from advisor.models import StartupAdvisor, BusinessAdvisor
from rest_framework.response import Response
from metadata.views import business_sector, companies,codedata,yeardata
from seller1.models import Seller1,Ablumfiles, SellBusiness, RevenueModel,\
    SellAsset, SellEquity, RaiseLoan, SellStartup, SellApp, SellIpcode, SellFranchise, Supplier
from seller1.forms import \
    SellerForm, BusinessForm, SellerUpdateForm, BusinessUpdateForm, \
    RevenueModelForm, RevenueModelUpdateForm, AssetForm, AssetUpdateForm,\
    EquityForm, EquityUpdateForm, LoanForm, LoanUpdateForm,\
    StartupForm, StartupUpdateForm, AppForm, AppUpdateForm, IpcodeForm, IpcodeUpdateForm,\
    SellFranchiseForm, FranchiseUpdateForm, SupplierForm, SupplierUpdateForm
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
from user_seller.models import Sell, Advise, Invest
from seller1.serializers import serializer_list, RevenueModelSerializer, SellerSerializer
from investor.views import inv_model_list, inv_serializer_list
from advisor.views import adv_model_list, adv_serializer_list
from investor.models import IndividualInvestor, CompanyInvestor
from advisor.serializers import AdvisorSerializer
from advisor.models import Advisor
from investor.models import Investor
from io import BytesIO, StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from profiles.models import Notification
from profiles.models import Profile
from user_seller.models import Sell, Advise, Invest
from staff.models import Task
from seller1.sms import email_adder, email_checker, phone_adder, phone_checker

base_model_list={
    'Seller':Seller1,
    'Advisor':Advisor,
    'Investor':Investor
}



model_list = {
    'Business': SellBusiness,
    'Asset': SellAsset,
    'Loan': RaiseLoan,
    'Equity': SellEquity,
    'Startup': SellStartup,
    'Ipcode': SellIpcode,
    'Application': SellApp,
    'Franchise': SellFranchise,
    'Supplier': Supplier,
}



@login_required(login_url='profiles:index')
def Business_task(request, task_hash):
    task = None
    try:
        print('inside business_task')
        task = get_object_or_404(Task, task_hash=task_hash)
        print(task.client)
        if task.expires.time() > datetime.now().time() and task.expires.date() >= datetime.now().date():
            pass
        else:
            return redirect('staff:staff-home')
    except:
        return redirect('profiles:index')

    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        'country_code_primary': 'country_code_primary',
        'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller':'about_seller',
        'address_line': 'address_line',
    }

    revenue_fields = {
        'rev_year': 'rev_year',
        'year_16': 'year_16',
        'year_17': 'year_17',
        'year_15': 'year_15',
        'year_14': 'year_14',
        'year_13': 'year_13',
        'no_emp': 'no_emp',
        'cp_emp': 'cp_emp',
    }

    text_fields = {
        'adress': 'adress',

    }
    a = True
    if request.user.is_staff:
        if request.method == 'POST':
            seller = SellerForm(request.POST)
            business = BusinessForm(request.POST)
            revenue = RevenueModelForm(request.POST)
            print('submit is done')
            #      print("posting")
            #       print(seller.is_valid())
            if seller.is_valid() and business.is_valid() and revenue.is_valid():
                print('everythin is valid')
                seller_1 = seller.save(commit=False)
                #       print(seller)
                seller_1.save()
                seller_1.trial = True
                seller_1.type = 'Business'
                print(seller_1.album_id)
                if seller_1.album_id is None:
                    # fs = FileSystemStorage()
                    print('no file selected')
                    category = seller_1.category1
                    bcard_pdf_name = os.path.join(settings.MEDIA_ROOT, 'category/default_' + str(category) + '.png')
                    file = None
                    try:
                        file = File.objects.get(name='category/default_' + str(category) + '.png')
                    except:
                        file = File()
                        file.file.name = 'category/default_' + str(category) + '.png'
                        file.save()
                    album = KAlbumForFile()
                    album.save()
                    album.files.add(file)
                    # album.seller=seller_1
                    album.save()
                    seller_1.album_id = album.album_id
                    seller_1.save()
                seller_1.save()
                id = seller_1.business_id
                print(id)
                # m = imager(id)
                print('seller is done')
                business_1 = business.save(commit=False)
                # business_1=business.save()
                business_1.seller = seller_1
                business_1.type = 'Business'
                business_1.save()
                print('business is also done')
                revenue_1 = revenue.save(commit=False)
                revenue_1.seller = seller_1
                revenue_1.save()
                print('revenue is also done')
                sell = make_sell(seller_1.business_id)
                curr_user = task.client
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                task.completed = True
                task.sell = sell
                task.save()
                if not email_checker(curr_user.id, seller_1.email_adress):
                    email_adder(curr_user, seller_1.email_adress)
                phone_number = '' + seller_1.country_code_primary + seller_1.phone_number_primary
                print(phone_number)
                if not phone_checker(curr_user.id, phone_number):
                    phone_adder(curr_user, seller_1.phone_number_primary, seller_1.country_code_primary)
                return redirect('seller1:seller-all-detail', business_id=seller_1.business_id)

            else:
                print(seller.errors)
                print(business.errors)
                print(revenue.errors)

        sectors = business_sector()
        types_companies = companies()
        code_data = codedata()
        business_form = SellerForm()
        sell_bsn = BusinessForm()
        rev_form = RevenueModelForm()
        type_fields = {
            'about': 'about',
            'asking_price': 'asking_price',
            'year_established': 'year_established',
            'reason_selling': 'reason_selling',
            'website': 'website'
        }
        context = {
            'sectors': sectors,
            'types_companies': types_companies,
            'model_fields': model_fields,
            'code_data': code_data,
            'client': task.client,
            'business_form': business_form,
            'year_data': yeardata,
            'text_fields': text_fields,
            'sell_bsn': sell_bsn,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form,
            

        }
        return render(request, 'seller1/sellbusiness.html', context)

    else:
        return redirect('profiles:index')



@login_required(login_url='profiles:index')
def Asset_task(request, task_hash):
    task = None
    try:
        print('inside business_task')
        task = get_object_or_404(Task, task_hash=task_hash)
        print(task.client)
        if task.expires.time() > datetime.now().time() and task.expires.date() >= datetime.now().date():
            pass
        else:
            return redirect('staff:staff-home')
    except:
        return redirect('profiles:index')
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        'country_code_primary': 'country_code_primary',
        'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller':'about_seller',
        'address_line': 'address_line',
    }

    revenue_fields = {
        'rev_year': 'rev_year',
        'year_16': 'year_16',
        'year_17': 'year_17',
        'year_15': 'year_15',
        'year_14': 'year_14',
        'year_13': 'year_13',
        'no_emp': 'no_emp',
        'cp_emp': 'cp_emp',
    }

    text_fields = {
        'adress': 'adress',

    }
    a = True
    if request.user.is_staff:
        if request.method == 'POST':
            seller = SellerForm(request.POST)
            business = AssetForm(request.POST)
            revenue = RevenueModelForm(request.POST)
            print('submit is done')
            #      print("posting")
            #       print(seller.is_valid())
            if seller.is_valid() and business.is_valid() and revenue.is_valid():
                print('everythin is valid')
                seller_1 = seller.save(commit=False)
                #       print(seller)
                seller_1.save()
                seller_1.trial = True
                seller_1.type = 'Asset'
                if seller_1.album_id is None:
                    # fs = FileSystemStorage()
                    print('no file selected')
                    category = seller_1.category1
                    bcard_pdf_name = os.path.join(settings.MEDIA_ROOT, 'category/default_' + str(category) + '.png')
                    file=None
                    try:
                        file = File.objects.get(name = 'category/default_' + str(category) + '.png')
                    except:
                        file = File()
                        file.file.name = 'category/default_' + str(category) + '.png'
                        file.save()
                    album = KAlbumForFile()
                    album.save()
                    album.files.add(file)
                    # album.seller=seller_1
                    album.save()
                    seller_1.album_id = album.album_id
                    seller_1.save()
                seller_1.save()
                id = seller_1.business_id
                print(id)
                # m = imager(id)
                print('seller is done')
                business_1 = business.save(commit=False)
                # business_1=business.save()
                business_1.seller = seller_1
                business_1.type = 'Asset'
                business_1.save()
                print('business is also done')
                revenue_1 = revenue.save(commit=False)
                revenue_1.seller = seller_1
                revenue_1.save()
                print('revenue is also done')
                sell = make_sell(seller_1.business_id)
                curr_user = task.client
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                task.completed = True
                task.sell = sell
                task.save()
                if not email_checker(curr_user.id, seller_1.email_adress):
                    email_adder(curr_user, seller_1.email_adress)
                phone_number = '' + seller_1.country_code_primary + seller_1.phone_number_primary
                print(phone_number)
                if not phone_checker(curr_user.id, phone_number):
                    phone_adder(curr_user, seller_1.phone_number_primary, seller_1.country_code_primary)
                return redirect('seller1:seller-all-detail', business_id=seller_1.business_id)

            else:
                print(seller.errors)
                print(business.errors)
                print(revenue.errors)

        sectors = business_sector()
        types_companies = companies()
        code_data = codedata()
        business_form = SellerForm()
        sell_asset = AssetForm()
        rev_form = RevenueModelForm()
        type_fields = {
        'asset_type' : 'asset_type',
        'about_asset' : 'about_asset',
        'asking_price' : 'asking_price',
        'purchase_price' : 'purchase_price',
        'purchase_year' : 'purchase_year',
        'reason_selling' : 'reason_selling',
        'website':'website'
        }
        context = {
            'sectors': sectors,
            'types_companies': types_companies,
            'model_fields': model_fields,
            'code_data': code_data,
            'client': task.client,
            'business_form': business_form,
            'year_data': yeardata,
            'text_fields': text_fields,
            'sell_asset': sell_asset,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form

        }
        return render(request, 'seller1/sellasset.html', context)

    else:
        return redirect('profiles:index')


@login_required(login_url='profiles:index')
def Equity_task(request, task_hash):
    task = None
    try:
        print('inside business_task')
        task = get_object_or_404(Task, task_hash=task_hash)
        print(task.client)
        if task.expires.time() > datetime.now().time() and task.expires.date() >= datetime.now().date():
            pass
        else:
            return redirect('staff:staff-home')
    except:
        return redirect('profiles:index')
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        'country_code_primary': 'country_code_primary',
        'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller':'about_seller',
        'address_line': 'address_line',
    }

    revenue_fields = {
        'rev_year': 'rev_year',
        'year_16': 'year_16',
        'year_17': 'year_17',
        'year_15': 'year_15',
        'year_14': 'year_14',
        'year_13': 'year_13',
        'no_emp': 'no_emp',
        'cp_emp': 'cp_emp',
    }

    text_fields = {
        'adress': 'adress',

    }
    a = True
    if request.user.is_staff:
        if request.method == 'POST':
            seller = SellerForm(request.POST)
            business = EquityForm(request.POST)
            revenue = RevenueModelForm(request.POST)
            print('submit is done')
            #      print("posting")
            #       print(seller.is_valid())
            if seller.is_valid() and business.is_valid() and revenue.is_valid():
                print('everythin is valid')
                seller_1 = seller.save(commit=False)
                #       print(seller)
                seller_1.save()
                seller_1.trial = True
                seller_1.type = 'Equity'
                if seller_1.album_id is None:
                    # fs = FileSystemStorage()
                    print('no file selected')
                    category = seller_1.category1
                    bcard_pdf_name = os.path.join(settings.MEDIA_ROOT, 'category/default_' + str(category) + '.png')
                    file=None
                    try:
                        file = File.objects.get(name = 'category/default_' + str(category) + '.png')
                    except:
                        file = File()
                        file.file.name = 'category/default_' + str(category) + '.png'
                        file.save()
                    album = KAlbumForFile()
                    album.save()
                    album.files.add(file)
                    # album.seller=seller_1
                    album.save()
                    seller_1.album_id = album.album_id
                    seller_1.save()
                seller_1.save()
                id = seller_1.business_id
                print(id)
                # m = imager(id)
                print('seller is done')
                business_1 = business.save(commit=False)
                # business_1=business.save()
                business_1.seller = seller_1
                business_1.type = 'Equity'
                business_1.save()
                print('business is also done')
                revenue_1 = revenue.save(commit=False)
                revenue_1.seller = seller_1
                revenue_1.save()
                print('revenue is also done')
                sell = make_sell(seller_1.business_id)
                curr_user = task.client
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                task.completed = True
                task.sell = sell
                task.save()
                if not email_checker(curr_user.id, seller_1.email_adress):
                    email_adder(curr_user, seller_1.email_adress)
                phone_number = '' + seller_1.country_code_primary + seller_1.phone_number_primary
                print(phone_number)
                if not phone_checker(curr_user.id, phone_number):
                    phone_adder(curr_user, seller_1.phone_number_primary, seller_1.country_code_primary)
                return redirect('seller1:seller-all-detail', business_id=seller_1.business_id)

            else:
                print(seller.errors)

        sectors = business_sector()
        types_companies = companies()
        code_data = codedata()
        business_form = SellerForm()
        sell_equity = EquityForm()
        rev_form = RevenueModelForm()
        type_fields = {
            'about_business': 'about_business',
            'stake': 'stake',
            'asking_price': 'asking_price',
            'year': 'year',
            'reason': 'reason',
            'website': 'website'
        }
        context = {
            'sectors': sectors,
            'types_companies': types_companies,
            'model_fields': model_fields,
            'code_data': code_data,
            'client': task.client,
            'business_form': business_form,
            'year_data': yeardata,
            'text_fields': text_fields,
            'sell_equity': sell_equity,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form

        }
        return render(request, 'seller1/sellequity.html', context)

    else:
        return redirect('profiles:index')



@login_required(login_url='profiles:index')
def Loan_task(request, task_hash):
    task = None
    try:
        print('inside business_task')
        task = get_object_or_404(Task, task_hash=task_hash)
        print(task.client)
        if task.expires.time() > datetime.now().time() and task.expires.date() >= datetime.now().date():
            pass
        else:
            return redirect('staff:staff-home')
    except:
        return redirect('profiles:index')
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        'country_code_primary': 'country_code_primary',
        'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller':'about_seller',
        'address_line': 'address_line',
    }

    revenue_fields = {
        'rev_year': 'rev_year',
        'year_16': 'year_16',
        'year_17': 'year_17',
        'year_15': 'year_15',
        'year_14': 'year_14',
        'year_13': 'year_13',
        'no_emp': 'no_emp',
        'cp_emp': 'cp_emp',
    }

    text_fields = {
        'adress': 'adress',

    }
    a = True
    if request.user.is_staff:
        if request.method == 'POST':
            seller = SellerForm(request.POST)
            business = LoanForm(request.POST)
            revenue = RevenueModelForm(request.POST)
            print('submit is done')
            #      print("posting")
            #       print(seller.is_valid())
            if seller.is_valid() and business.is_valid() and revenue.is_valid():
                print('everythin is valid')
                seller_1 = seller.save(commit=False)
                #       print(seller)
                seller_1.save()
                seller_1.trial = True
                seller_1.type = 'Loan'
                if seller_1.album_id is None:
                    # fs = FileSystemStorage()
                    print('no file selected')
                    category = seller_1.category1
                    bcard_pdf_name = os.path.join(settings.MEDIA_ROOT, 'category/default_' + str(category) + '.png')
                    file=None
                    try:
                        file = File.objects.get(name = 'category/default_' + str(category) + '.png')
                    except:
                        file = File()
                        file.file.name = 'category/default_' + str(category) + '.png'
                        file.save()
                    album = KAlbumForFile()
                    album.save()
                    album.files.add(file)
                    # album.seller=seller_1
                    album.save()
                    seller_1.album_id = album.album_id
                    seller_1.save()
                seller_1.save()
                id = seller_1.business_id
                print(id)
                # m = imager(id)
                print('seller is done')
                business_1 = business.save(commit=False)
                # business_1=business.save()
                business_1.seller = seller_1
                business_1.type = 'Loan'
                business_1.save()
                print('business is also done')
                revenue_1 = revenue.save(commit=False)
                revenue_1.seller = seller_1
                revenue_1.save()
                print('revenue is also done')
                sell = make_sell(seller_1.business_id)
                curr_user = task.client
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                task.completed = True
                task.sell = sell
                task.save()
                if not email_checker(curr_user.id, seller_1.email_adress):
                    email_adder(curr_user, seller_1.email_adress)
                phone_number = '' + seller_1.country_code_primary + seller_1.phone_number_primary
                print(phone_number)
                if not phone_checker(curr_user.id, phone_number):
                    phone_adder(curr_user, seller_1.phone_number_primary, seller_1.country_code_primary)
                return redirect('seller1:seller-all-detail', business_id=seller_1.business_id)

            else:
                print(seller.errors)

        sectors = business_sector()
        types_companies = companies()
        code_data = codedata()
        business_form = SellerForm()
        sell_loan = LoanForm()
        rev_form = RevenueModelForm()
        type_fields = {
            'about_business': 'about_business',
            'loan_amount': 'loan_amount',
            'sought_interest': 'sought_interest',
            'year_established': 'year_established',
            'reason_loan': 'reason_loan',
            'website': 'website'
        }
        context = {
            'sectors': sectors,
            'types_companies': types_companies,
            'model_fields': model_fields,
            'code_data': code_data,
            'client': task.client,
            'business_form': business_form,
            'year_data': yeardata,
            'text_fields': text_fields,
            'sell_loan': sell_loan,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form

        }
        return render(request, 'seller1/selloan.html', context)

    else:
        return redirect('profiles:index')


@login_required(login_url='profiles:index')
def Startup_task(request, task_hash):
    task = None
    try:
        print('inside business_task')
        task = get_object_or_404(Task, task_hash=task_hash)
        print(task.client)
        if task.expires.time() > datetime.now().time() and task.expires.date() >= datetime.now().date():
            pass
        else:
            return redirect('staff:staff-home')
    except:
        return redirect('profiles:index')
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        'country_code_primary': 'country_code_primary',
        'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller':'about_seller',
        'address_line': 'address_line',
    }

    revenue_fields = {
        'rev_year': 'rev_year',
        'year_16': 'year_16',
        'year_17': 'year_17',
        'year_15': 'year_15',
        'year_14': 'year_14',
        'year_13': 'year_13',
        'no_emp': 'no_emp',
        'cp_emp': 'cp_emp',
    }

    text_fields = {
        'adress': 'adress',

    }
    a = True
    if request.user.is_staff:
        if request.method == 'POST':
            seller = SellerForm(request.POST)
            business = StartupForm(request.POST)
            revenue = RevenueModelForm(request.POST)
            print('submit is done')
            #      print("posting")
            #       print(seller.is_valid())
            if seller.is_valid() and business.is_valid() and revenue.is_valid():
                print('everythin is valid')
                seller_1 = seller.save(commit=False)
                #       print(seller)
                seller_1.save()
                seller_1.trial = True
                seller_1.type = 'Startup'
                if seller_1.album_id is None:
                    # fs = FileSystemStorage()
                    print('no file selected')
                    category = seller_1.category1
                    bcard_pdf_name = os.path.join(settings.MEDIA_ROOT, 'category/default_' + str(category) + '.png')
                    file=None
                    try:
                        file = File.objects.get(name = 'category/default_' + str(category) + '.png')
                    except:
                        file = File()
                        file.file.name = 'category/default_' + str(category) + '.png'
                        file.save()
                    album = KAlbumForFile()
                    album.save()
                    album.files.add(file)
                    # album.seller=seller_1
                    album.save()
                    seller_1.album_id = album.album_id
                    seller_1.save()
                seller_1.save()
                id = seller_1.business_id
                print(id)
                # m = imager(id)
                print('seller is done')
                business_1 = business.save(commit=False)
                # business_1=business.save()
                business_1.seller = seller_1
                business_1.type = 'Startup'
                business_1.save()
                print('business is also done')
                revenue_1 = revenue.save(commit=False)
                revenue_1.seller = seller_1
                revenue_1.save()
                print('revenue is also done')
                sell = make_sell(seller_1.business_id)
                curr_user = task.client
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                task.completed = True
                task.sell = sell
                task.save()
                if not email_checker(curr_user.id, seller_1.email_adress):
                    email_adder(curr_user, seller_1.email_adress)
                phone_number = '' + seller_1.country_code_primary + seller_1.phone_number_primary
                print(phone_number)
                if not phone_checker(curr_user.id, phone_number):
                    phone_adder(curr_user, seller_1.phone_number_primary, seller_1.country_code_primary)
                return redirect('seller1:seller-all-detail', business_id=seller_1.business_id)

            else:
                print(seller.errors)

        sectors = business_sector()
        types_companies = companies()
        code_data = codedata()
        business_form = SellerForm()
        sell_startup = StartupForm()
        rev_form = RevenueModelForm()
        type_fields = {
            'about': 'about',
            'sought_equity': 'sought_equity',
            'asking_price': 'asking_price',
            'revenue_growth': 'revenue_growth',
            'year_established': 'year_established',
            'reason_selling': 'reason_selling',
            'website': 'website'
        }
        context = {
            'sectors': sectors,
            'types_companies': types_companies,
            'model_fields': model_fields,
            'code_data': code_data,
            'client': task.client,
            'business_form': business_form,
            'year_data': yeardata,
            'text_fields': text_fields,
            'sell_startup': sell_startup,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form

        }
        return render(request, 'seller1/sellstartup.html', context)

    else:
        return redirect('profiles:index')



@login_required(login_url='profiles:index')
def App_task(request, task_hash):
    task = None
    try:
        print('inside business_task')
        task = get_object_or_404(Task, task_hash=task_hash)
        print(task.client)
        if task.expires.time() > datetime.now().time() and task.expires.date() >= datetime.now().date():
            pass
        else:
            return redirect('staff:staff-home')
    except:
        return redirect('profiles:index')
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        'country_code_primary': 'country_code_primary',
        # 'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller':'about_seller',
        'address_line': 'address_line',
    }

    revenue_fields = {
        'rev_year': 'rev_year',
        'year_16': 'year_16',
        'year_17': 'year_17',
        'year_15': 'year_15',
        'year_14': 'year_14',
        'year_13': 'year_13',
        'no_emp': 'no_emp',
        'cp_emp': 'cp_emp',
    }

    text_fields = {
        'adress': 'adress',

    }
    a = True
    if request.user.is_staff:
        if request.method == 'POST':
            seller = SellerForm(request.POST)
            business = AppForm(request.POST)
            # revenue = RevenueModelForm(request.POST)
            print('submit is done')
            #      print("posting")
            #       print(seller.is_valid())
            if seller.is_valid() and business.is_valid():
                print('everythin is valid')
                seller_1 = seller.save(commit=False)
                #       print(seller)
                seller_1.save()
                seller_1.trial = True
                seller_1.type = 'Application'
                if seller_1.album_id is None:
                    # fs = FileSystemStorage()
                    print('no file selected')
                    category = seller_1.category1
                    bcard_pdf_name = os.path.join(settings.MEDIA_ROOT, 'category/default_' + str(category) + '.png')
                    file=None
                    try:
                        file = File.objects.get(name = 'category/default_' + str(category) + '.png')
                    except:
                        file = File()
                        file.file.name = 'category/default_' + str(category) + '.png'
                        file.save()
                    album = KAlbumForFile()
                    album.save()
                    album.files.add(file)
                    # album.seller=seller_1
                    album.save()
                    seller_1.album_id = album.album_id
                    seller_1.save()
                seller_1.save()
                id = seller_1.business_id
                print(id)
                # m = imager(id)
                print('seller is done')
                business_1 = business.save(commit=False)
                # business_1=business.save()
                business_1.seller = seller_1
                business_1.type = 'Application'
                business_1.save()
                print('business is also done')
                sell = make_sell(seller_1.business_id)
                curr_user = task.client
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                task.completed = True
                task.sell = sell
                task.save()
                if not email_checker(curr_user.id, seller_1.email_adress):
                    email_adder(curr_user, seller_1.email_adress)
                phone_number = '' + seller_1.country_code_primary + seller_1.phone_number_primary
                print(phone_number)
                if not phone_checker(curr_user.id, phone_number):
                    phone_adder(curr_user, seller_1.phone_number_primary, seller_1.country_code_primary)
                # revenue_1 = revenue.save(commit=False)
                # revenue_1.seller = seller_1
                # revenue_1.save()
                # print('revenue is also done')
                return redirect('seller1:seller-all-detail', business_id=seller_1.business_id)

            else:
                print(seller.errors)

        sectors = business_sector()
        types_companies = companies()
        code_data = codedata()
        business_form = SellerForm()
        sell_app = AppForm()
        rev_form = RevenueModelForm()
        type_fields = {
            'about': 'about',
            'email_app': 'email_app',
            'asking_price': 'asking_price',
            'average_monthly_revenue': 'average_monthly_revenue',
            'average_monthly_expense': 'average_monthly_expense',
            'date_established': 'date_established',
            'average_monthly_downloads': 'average_monthly_downloads',
            'website': 'website'
        }
        context = {
            'sectors': sectors,
            'types_companies': types_companies,
            'model_fields': model_fields,
            'code_data': code_data,
            'client': task.client,
            'business_form': business_form,
            'year_data': yeardata,
            'text_fields': text_fields,
            'sell_app': sell_app,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form

        }
        return render(request, 'seller1/sellapp.html', context)

    else:
        return redirect('profiles:index')



@login_required(login_url='profiles:index')
def Ipcode_task(request, task_hash):
    task = None
    try:
        print('inside business_task')
        task = get_object_or_404(Task, task_hash=task_hash)
        print(task.client)
        if task.expires.time() > datetime.now().time() and task.expires.date() >= datetime.now().date():
            pass
        else:
            return redirect('staff:staff-home')
    except:
        return redirect('profiles:index')
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        'country_code_primary': 'country_code_primary',
        # 'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller':'about_seller',
        'address_line': 'address_line',
    }

    revenue_fields = {
        'rev_year': 'rev_year',
        'year_16': 'year_16',
        'year_17': 'year_17',
        'year_15': 'year_15',
        'year_14': 'year_14',
        'year_13': 'year_13',
        'no_emp': 'no_emp',
        'cp_emp': 'cp_emp',
    }

    text_fields = {
        'adress': 'adress',

    }
    a = True
    if request.user.is_staff:
        if request.method == 'POST':
            seller = SellerForm(request.POST)
            business = IpcodeForm(request.POST)
            # revenue = RevenueModelForm(request.POST)
            print('submit is done')
            #      print("posting")
            #       print(seller.is_valid())
            if seller.is_valid() and business.is_valid():
                print('everythin is valid')
                seller_1 = seller.save(commit=False)
                #       print(seller)
                seller_1.save()
                seller_1.trial = True
                seller_1.type = 'Ipcode'
                if seller_1.album_id is None:
                    # fs = FileSystemStorage()
                    print('no file selected')
                    category = seller_1.category1
                    bcard_pdf_name = os.path.join(settings.MEDIA_ROOT, 'category/default_' + str(category) + '.png')
                    file=None
                    try:
                        file = File.objects.get(name = 'category/default_' + str(category) + '.png')
                    except:
                        file = File()
                        file.file.name = 'category/default_' + str(category) + '.png'
                        file.save()
                    album = KAlbumForFile()
                    album.save()
                    album.files.add(file)
                    # album.seller=seller_1
                    album.save()
                    seller_1.album_id = album.album_id
                    seller_1.save()
                seller_1.save()
                id = seller_1.business_id
                print(id)
                # m = imager(id)
                print('seller is done')
                business_1 = business.save(commit=False)
                # business_1=business.save()
                business_1.seller = seller_1
                business_1.type = 'Ipcode'
                business_1.save()
                print('business is also done')
                sell = make_sell(seller_1.business_id)
                curr_user = task.client
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                task.completed = True
                task.sell = sell
                task.save()
                if not email_checker(curr_user.id, seller_1.email_adress):
                    email_adder(curr_user, seller_1.email_adress)
                phone_number = '' + seller_1.country_code_primary + seller_1.phone_number_primary
                print(phone_number)
                if not phone_checker(curr_user.id, phone_number):
                    phone_adder(curr_user, seller_1.phone_number_primary, seller_1.country_code_primary)
                # revenue_1 = revenue.save(commit=False)
                # revenue_1.seller = seller_1
                # revenue_1.save()
                # print('revenue is also done')
                return redirect('seller1:seller-all-detail', business_id=seller_1.business_id)

            else:
                print(seller.errors)
                print(business.errors)

        sectors = business_sector()
        types_companies = companies()
        code_data = codedata()
        business_form = SellerForm()
        sell_ipcode = IpcodeForm()
        rev_form = RevenueModelForm()
        type_fields = {
            'about': 'about',
            'asking_price': 'asking_price',
            'research_title': 'research_title',
            'website': 'website'
        }
        context = {
            'sectors': sectors,
            'types_companies': types_companies,
            'model_fields': model_fields,
            'code_data': code_data,
            'client': task.client,
            'business_form': business_form,
            'year_data': yeardata,
            'text_fields': text_fields,
            'sell_ipcode': sell_ipcode,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form

        }
        return render(request, 'seller1/sellipcode.html', context)

    else:
        return redirect('profiles:index')


@login_required(login_url='profiles:index')
def Franchise_task(request, task_hash):
    task = None
    try:
        print('inside business_task')
        task = get_object_or_404(Task, task_hash=task_hash)
        print(task.client)
        if task.expires.time() > datetime.now().time() and task.expires.date() >= datetime.now().date():
            pass
        else:
            return redirect('staff:staff-home')
    except:
        return redirect('profiles:index')
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        'country_code_primary': 'country_code_primary',
        'name': 'name',
        'title': 'title',

    }

    revenue_fields = {
        'rev_year': 'rev_year',
        'year_16': 'year_16',
        'year_17': 'year_17',
        'year_15': 'year_15',
        'year_14': 'year_14',
        'year_13': 'year_13',
        'no_emp': 'no_emp',
        'cp_emp': 'cp_emp',
    }

    text_fields = {
        'adress': 'adress',

    }

    a = True
    if request.user.is_staff:
        if request.method == 'POST':
            seller = SellerForm(request.POST)
            business = SellFranchiseForm(request.POST)
            print('f hh ryhryh')
            print(seller.is_valid())
            print(business.is_valid())
            print(business.errors)
            if seller.is_valid() and business.is_valid():
                print('everythin is valid')
                seller_1 = seller.save(commit=False)
                seller_1.save()
                seller_1.trial = True
                seller_1.type = 'Franchise'
                if seller_1.album_id is None:
                    # fs = FileSystemStorage()
                    print('no file selected')
                    category = seller_1.category1
                    bcard_pdf_name = os.path.join(settings.MEDIA_ROOT, 'category/default_' + str(category) + '.png')
                    file=None
                    try:
                        file = File.objects.get(name = 'category/default_' + str(category) + '.png')
                    except:
                        file = File()
                        file.file.name = 'category/default_' + str(category) + '.png'
                        file.save()
                    album = KAlbumForFile()
                    album.save()
                    album.files.add(file)
                    # album.seller=seller_1
                    album.save()
                    seller_1.album_id = album.album_id
                    seller_1.save()
                seller_1.save()
                id = seller_1.business_id
                print(id)
                # m = imager(id)
                print('seller is done')
                business_1 = business.save(commit=False)
                business_1.seller = seller_1
                business_1.type = 'Franchise'
                business_1.save()
                print('business is also done')
                sell = make_sell(seller_1.business_id)
                curr_user = task.client
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                task.completed = True
                task.sell = sell
                task.save()
                if not email_checker(curr_user.id, seller_1.email_adress):
                    email_adder(curr_user, seller_1.email_adress)
                phone_number = '' + seller_1.country_code_primary + seller_1.phone_number_primary
                print(phone_number)
                if not phone_checker(curr_user.id, phone_number):
                    phone_adder(curr_user, seller_1.phone_number_primary, seller_1.country_code_primary)
                return redirect('seller1:seller-all-detail', business_id=seller_1.business_id)
            else:
                print(seller.errors)

        sectors = business_sector()
        types_companies = companies()
        code_data = codedata()
        business_form = SellerForm()
        sell_ipcode = SellFranchiseForm()
        rev_form = RevenueModelForm()
        type_fields = {
            'prod_info': 'prod_info',
            'asking_price': 'asking_price',
            'looking_for': 'looking_for',
            'website': 'website',
            'exp_ret':'exp_ret',
            'num_outlets':'num_outlets',
            'cap_req':'cap_req',
        }
        context = {
            'sectors': sectors,
            'types_companies': types_companies,
            'model_fields': model_fields,
            'code_data': code_data,
            'client': task.client,
            'business_form': business_form,
            'year_data': yeardata,
            'text_fields': text_fields,
            'sell_ipcode': sell_ipcode,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form

        }
        return render(request, 'seller1/sellfranchise.html', context)

    else:
        return redirect('profiles:index')


@login_required(login_url='profiles:index')
def Supplier_task(request, task_hash):
    task = None
    try:
        print('inside business_task')
        task = get_object_or_404(Task, task_hash=task_hash)
        print(task.client)
        if task.expires.time() > datetime.now().time() and task.expires.date() >= datetime.now().date():
            pass
        else:
            return redirect('staff:staff-home')
    except:
        return redirect('profiles:index')
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        'country_code_primary': 'country_code_primary',
        'name': 'name',
        'title': 'title',

    }

    revenue_fields = {
        'rev_year': 'rev_year',
        'year_16': 'year_16',
        'year_17': 'year_17',
        'year_15': 'year_15',
        'year_14': 'year_14',
        'year_13': 'year_13',
        'no_emp': 'no_emp',
        'cp_emp': 'cp_emp',
    }

    text_fields = {
        'adress': 'adress',

    }
    if request.user.is_staff:
        if request.method == 'POST':
            seller = SellerForm(request.POST)
            business = SupplierForm(request.POST)
            print('submit is done')
            if seller.is_valid() and business.is_valid():
                print('everythin is valid')
                seller_1 = seller.save(commit=False)
                seller_1.save()
                seller_1.trial = True
                seller_1.type = 'Supplier'
                if seller_1.album_id is None:
                    # fs = FileSystemStorage()
                    print('no file selected')
                    category = seller_1.category1
                    bcard_pdf_name = os.path.join(settings.MEDIA_ROOT, 'category/default_' + str(category) + '.png')
                    file = None
                    try:
                        file = File.objects.get(name='category/default_' + str(category) + '.png')
                    except:
                        file = File()
                        file.file.name = 'category/default_' + str(category) + '.png'
                        file.save()
                    album = KAlbumForFile()
                    album.save()
                    album.files.add(file)
                    # album.seller=seller_1
                    album.save()
                    seller_1.album_id = album.album_id
                    seller_1.save()
                seller_1.save()
                id = seller_1.business_id
                print(id)
                # m = imager(id)
                print('seller is done')
                business_1 = business.save(commit=False)
                business_1.seller = seller_1
                business_1.type = 'Supplier'
                business_1.save()
                print('business is also done')
                sell = make_sell(seller_1.business_id)
                curr_user = task.client
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                task.completed = True
                task.sell = sell
                task.save()
                if not email_checker(curr_user.id, seller_1.email_adress):
                    email_adder(curr_user, seller_1.email_adress)
                phone_number = '' + seller_1.country_code_primary + seller_1.phone_number_primary
                print(phone_number)
                if not phone_checker(curr_user.id, phone_number):
                    phone_adder(curr_user, seller_1.phone_number_primary, seller_1.country_code_primary)
                return redirect('seller1:seller-all-detail', business_id=seller_1.business_id)
            else:
                print(seller.errors)
                print(business.errors)

        sectors = business_sector()
        types_companies = companies()
        code_data = codedata()
        business_form = SellerForm()
        sell_ipcode = SupplierForm()
        rev_form = RevenueModelForm()
        type_fields = {
            'prod_info': 'prod_info',
            'asking_price': 'asking_price',
            'looking_for': 'looking_for',
            'website': 'website',
            'exp_ret':'exp_ret',
        }
        context = {
            'sectors': sectors,
            'types_companies': types_companies,
            'model_fields': model_fields,
            'code_data': code_data,
            'client': task.client,
            'business_form': business_form,
            'year_data': yeardata,
            'text_fields': text_fields,
            'sell_ipcode': sell_ipcode,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form

        }
        return render(request, 'seller1/supplier.html', context)

    else:
        return redirect('profiles:index')



