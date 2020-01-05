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
def seller(request):
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
    if a:
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
                m = imager(id)
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
                curr_user = request.user
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                return redirect('seller1:seller-user-detail', business_id=seller_1.business_id)

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
            'business_form': business_form,
            'year_data': yeardata,
            'text_fields': text_fields,
            'sell_bsn': sell_bsn,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form

        }
        return render(request, 'seller1/sellbusiness.html', context)

    else:
        return redirect('seller1/sellbusiness.html')

@login_required(login_url='profiles:index')
def SellerUpdate(request, business_id):
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        # 'country_code_primary': 'country_code_primary',
        'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller': 'about_seller',
        'address_line': 'address_line',
    }
    # if request.method == 'POST':
    business_id = business_id
    business_instance = get_object_or_404(SellBusiness, business_id=business_id)
    ktype = business_instance.type
    # ktype='Business'
    seller_id = business_instance.seller.business_id
    seller_instance = get_object_or_404(Seller1, business_id=seller_id)
    sell = Sell.objects.get(seller=seller_instance)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    revenue_instance = get_object_or_404(RevenueModel, seller=seller_instance)
    business_form = SellerUpdateForm(request.POST or None, instance=seller_instance)
    sell_bsn = BusinessUpdateForm(request.POST or None, instance=business_instance)
    rev_form = RevenueModelUpdateForm(request.POST or None, instance=revenue_instance)
    if business_form.is_valid() and sell_bsn.is_valid() and rev_form.is_valid():
        print('inside if 1')
        instance_seller = business_form.save(commit=False)
        print('inside if 2')
        instance_seller.save()
        print('inside if 3')
        instance_bsn = sell_bsn.save(commit=False)
        print('inside if 4')
        instance_bsn.save()
        instance_rev = rev_form.save(commit=False)
        instance_rev.save()
        instance_rev.seller = instance_seller
        instance_rev.save()

        print('rev done')
        instance_bsn.seller = instance_seller
        instance_bsn.type = ktype
        instance_seller.type = ktype
        instance_bsn.save()
        instance_seller.save()
        files = list(KAlbumForFile.objects.get(album_id=instance_seller.album_id).files.all())
        if len(files) == 0:
            print('inside no files in album')
            category = instance_seller.category1
            file = None
            try:
                file = File.objects.get(name='category/default_' + str(category) + '.png')
            except:
                file = File()
                file.file.name = 'category/default_' + str(category) + '.png'
                file.save()
            album = KAlbumForFile.objects.get(album_id=instance_seller.album_id)
            album.files.add(file)
            album.save()
        print('inside if 5')
        return redirect('seller1:seller-user-detail', business_id=instance_seller.business_id)
    else:
        print(business_form.errors)
        print(sell_bsn.errors)
        print(rev_form.errors)
        pass
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    print(seller_id)

    files = Ablumfiles.objects.filter(seller_id=seller_id)
    print(files)
    type_fields = {
        'about': 'about',
        'asking_price': 'asking_price',
        'year_established': 'year_established',
        'reason_selling': 'reason_selling',
        'website': 'website',
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

    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'model_fields': model_fields,
        'code_data': code_data,
        'business_form': business_form,
        'year_data': yeardata,
        'sell_bsn': sell_bsn,
        'type_fields': type_fields,
        'files': files,
        'seller': seller_instance,
        'business': business_instance,
        'seller_id': seller_id,
        'revenue_fields': revenue_fields,
        'rev_form': rev_form
    }
    return render(request, 'seller1/updatebusiness.html', context)


def imager(number):
#     # Getting static folder path from project settings
#     media_dir = settings.MEDIA_ROOT
#     #Creating a folder in static directory
#     new_dir_path = os.path.join(media_dir, "new_dir"+str(number))
#     file_path=os.path.join(media_dir, "files")
#     os.makedirs(new_dir_path)
# #    try:
# #        os.makedirs(new_dir_path)
# #    except OSError as e:
# #        if e.errno != errno.EEXIST:
# #            #directory already exists
# #            pass
# #        else:
# #            print(e)
#
#     entry=File.objects.all()
#     filename=[]
#     a=list(entry)
#     for i in a:
#         i=str(i)
#         b=i.split('/')
#         filename.append(b[1])
#
#     for i in filename:
#         start_part=os.path.join(file_path,i)
#         if os.path.isfile(start_part):
#             shutil.copy2(start_part,new_dir_path)
#             os.remove(start_part)
#     File.objects.all().delete()
#     for i in filename:
#         kkr=Ablumfiles()
#         kkr.seller_id=number
#         kkr.file_name=i
#         kkr.save()
    return(0)

def validate(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = SellerForm()
        data = {}
        if(field_get=='website'and field_val==''):
            data['error'] = ''
            data['class'] = "valid"
            data['err'] = 0
            # Avatar is valid.
            return JsonResponse(data)
        try:
            business_form.fields[field_get].clean(value=field_val)
            data['error'] = ''
            data['class'] = "valid"
            data['err'] = 0
            # Avatar is valid.
            return JsonResponse(data)

        except ValidationError as e:
            try:
                data['error'] = e.message
                data['class'] = "invalid"
                data['err'] = 1
                return JsonResponse(data, safe=False)
            except :


                data['error'] = 'Field is invalid'
                data['class'] = "invalid"
                data['err'] = 1
                # Avatar is invalid.
                return JsonResponse(data, safe=False)

def validate_bsn(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = BusinessForm()
        data = {}
        try:
            business_form.fields[field_get].clean(value=field_val)
            data['error'] = ''
            data['class'] = "valid"
            data['err'] = 0
            # Avatar is valid.
            return JsonResponse(data)

        except ValidationError as e:
            try:
                data['error'] = e.message
                data['class'] = "invalid"
                data['err'] = 1
                return JsonResponse(data, safe=False)
            except :


                data['error'] = 'Field is invalid'
                data['class'] = "invalid"
                data['err'] = 1
                # Avatar is invalid.
                return JsonResponse(data, safe=False)



def validate_asset(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = AssetForm()
        data = {}
        try:
            business_form.fields[field_get].clean(value=field_val)
            data['error'] = ''
            data['class'] = "valid"
            data['err'] = 0
            # Avatar is valid.
            return JsonResponse(data)

        except ValidationError as e:
            try:
                data['error'] = e.message
                data['class'] = "invalid"
                data['err'] = 1
                return JsonResponse(data, safe=False)
            except :


                data['error'] = 'Field is invalid'
                data['class'] = "invalid"
                data['err'] = 1
                # Avatar is invalid.
                return JsonResponse(data, safe=False)

def validate_equity(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = EquityForm()
        data = {}
        try:
            business_form.fields[field_get].clean(value=field_val)
            data['error'] = ''
            data['class'] = "valid"
            data['err'] = 0
            # Avatar is valid.
            return JsonResponse(data)

        except ValidationError as e:
            try:
                data['error'] = e.message
                data['class'] = "invalid"
                data['err'] = 1
                return JsonResponse(data, safe=False)
            except :


                data['error'] = 'Field is invalid'
                data['class'] = "invalid"
                data['err'] = 1
                # Avatar is invalid.
                return JsonResponse(data, safe=False)


def validate_loan(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = LoanForm()
        data = {}
        try:
            business_form.fields[field_get].clean(value=field_val)
            data['error'] = ''
            data['class'] = "valid"
            data['err'] = 0
            # Avatar is valid.
            return JsonResponse(data)

        except ValidationError as e:
            try:
                data['error'] = e.message
                data['class'] = "invalid"
                data['err'] = 1
                return JsonResponse(data, safe=False)
            except :


                data['error'] = 'Field is invalid'
                data['class'] = "invalid"
                data['err'] = 1
                # Avatar is invalid.
                return JsonResponse(data, safe=False)


def validate_startup(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = StartupForm()
        data = {}
        try:
            business_form.fields[field_get].clean(value=field_val)
            data['error'] = ''
            data['class'] = "valid"
            data['err'] = 0
            # Avatar is valid.
            return JsonResponse(data)

        except ValidationError as e:
            try:
                data['error'] = e.message
                data['class'] = "invalid"
                data['err'] = 1
                return JsonResponse(data, safe=False)
            except :


                data['error'] = 'Field is invalid'
                data['class'] = "invalid"
                data['err'] = 1
                # Avatar is invalid.
                return JsonResponse(data, safe=False)


def validate_supplier(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = SupplierForm()
        data = {}
        try:
            business_form.fields[field_get].clean(value=field_val)
            data['error'] = ''
            data['class'] = "valid"
            data['err'] = 0
            # Avatar is valid.
            return JsonResponse(data)

        except ValidationError as e:
            try:
                data['error'] = e.message
                data['class'] = "invalid"
                data['err'] = 1
                return JsonResponse(data, safe=False)
            except :


                data['error'] = 'Field is invalid'
                data['class'] = "invalid"
                data['err'] = 1
                # Avatar is invalid.
                return JsonResponse(data, safe=False)




def validate_ipcode(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = IpcodeForm()
        data = {}
        try:
            business_form.fields[field_get].clean(value=field_val)
            data['error'] = ''
            data['class'] = "valid"
            data['err'] = 0
            # Avatar is valid.
            return JsonResponse(data)

        except ValidationError as e:
            try:
                data['error'] = e.message
                data['class'] = "invalid"
                data['err'] = 1
                return JsonResponse(data, safe=False)
            except :


                data['error'] = 'Field is invalid'
                data['class'] = "invalid"
                data['err'] = 1
                # Avatar is invalid.
                return JsonResponse(data, safe=False)


def validate_app(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = AppForm()
        data = {}
        try:
            business_form.fields[field_get].clean(value=field_val)
            data['error'] = ''
            data['class'] = "valid"
            data['err'] = 0
            # Avatar is valid.
            return JsonResponse(data)

        except ValidationError as e:
            try:
                data['error'] = e.message
                data['class'] = "invalid"
                data['err'] = 1
                return JsonResponse(data, safe=False)
            except :


                data['error'] = 'Field is invalid'
                data['class'] = "invalid"
                data['err'] = 1
                # Avatar is invalid.
                return JsonResponse(data, safe=False)



def validate_rev(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        revenue_form = RevenueModelForm()
        data = {}
        if(field_get=='website'and field_val==''):
            data['error'] = ''
            data['class'] = "valid"
            data['err'] = 0
            # Avatar is valid.
            return JsonResponse(data)
        try:
            revenue_form.fields[field_get].clean(value=field_val)
            data['error'] = ''
            data['class'] = "valid"
            data['err'] = 0
            # Avatar is valid.
            return JsonResponse(data)

        except ValidationError as e:
            try:
                data['error'] = e.message
                data['class'] = "invalid"
                data['err'] = 1
                return JsonResponse(data, safe=False)
            except :


                data['error'] = 'Field is invalid'
                data['class'] = "invalid"
                data['err'] = 1
                # Avatar is invalid.
                return JsonResponse(data, safe=False)

def validate_franchise(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = SellFranchiseForm()
        data = {}
        try:
            business_form.fields[field_get].clean(value=field_val)
            data['error'] = ''
            data['class'] = "valid"
            data['err'] = 0
            # Avatar is valid.
            return JsonResponse(data)
        except:

            data['error'] = 'Field is invalid'
            data['class'] = "invalid"
            data['err'] = 1
            # Avatar is invalid.
            return JsonResponse(data, safe=False)


def getModelfields(request):
    if request.method == 'GET':
        model_fields = {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email',

            'business_name': 'business_name',

            'price_for_business': 'price_for_business',
            'year_established': 'year_established',

            'website': 'website',
            'revenue': 'revenue',
            'profit': 'profit',
            'cost_of_employee': 'cost_of_employee',
            'num_of_employees': 'num_of_employees'
        }
        return JsonResponse(model_fields, safe=False)


def BusinessDetail(request, business_id):
    sell_bsn=SellBusiness.objects.get(business_id=business_id)
    seller_id = sell_bsn.seller.business_id
    seller = Seller1.objects.get(business_id=seller_id)
    context={
        'sell_bsn': sell_bsn,
        'seller': seller
    }
    return render(request, 'seller1/sellbusiness-profile.html', context)

@login_required(login_url='profiles:index')
def UpdateFiles(request):
    seller_id = request.GET['seller_id']
    seller=Seller1.objects.get(business_id=seller_id)
    album_id = seller.album_id
    album = KAlbumForFile.objects.get(album_id=album_id)
    files=album.files
    print(files)
    # print(files[0].file_size)
    # ffiles = {
    #     'files':files,
    #     'seller_id':seller_id
    # }
    serializer=FileSerializer(files, many=True)
    print(serializer.data)
    return JsonResponse(json.dumps(serializer.data), safe=False)

@login_required(login_url='profiles:index')
def SellBusinessDelete(request, business_id):
    bsn_id = business_id
    bsn = SellBusiness.objects.get(business_id=bsn_id)
    seller_id = bsn.seller.business_id
    seller=Seller1.objects.get(business_id=seller_id)
    sell = Sell.objects.get(seller=seller)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    album_id = seller.album_id
    album = KAlbumForFile.objects.get(album_id=album_id)
    for file in album.files.all():
        album.files.remove(file)
        file.delete()

    album.delete()
    revenue = RevenueModel.objects.get(seller=seller)
    revenue.delete()
    seller.delete()
    bsn.delete()
    print('above redirect')
    print('below redirect')
    return redirect('profiles:index')

@login_required(login_url='profiles:index')
def SellAssetDelete(request, business_id):
    bsn_id = business_id
    bsn = SellAsset.objects.get(asset_id=bsn_id)
    seller_id = bsn.seller.business_id
    seller = Seller1.objects.get(business_id=seller_id)
    sell = Sell.objects.get(seller=seller)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    album_id = seller.album_id
    album = KAlbumForFile.objects.get(album_id=album_id)
    for file in album.files.all():
        album.files.remove(file)
        file.delete()

    album.delete()
    revenue = RevenueModel.objects.get(seller=seller)
    revenue.delete()
    seller.delete()
    bsn.delete()
    print('above redirect')
    print('below redirect')
    return redirect('profiles:index')

@login_required(login_url='profiles:index')
def RaiseLoanDelete(request, business_id):
    bsn_id = business_id
    bsn = RaiseLoan.objects.get(loan_id=bsn_id)
    seller_id = bsn.seller.business_id
    seller = Seller1.objects.get(business_id=seller_id)
    sell = Sell.objects.get(seller=seller)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    album_id = seller.album_id
    album = KAlbumForFile.objects.get(album_id=album_id)
    for file in album.files.all():
        album.files.remove(file)
        file.delete()

    album.delete()
    revenue = RevenueModel.objects.get(seller=seller)
    revenue.delete()
    seller.delete()
    bsn.delete()
    print('above redirect')
    print('below redirect')
    return redirect('profiles:index')

@login_required(login_url='profiles:index')
def SellEquityDelete(request, business_id):
    bsn_id = business_id
    bsn = SellEquity.objects.get(equity_id=bsn_id)
    seller_id = bsn.seller.business_id
    seller = Seller1.objects.get(business_id=seller_id)
    sell = Sell.objects.get(seller=seller)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    album_id = seller.album_id
    album = KAlbumForFile.objects.get(album_id=album_id)
    for file in album.files.all():
        album.files.remove(file)
        file.delete()

    album.delete()
    revenue = RevenueModel.objects.get(seller=seller)
    revenue.delete()
    seller.delete()
    bsn.delete()
    print('above redirect')
    print('below redirect')
    return redirect('profiles:index')

@login_required(login_url='profiles:index')
def SellAppDelete(request, business_id):
    bsn_id = business_id
    bsn = SellApp.objects.get(app_id=bsn_id)
    seller_id = bsn.seller.business_id
    seller = Seller1.objects.get(business_id=seller_id)
    sell = Sell.objects.get(seller=seller)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    album_id = seller.album_id
    album = KAlbumForFile.objects.get(album_id=album_id)
    for file in album.files.all():
        album.files.remove(file)
        file.delete()

    album.delete()

    seller.delete()
    bsn.delete()
    print('above redirect')
    print('below redirect')
    return redirect('profiles:index')

@login_required(login_url='profiles:index')
def SellIpcodeDelete(request, business_id):
    bsn_id = business_id
    bsn = SellIpcode.objects.get(ipcode_id=bsn_id)
    seller_id = bsn.seller.business_id
    seller = Seller1.objects.get(business_id=seller_id)
    sell = Sell.objects.get(seller=seller)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    album_id = seller.album_id
    album = KAlbumForFile.objects.get(album_id=album_id)
    for file in album.files.all():
        album.files.remove(file)
        file.delete()

    album.delete()

    seller.delete()
    bsn.delete()
    print('above redirect')
    print('below redirect')
    return redirect('profiles:index')



@login_required(login_url='profiles:index')
def SellStartupDelete(request, business_id):
    bsn_id = business_id
    bsn = SellStartup.objects.get(startup_id=bsn_id)
    seller_id = bsn.seller.business_id
    seller = Seller1.objects.get(business_id=seller_id)
    sell = Sell.objects.get(seller=seller)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    album_id = seller.album_id
    album = KAlbumForFile.objects.get(album_id=album_id)
    for file in album.files.all():
        album.files.remove(file)
        file.delete()

    album.delete()
    revenue = RevenueModel.objects.get(seller=seller)
    revenue.delete()
    seller.delete()
    bsn.delete()
    print('above redirect')
    print('below redirect')
    return redirect('profiles:index')


@login_required(login_url='profiles:index')
def SellFranchiseDelete(request, business_id):
    bsn_id = business_id
    bsn = SellFranchise.objects.get(franchise_id=bsn_id)
    seller_id = bsn.seller.business_id
    seller = Seller1.objects.get(business_id=seller_id)
    sell = Sell.objects.get(seller=seller)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    album_id = seller.album_id
    album = KAlbumForFile.objects.get(album_id=album_id)
    for file in album.files.all():
        album.files.remove(file)
        file.delete()

    album.delete()

    seller.delete()
    bsn.delete()
    print('above redirect')
    print('below redirect')
    return redirect('profiles:index')

@login_required(login_url='profiles:index')
def SellSupplierDelete(request, business_id):
    bsn_id = business_id
    bsn = Supplier.objects.get(supplier_id=bsn_id)
    seller_id = bsn.seller.business_id
    seller = Seller1.objects.get(business_id=seller_id)
    sell = Sell.objects.get(seller=seller)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    album_id = seller.album_id
    album = KAlbumForFile.objects.get(album_id=album_id)
    for file in album.files.all():
        album.files.remove(file)
        file.delete()

    album.delete()

    seller.delete()
    bsn.delete()
    print('above redirect')
    print('below redirect')
    return redirect('profiles:index')





@login_required(login_url='profiles:index')
def seller_asset(request):
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
    if a:
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
                m = imager(id)
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
                curr_user = request.user
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()

                return redirect('seller1:seller-user-detail', business_id=seller_1.business_id)

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
        return redirect('seller1/sellasset.html')

@login_required(login_url='profiles:index')
def AssetUpdate(request, business_id):
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        # 'country_code_primary': 'country_code_primary',
        'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller': 'about_seller',
        'address_line': 'address_line',
    }
    # if request.method == 'POST':
    business_id = business_id
    business_instance = get_object_or_404(SellAsset, asset_id=business_id)
    ktype = business_instance.type
    # ktype='Business'
    seller_id = business_instance.seller.business_id
    seller_instance = get_object_or_404(Seller1, business_id=seller_id)
    sell = Sell.objects.get(seller=seller_instance)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    revenue_instance = get_object_or_404(RevenueModel, seller=seller_instance)
    business_form = SellerUpdateForm(request.POST or None, instance=seller_instance)
    sell_asset = AssetUpdateForm(request.POST or None, instance=business_instance)
    rev_form = RevenueModelUpdateForm(request.POST or None, instance=revenue_instance)
    if business_form.is_valid() and sell_asset.is_valid() and rev_form.is_valid():
        print('inside if 1')
        instance_seller = business_form.save(commit=False)
        print('inside if 2')
        instance_seller.save()
        print('inside if 3')
        instance_bsn = sell_asset.save(commit=False)
        print('inside if 4')
        instance_bsn.save()
        instance_rev = rev_form.save(commit=False)
        instance_rev.save()
        instance_rev.seller = instance_seller
        instance_rev.save()
        print('rev done')
        instance_bsn.seller=instance_seller
        instance_bsn.type=ktype
        instance_seller.type=ktype
        instance_bsn.save()
        instance_seller.save()
        files = list(KAlbumForFile.objects.get(album_id=instance_seller.album_id).files.all())
        if len(files) == 0:
            print('inside no files in album')
            category = instance_seller.category1
            file = None
            try:
                file = File.objects.get(name='category/default_' + str(category) + '.png')
            except:
                file = File()
                file.file.name = 'category/default_' + str(category) + '.png'
                file.save()
            album = KAlbumForFile.objects.get(album_id=instance_seller.album_id)
            album.files.add(file)
            album.save()
        print('inside if 5')
        return redirect('seller1:seller-user-detail', business_id=instance_seller.business_id)
    else:
        print(business_form.errors)
        print(sell_asset.errors)
        print(rev_form.errors)
        pass
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    print(seller_id)

    files = Ablumfiles.objects.filter(seller_id=seller_id)
    print(files)
    type_fields = {
        'asset_type': 'asset_type',
        'about_asset': 'about_asset',
        'asking_price': 'asking_price',
        'purchase_price': 'purchase_price',
        'purchase_year': 'purchase_year',
        'reason_selling': 'reason_selling',
        'website':'website'
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

    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'model_fields': model_fields,
        'code_data': code_data,
        'business_form': business_form,
        'year_data': yeardata,
        'sell_asset': sell_asset,
        'type_fields': type_fields,
        'files': files,
        'seller':seller_instance,
        'business':business_instance,
        'seller_id': seller_id,
        'revenue_fields': revenue_fields,
        'rev_form':rev_form
    }
    return render(request, 'seller1/updateasset.html', context)



@login_required(login_url='profiles:index')
def seller_equity(request):
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
    if a:
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
                m = imager(id)
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
                curr_user = request.user
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                return redirect('seller1:seller-user-detail', business_id=seller_1.business_id)

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
        return redirect('seller1/sellequity.html')

@login_required(login_url='profiles:index')
def EquityUpdate(request, business_id):
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        # 'country_code_primary': 'country_code_primary',
        'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller': 'about_seller',
        'address_line': 'address_line',
    }
    # if request.method == 'POST':
    business_id = business_id
    business_instance = get_object_or_404(SellEquity, equity_id=business_id)
    ktype = business_instance.type
    # ktype='Business'
    seller_id = business_instance.seller.business_id
    seller_instance = get_object_or_404(Seller1, business_id=seller_id)
    sell = Sell.objects.get(seller=seller_instance)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    sell = Sell.objects.get(seller=seller_instance)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    revenue_instance = get_object_or_404(RevenueModel, seller=seller_instance)
    business_form = SellerUpdateForm(request.POST or None, instance=seller_instance)
    sell_equity = EquityUpdateForm(request.POST or None, instance=business_instance)
    rev_form = RevenueModelUpdateForm(request.POST or None, instance=revenue_instance)
    if business_form.is_valid() and sell_equity.is_valid() and rev_form.is_valid():
        print('inside if 1')
        instance_seller = business_form.save(commit=False)
        print('inside if 2')
        instance_seller.save()
        print('inside if 3')
        instance_bsn = sell_equity.save(commit=False)
        print('inside if 4')
        instance_bsn.save()
        instance_rev = rev_form.save(commit=False)
        instance_rev.save()
        instance_rev.seller = instance_seller
        instance_rev.save()
        print('rev done')
        instance_bsn.seller=instance_seller
        instance_bsn.type=ktype
        instance_seller.type=ktype
        instance_bsn.save()
        instance_seller.save()
        files = list(KAlbumForFile.objects.get(album_id=instance_seller.album_id).files.all())
        if len(files) == 0:
            print('inside no files in album')
            category = instance_seller.category1
            file = None
            try:
                file = File.objects.get(name='category/default_' + str(category) + '.png')
            except:
                file = File()
                file.file.name = 'category/default_' + str(category) + '.png'
                file.save()
            album = KAlbumForFile.objects.get(album_id=instance_seller.album_id)
            album.files.add(file)
            album.save()
        print('inside if 5')
        return redirect('seller1:seller-user-detail', business_id=instance_seller.business_id)
    else:
        print(business_form.errors)
        print(sell_equity.errors)
        print(rev_form.errors)
        pass
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    print(seller_id)

    files = Ablumfiles.objects.filter(seller_id=seller_id)
    print(files)
    type_fields = {
        'about_business': 'about_business',
        'stake': 'stake',
        'asking_price': 'asking_price',
        'year': 'year',
        'reason': 'reason',
        'website':'website'
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

    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'model_fields': model_fields,
        'code_data': code_data,
        'business_form': business_form,
        'year_data': yeardata,
        'sell_equity': sell_equity,
        'type_fields': type_fields,
        'files': files,
        'seller':seller_instance,
        'business':business_instance,
        'seller_id': seller_id,
        'revenue_fields': revenue_fields,
        'rev_form':rev_form
    }
    return render(request, 'seller1/updatequity.html', context)


@login_required(login_url='profiles:index')
def seller_loan(request):
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
    if a:
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
                m = imager(id)
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
                curr_user = request.user
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                return redirect('seller1:seller-user-detail', business_id=seller_1.business_id)

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
        return redirect('seller1/selloan.html')

@login_required(login_url='profiles:index')
def LoanUpdate(request, business_id):
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        # 'country_code_primary': 'country_code_primary',
        'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller': 'about_seller',
        'address_line': 'address_line',
    }
    # if request.method == 'POST':
    business_id = business_id
    business_instance = get_object_or_404(RaiseLoan, loan_id=business_id)
    ktype = business_instance.type
    # ktype='Business'
    seller_id = business_instance.seller.business_id
    seller_instance = get_object_or_404(Seller1, business_id=seller_id)
    sell = Sell.objects.get(seller=seller_instance)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    revenue_instance = get_object_or_404(RevenueModel, seller=seller_instance)
    business_form = SellerUpdateForm(request.POST or None, instance=seller_instance)
    sell_loan = LoanUpdateForm(request.POST or None, instance=business_instance)
    rev_form = RevenueModelUpdateForm(request.POST or None, instance=revenue_instance)
    if business_form.is_valid() and sell_loan.is_valid() and rev_form.is_valid():
        print('inside if 1')
        instance_seller = business_form.save(commit=False)
        print('inside if 2')
        instance_seller.save()
        print('inside if 3')
        instance_bsn = sell_loan.save(commit=False)
        print('inside if 4')
        instance_bsn.save()
        instance_rev = rev_form.save(commit=False)
        instance_rev.save()
        instance_rev.seller = instance_seller
        instance_rev.save()
        print('rev done')
        instance_bsn.seller=instance_seller
        instance_bsn.type=ktype
        instance_seller.type=ktype
        instance_bsn.save()
        instance_seller.save()
        files = list(KAlbumForFile.objects.get(album_id=instance_seller.album_id).files.all())
        if len(files) == 0:
            print('inside no files in album')
            category = instance_seller.category1
            file = None
            try:
                file = File.objects.get(name='category/default_' + str(category) + '.png')
            except:
                file = File()
                file.file.name = 'category/default_' + str(category) + '.png'
                file.save()
            album = KAlbumForFile.objects.get(album_id=instance_seller.album_id)
            album.files.add(file)
            album.save()
        print('inside if 5')
        return redirect('seller1:seller-user-detail', business_id=instance_seller.business_id)
    else:
        print(business_form.errors)
        print(sell_loan.errors)
        print(rev_form.errors)
        pass
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    print(seller_id)

    files = Ablumfiles.objects.filter(seller_id=seller_id)
    print(files)
    type_fields = {
        'about_business': 'about_business',
        'loan_amount': 'loan_amount',
        'sought_interest': 'sought_interest',
        'year_established': 'year_established',
        'reason_loan': 'reason_loan',
        'website': 'website'
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

    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'model_fields': model_fields,
        'code_data': code_data,
        'business_form': business_form,
        'year_data': yeardata,
        'sell_loan': sell_loan,
        'type_fields': type_fields,
        'files': files,
        'seller':seller_instance,
        'business':business_instance,
        'seller_id': seller_id,
        'revenue_fields': revenue_fields,
        'rev_form':rev_form
    }
    return render(request, 'seller1/updateloan.html', context)



@login_required(login_url='profiles:index')
def seller_startup(request):
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
    if a:
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
                m = imager(id)
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
                curr_user = request.user
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                return redirect('seller1:seller-user-detail', business_id=seller_1.business_id)

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
        return redirect('seller1/sellstartup.html')

@login_required(login_url='profiles:index')
def StartupUpdate(request, business_id):
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        # 'country_code_primary': 'country_code_primary',
        'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller': 'about_seller',
        'address_line': 'address_line',
    }
    # if request.method == 'POST':
    business_id = business_id
    business_instance = get_object_or_404(SellStartup, startup_id=business_id)
    ktype = business_instance.type
    # ktype='Business'
    seller_id = business_instance.seller.business_id
    seller_instance = get_object_or_404(Seller1, business_id=seller_id)
    sell = Sell.objects.get(seller=seller_instance)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    revenue_instance = get_object_or_404(RevenueModel, seller=seller_instance)
    business_form = SellerUpdateForm(request.POST or None, instance=seller_instance)
    sell_startup = StartupUpdateForm(request.POST or None, instance=business_instance)
    rev_form = RevenueModelUpdateForm(request.POST or None, instance=revenue_instance)
    if business_form.is_valid() and sell_startup.is_valid() and rev_form.is_valid():
        print('inside if 1')
        instance_seller = business_form.save(commit=False)
        print('inside if 2')
        instance_seller.save()
        print('inside if 3')
        instance_bsn = sell_startup.save(commit=False)
        print('inside if 4')
        instance_bsn.save()
        instance_rev = rev_form.save(commit=False)
        instance_rev.save()
        instance_rev.seller = instance_seller
        instance_rev.save()
        print('rev done')
        instance_bsn.seller=instance_seller
        instance_bsn.type=ktype
        instance_seller.type=ktype
        instance_bsn.save()
        instance_seller.save()
        files = list(KAlbumForFile.objects.get(album_id=instance_seller.album_id).files.all())
        if len(files) == 0:
            print('inside no files in album')
            category = instance_seller.category1
            file = None
            try:
                file = File.objects.get(name='category/default_' + str(category) + '.png')
            except:
                file = File()
                file.file.name = 'category/default_' + str(category) + '.png'
                file.save()
            album = KAlbumForFile.objects.get(album_id=instance_seller.album_id)
            album.files.add(file)
            album.save()
        print('inside if 5')
        return redirect('seller1:seller-user-detail', business_id=instance_seller.business_id)
    else:
        print(business_form.errors)
        print(sell_startup.errors)
        print(rev_form.errors)
        pass
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    print(seller_id)

    files = Ablumfiles.objects.filter(seller_id=seller_id)
    print(files)
    type_fields = {
        'about': 'about',
        'sought_equity': 'sought_equity',
        'asking_price': 'asking_price',
        'revenue_growth': 'revenue_growth',
        'year_established': 'year_established',
        'reason_selling': 'reason_selling',
        'website': 'website'
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

    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'model_fields': model_fields,
        'code_data': code_data,
        'business_form': business_form,
        'year_data': yeardata,
        'sell_startup': sell_startup,
        'type_fields': type_fields,
        'files': files,
        'seller':seller_instance,
        'business':business_instance,
        'seller_id': seller_id,
        'revenue_fields': revenue_fields,
        'rev_form':rev_form
    }
    return render(request, 'seller1/updatestartup.html', context)

@login_required(login_url='profiles:index')
def AppUpdate(request, business_id):
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        # 'country_code_primary': 'country_code_primary',
        # 'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller': 'about_seller',
        # 'address_line': 'address_line',
    }
    # if request.method == 'POST':
    business_id = business_id
    business_instance = get_object_or_404(SellApp, app_id=business_id)
    ktype = business_instance.type
    # ktype='Business'
    seller_id = business_instance.seller.business_id
    seller_instance = get_object_or_404(Seller1, business_id=seller_id)
    sell = Sell.objects.get(seller=seller_instance)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    # revenue_instance = get_object_or_404(RevenueModel, seller=seller_instance)
    business_form = SellerUpdateForm(request.POST or None, instance=seller_instance)
    sell_app = AppUpdateForm(request.POST or None, instance=business_instance)
    # rev_form = RevenueModelUpdateForm(request.POST or None, instance=revenue_instance)
    if business_form.is_valid() and sell_app.is_valid():
        print('inside if 1')
        instance_seller = business_form.save(commit=False)
        print('inside if 2')
        instance_seller.save()
        print('inside if 3')
        instance_bsn = sell_app.save(commit=False)
        print('inside if 4')
        instance_bsn.save()
        # instance_rev = rev_form.save(commit=False)
        # instance_rev.save()
        # instance_rev.seller = instance_seller
        # # instance_rev.save()
        # print('rev done')
        instance_bsn.seller=instance_seller
        instance_bsn.type=ktype
        instance_seller.type=ktype
        instance_bsn.save()
        instance_seller.save()
        files = list(KAlbumForFile.objects.get(album_id=instance_seller.album_id).files.all())
        if len(files) == 0:
            print('inside no files in album')
            category = instance_seller.category1
            file = None
            try:
                file = File.objects.get(name='category/default_' + str(category) + '.png')
            except:
                file = File()
                file.file.name = 'category/default_' + str(category) + '.png'
                file.save()
            album = KAlbumForFile.objects.get(album_id=instance_seller.album_id)
            album.files.add(file)
            album.save()
        print('inside if 5')
        return redirect('seller1:seller-user-detail', business_id=instance_seller.business_id)
    else:
        print(business_form.errors)
        print(sell_app.errors)
        # print(rev_form.errors)
        pass
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    print(seller_id)

    files = Ablumfiles.objects.filter(seller_id=seller_id)
    print(files)
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

    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'model_fields': model_fields,
        'code_data': code_data,
        'business_form': business_form,
        'year_data': yeardata,
        'sell_app': sell_app,
        'type_fields': type_fields,
        'files': files,
        'seller':seller_instance,
        'business':business_instance,
        'seller_id': seller_id,
        'revenue_fields': revenue_fields,
        # 'rev_form':rev_form
    }
    return render(request, 'seller1/updateapp.html', context)



@login_required(login_url='profiles:index')
def seller_app(request):
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
    if a:
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
                m = imager(id)
                print('seller is done')
                business_1 = business.save(commit=False)
                # business_1=business.save()
                business_1.seller = seller_1
                business_1.type = 'Application'
                business_1.save()
                print('business is also done')
                sell = make_sell(seller_1.business_id)
                curr_user = request.user
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                # revenue_1 = revenue.save(commit=False)
                # revenue_1.seller = seller_1
                # revenue_1.save()
                # print('revenue is also done')
                return redirect('seller1:seller-user-detail', business_id=seller_1.business_id)

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
        return redirect('seller1/sellapp.html')

@login_required(login_url='profiles:index')
def IpcodeUpdate(request, business_id):
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        # 'country_code_primary': 'country_code_primary',
        # 'name': 'name',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller': 'about_seller',
        # 'address_line': 'address_line',
    }
    # if request.method == 'POST':
    business_id = business_id
    business_instance = get_object_or_404(SellIpcode,ipcode_id=business_id)
    ktype = business_instance.type
    # ktype='Business'
    seller_id = business_instance.seller.business_id
    seller_instance = get_object_or_404(Seller1, business_id=seller_id)
    sell = Sell.objects.get(seller=seller_instance)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    # revenue_instance = get_object_or_404(RevenueModel, seller=seller_instance)
    business_form = SellerUpdateForm(request.POST or None, instance=seller_instance)
    sell_ipcode = IpcodeUpdateForm(request.POST or None, instance=business_instance)
    # rev_form = RevenueModelUpdateForm(request.POST or None, instance=revenue_instance)
    if business_form.is_valid() and sell_ipcode.is_valid():
        print('inside if 1')
        instance_seller = business_form.save(commit=False)
        print('inside if 2')
        instance_seller.save()
        print('inside if 3')
        instance_bsn = sell_ipcode.save(commit=False)
        print('inside if 4')
        instance_bsn.save()
        # instance_rev = rev_form.save(commit=False)
        # instance_rev.save()
        # instance_rev.seller = instance_seller
        # # instance_rev.save()
        # print('rev done')
        instance_bsn.seller=instance_seller
        instance_bsn.type=ktype
        instance_seller.type=ktype
        instance_bsn.save()
        instance_seller.save()
        files = list(KAlbumForFile.objects.get(album_id=instance_seller.album_id).files.all())
        if len(files) == 0:
            print('inside no files in album')
            category = instance_seller.category1
            file = None
            try:
                file = File.objects.get(name='category/default_' + str(category) + '.png')
            except:
                file = File()
                file.file.name = 'category/default_' + str(category) + '.png'
                file.save()
            album = KAlbumForFile.objects.get(album_id=instance_seller.album_id)
            album.files.add(file)
            album.save()
        print('inside if 5')
        return redirect('seller1:seller-user-detail', business_id=instance_seller.business_id)
    else:
        print(business_form.errors)
        print(sell_ipcode.errors)
        # print(rev_form.errors)
        pass
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    print(seller_id)

    files = Ablumfiles.objects.filter(seller_id=seller_id)
    print(files)
    type_fields = {
        'about': 'about',
        'asking_price': 'asking_price',
        'research_title': 'research_title',
        'website': 'website'
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

    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'model_fields': model_fields,
        'code_data': code_data,
        'business_form': business_form,
        'year_data': yeardata,
        'sell_ipcode': sell_ipcode,
        'type_fields': type_fields,
        'files': files,
        'seller':seller_instance,
        'business':business_instance,
        'seller_id': seller_id,
        'revenue_fields': revenue_fields,
        # 'rev_form':rev_form
    }
    return render(request, 'seller1/updateipcode.html', context)



@login_required(login_url='profiles:index')
def seller_ipcode(request):
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
    if a:
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
                m = imager(id)
                print('seller is done')
                business_1 = business.save(commit=False)
                # business_1=business.save()
                business_1.seller = seller_1
                business_1.type = 'Ipcode'
                business_1.save()
                print('business is also done')
                sell = make_sell(seller_1.business_id)
                curr_user = request.user
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                # revenue_1 = revenue.save(commit=False)
                # revenue_1.seller = seller_1
                # revenue_1.save()
                # print('revenue is also done')
                return redirect('seller1:seller-user-detail', business_id=seller_1.business_id)

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
        return redirect('seller1/sellipcode.html')

@login_required(login_url='profiles:index')
def seller_franchise(request):
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
    if a:
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
                m = imager(id)
                print('seller is done')
                business_1 = business.save(commit=False)
                business_1.seller = seller_1
                business_1.type = 'Franchise'
                business_1.save()
                print('business is also done')
                sell = make_sell(seller_1.business_id)
                curr_user = request.user
                curr_user.profile.sell_type.add(seller_1)
                curr_user.profile.user_sell.add(sell)
                curr_user.save()
                return redirect('seller1:seller-user-detail', business_id=seller_1.business_id)
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
        return redirect('seller1/sellipcode.html')

@login_required(login_url='profiles:index')
def FranchiseUpdate(request, business_id):
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
    # if request.method == 'POST':
    business_id = business_id
    business_instance = get_object_or_404(SellFranchise,franchise_id=business_id)
    ktype = business_instance.type
    # ktype='Business'
    seller_id = business_instance.seller.business_id
    seller_instance = get_object_or_404(Seller1, business_id=seller_id)
    sell = Sell.objects.get(seller=seller_instance)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    # revenue_instance = get_object_or_404(RevenueModel, seller=seller_instance)
    business_form = SellerUpdateForm(request.POST or None, instance=seller_instance)
    sell_franchise = FranchiseUpdateForm(request.POST or None, instance=business_instance)
    # rev_form = RevenueModelUpdateForm(request.POST or None, instance=revenue_instance)
    if business_form.is_valid() and sell_franchise.is_valid():
        print('inside if 1')
        instance_seller = business_form.save(commit=False)
        print('inside if 2')
        instance_seller.save()
        print('inside if 3')
        instance_bsn = sell_franchise.save(commit=False)
        print('inside if 4')
        instance_bsn.save()
        # instance_rev = rev_form.save(commit=False)
        # instance_rev.save()
        # instance_rev.seller = instance_seller
        # # instance_rev.save()
        # print('rev done')
        instance_bsn.seller=instance_seller
        instance_bsn.type=ktype
        instance_seller.type=ktype
        instance_bsn.save()
        instance_seller.save()
        files = list(KAlbumForFile.objects.get(album_id=instance_seller.album_id).files.all())
        if len(files) == 0:
            print('inside no files in album')
            category = instance_seller.category1
            file = None
            try:
                file = File.objects.get(name='category/default_' + str(category) + '.png')
            except:
                file = File()
                file.file.name = 'category/default_' + str(category) + '.png'
                file.save()
            album = KAlbumForFile.objects.get(album_id=instance_seller.album_id)
            album.files.add(file)
            album.save()
        print('inside if 5')
        return redirect('seller1:seller-user-detail', business_id=instance_seller.business_id)
    else:
        print(business_form.errors)
        print(sell_franchise.errors)
        # print(rev_form.errors)
        pass
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    print(seller_id)

    files = Ablumfiles.objects.filter(seller_id=seller_id)
    print(files)
    type_fields = {
        'prod_info': 'prod_info',
        'asking_price': 'asking_price',
        'looking_for': 'looking_for',
        'website': 'website',
        'exp_ret': 'exp_ret',
        'num_outlets': 'num_outlets',
        'cap_req':'cap_req',            
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

    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'model_fields': model_fields,
        'code_data': code_data,
        'business_form': business_form,
        'year_data': yeardata,
        'sell_ipcode': sell_franchise,
        'type_fields': type_fields,
        'files': files,
        'seller':seller_instance,
        'business':business_instance,
        'seller_id': seller_id,
        # 'revenue_fields': revenue_fields,
        # 'rev_form':rev_form
    }
    return render(request, 'seller1/updatefranchise.html', context)

@login_required(login_url='profiles:index')
def seller_supplier(request):
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
            m = imager(id)
            print('seller is done')
            business_1 = business.save(commit=False)
            business_1.seller = seller_1
            business_1.type = 'Supplier'
            business_1.save()
            print('business is also done')
            sell = make_sell(seller_1.business_id)
            curr_user = request.user
            curr_user.profile.sell_type.add(seller_1)
            curr_user.profile.user_sell.add(sell)
            curr_user.save()
            return redirect('seller1:seller-user-detail', business_id=seller_1.business_id)
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
        'business_form': business_form,
        'year_data': yeardata,
        'text_fields': text_fields,
        'sell_ipcode': sell_ipcode,
        'type_fields': type_fields,
        'revenue_fields': revenue_fields,
        'rev_form': rev_form

    }
    return render(request, 'seller1/supplier.html', context)

@login_required(login_url='profiles:index')
def SupplierUpdate(request, business_id):
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
    # if request.method == 'POST':
    business_id = business_id
    business_instance = get_object_or_404(Supplier,supplier_id=business_id)
    ktype = business_instance.type
    # ktype='Business'
    seller_id = business_instance.seller.business_id
    seller_instance = get_object_or_404(Seller1, business_id=seller_id)
    sell = Sell.objects.get(seller=seller_instance)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    # revenue_instance = get_object_or_404(RevenueModel, seller=seller_instance)
    business_form = SellerUpdateForm(request.POST or None, instance=seller_instance)
    sell_franchise = SupplierUpdateForm(request.POST or None, instance=business_instance)
    # rev_form = RevenueModelUpdateForm(request.POST or None, instance=revenue_instance)
    if business_form.is_valid() and sell_franchise.is_valid():
        print('inside if 1')
        instance_seller = business_form.save(commit=False)
        print('inside if 2')
        instance_seller.save()
        print('inside if 3')
        instance_bsn = sell_franchise.save(commit=False)
        print('inside if 4')
        instance_bsn.save()
        # instance_rev = rev_form.save(commit=False)
        # instance_rev.save()
        # instance_rev.seller = instance_seller
        # # instance_rev.save()
        # print('rev done')
        instance_bsn.seller=instance_seller
        instance_bsn.type=ktype
        instance_seller.type=ktype
        instance_bsn.save()
        instance_seller.save()
        files = list(KAlbumForFile.objects.get(album_id=instance_seller.album_id).files.all())
        if len(files) == 0:
            print('inside no files in album')
            category = instance_seller.category1
            file = None
            try:
                file = File.objects.get(name='category/default_' + str(category) + '.png')
            except:
                file = File()
                file.file.name = 'category/default_' + str(category) + '.png'
                file.save()
            album = KAlbumForFile.objects.get(album_id=instance_seller.album_id)
            album.files.add(file)
            album.save()
        print('inside if 5')
        return redirect('seller1:seller-user-detail', business_id=instance_seller.business_id)
    else:
        print(business_form.errors)
        print(sell_franchise.errors)
        # print(rev_form.errors)
        pass
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    print(seller_id)

    files = Ablumfiles.objects.filter(seller_id=seller_id)
    print(files)
    type_fields = {
        'prod_info': 'prod_info',
        'asking_price': 'asking_price',
        'looking_for': 'looking_for',
        'website': 'website',
        'exp_ret': 'exp_ret',
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

    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'model_fields': model_fields,
        'code_data': code_data,
        'business_form': business_form,
        'year_data': yeardata,
        'sell_ipcode': sell_franchise,
        'type_fields': type_fields,
        'files': files,
        'seller':seller_instance,
        'business':business_instance,
        'seller_id': seller_id,
        # 'revenue_fields': revenue_fields,
        # 'rev_form':rev_form
    }
    return render(request, 'seller1/updatesupplier.html', context)






@login_required(login_url='profiles:index')
def detail_sell_type(request, business_id):
    seller = Seller1.objects.get(business_id=business_id)
    sell = Sell.objects.get(seller=seller)
    user = request.user
    user_sells = user.profile.user_sell.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    sell = Sell.objects.get(seller=seller)
    print(sell)
    stype = sell.type
    smodel = model_list[stype].objects.get(seller=seller)
    sserializer = serializer_list[stype](smodel)
    sdata = sserializer.data
    serializer = SellerSerializer(seller)
    data = serializer.data
    cdata = data.copy()
    # cdata.update(sdata)
    main_album_id = seller.album_id
    main_album = KAlbumForFile(album_id=main_album_id)
    main_files = main_album.files.all()
    srevenue = None
    rdata = None
    try:
        srevenue = RevenueModel.objects.get(seller=seller)
        rserializer = RevenueModelSerializer(srevenue)
        rdata = rserializer.data
        cdata.update(rdata)
    except:
        print('no revenue')
    # jdata = json.load(cdata)

    if seller.trial:
        seller.trial = False
        seller.save()
    fdata = {}
    fdata['seller'] = cdata
    fdata['business'] = sdata
    fdata['inst_invest'] = []
    fdata['inst_advisor'] = []
    fdata['cart_investor'] = []
    fdata['cart_advisor'] = []
    fdata['cart_seller'] = []
    fdata['inst_seller'] = []
    fdata['cart'] = []
    fdata['inst'] = []
    inst_invest = sell.inst_investors.all()
    inst_advisor = sell.inst_advisor.all()
    cart_investor = sell.cart_investor.all()
    cart_advisor = sell.cart_advisor.all()
    for investor in inst_invest:
        serializer = InvestorSerializer(investor)
        x = serializer.data
        album_id = investor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Investor'
        }
        itype = investor.type

        imodel = inv_model_list[itype].objects.get(investor=investor)
        iserializer = inv_serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        cx.update(y)
        cx.update(z)
        fdata['inst_invest'].append(cx)

    for investor in cart_investor:
        serializer = InvestorSerializer(investor)
        x = serializer.data
        album_id = investor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Investor'
        }
        itype = investor.type

        imodel = inv_model_list[itype].objects.get(investor=investor)
        iserializer = inv_serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        cx.update(y)
        cx.update(z)
        fdata['cart_investor'].append(cx)

    for advisor in inst_advisor:
        serializer = AdvisorSerializer(advisor)
        x = serializer.data
        album_id = advisor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Advisor'
        }
        itype = advisor.type

        imodel = adv_model_list[itype].objects.get(advisor=advisor)
        iserializer = adv_serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        cx.update(y)
        cx.update(z)
        fdata['inst_advisor'].append(cx)

    for advisor in cart_advisor:
        serializer = AdvisorSerializer(advisor)
        x = serializer.data
        album_id = advisor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Advisor'
        }
        itype = advisor.type

        imodel = adv_model_list[itype].objects.get(advisor=advisor)
        iserializer = adv_serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        cx.update(y)
        cx.update(z)
        fdata['cart_advisor'].append(cx)
    if seller.type=='Supplier':
        cart_sellers=sell.cart_sellers.all()
        inst_sellers=sell.inst_sellers.all()
        for investor in cart_sellers:
            serializer = SellerSerializer(investor)
            x = serializer.data
            album_id = investor.album_id
            album = KAlbumForFile.objects.get(album_id=album_id)
            file = album.files.all()[0]
            file_name = file.name
            y = {
                'file_name': file_name,
                'base_type': 'Seller'
            }
            itype = investor.type
            seller_id = investor.business_id
            r = None
            try:
                srevenue = RevenueModel.objects.get(seller=investor)
                rserializer = RevenueModelSerializer(srevenue)
                r = rserializer.data
            except:
                r = {}
                print('no revenue')
            imodel = model_list[itype].objects.get(seller=investor)
            iserializer = serializer_list[itype](imodel)
            z = iserializer.data
            cx = x.copy()
            k = {
                'seller_id': seller_id
            }
            cx.update(y)
            # cx.update(z)
            cx.update(r)
            data = {}
            data['seller'] = cx
            data['business'] = z
            fdata['cart_seller'].append(data)

        for investor in inst_sellers:
            serializer = SellerSerializer(investor)
            x = serializer.data
            album_id = investor.album_id
            album = KAlbumForFile.objects.get(album_id=album_id)
            file = album.files.all()[0]
            file_name = file.name
            y = {
                'file_name': file_name,
                'base_type': 'Seller'
            }
            itype = investor.type
            seller_id = investor.business_id
            r = None
            try:
                srevenue = RevenueModel.objects.get(seller=investor)
                rserializer = RevenueModelSerializer(srevenue)
                r = rserializer.data
            except:
                r = {}
                print('no revenue')
            imodel = model_list[itype].objects.get(seller=investor)
            iserializer = serializer_list[itype](imodel)
            z = iserializer.data
            cx = x.copy()
            k = {
                'seller_id': seller_id
            }
            cx.update(y)
            # cx.update(z)
            cx.update(r)
            data = {}
            data['seller'] = cx
            data['business'] = z
            fdata['inst_seller'].append(data)
    else:
        cart_sellers = sell.cart_suppliers.all()
        inst_sellers = sell.inst_suppliers.all()
        for investor in cart_sellers:
            serializer = SellerSerializer(investor)
            x = serializer.data
            album_id = investor.album_id
            album = KAlbumForFile.objects.get(album_id=album_id)
            file = album.files.all()[0]
            file_name = file.name
            y = {
                'file_name': file_name,
                'base_type': 'Seller'
            }
            itype = investor.type
            seller_id = investor.business_id
            r = None
            try:
                srevenue = RevenueModel.objects.get(seller=investor)
                rserializer = RevenueModelSerializer(srevenue)
                r = rserializer.data
            except:
                r = {}
                print('no revenue')
            imodel = model_list[itype].objects.get(seller=investor)
            iserializer = serializer_list[itype](imodel)
            z = iserializer.data
            cx = x.copy()
            k = {
                'seller_id': seller_id
            }
            cx.update(y)
            # cx.update(z)
            cx.update(r)
            data = {}
            data['seller'] = cx
            data['business'] = z
            fdata['cart_seller'].append(data)

        for investor in inst_sellers:
            serializer = SellerSerializer(investor)
            x = serializer.data
            album_id = investor.album_id
            album = KAlbumForFile.objects.get(album_id=album_id)
            file = album.files.all()[0]
            file_name = file.name
            y = {
                'file_name': file_name,
                'base_type': 'Seller'
            }
            itype = investor.type
            seller_id = investor.business_id
            r = None
            try:
                srevenue = RevenueModel.objects.get(seller=investor)
                rserializer = RevenueModelSerializer(srevenue)
                r = rserializer.data
            except:
                r = {}
                print('no revenue')
            imodel = model_list[itype].objects.get(seller=investor)
            iserializer = serializer_list[itype](imodel)
            z = iserializer.data
            cx = x.copy()
            k = {
                'seller_id': seller_id
            }
            cx.update(y)
            # cx.update(z)
            cx.update(r)
            data = {}
            data['seller'] = cx
            data['business'] = z
            fdata['inst_seller'].append(data)

    fdata['images'] = []
    for file in main_files:
        name = file.name
        name_dict = {
            'file_name': name
        }
        fdata['images'].append(name_dict)
    fdata['same'] = 'False'
    user = request.user
    for xseller in user.profile.sell_type.all():
        if xseller == seller:
            fdata['same'] = 'True'

    fdata['cart'] = list(chain(fdata['cart_investor'], fdata['cart_advisor'], fdata['cart_seller']))
    print('adjvhb')
    print(fdata['cart'])
    random.shuffle(fdata['cart'])
    print(fdata['cart'])
    fdata['inst'] = list(chain(fdata['inst_advisor'], fdata['inst_invest'], fdata['inst_seller']))
    print(fdata['inst'])
    random.shuffle(fdata['cart'])
    print(fdata['inst'])

    basic_fields = 11
    # type_fields = 0
    # optional = 0
    revenue_fields = 8
    fdata['optional'] = 0
    fdata['total_fields'] = 0
    fdata['completeness'] = None
    if stype == 'Business':
        type_fields = 5
        total_fields = int(basic_fields) + int(type_fields) + int(revenue_fields)
        optional = 0
        if smodel.website is None or smodel.website == '':
            print(smodel.website)
            optional = optional + 1
        if srevenue.year_16 is None or srevenue.year_16 == 0:
            print(srevenue.year_16)
            optional = optional + 1
        if srevenue.year_17 is None or srevenue.year_17 == 0:
            optional = optional + 1
        if srevenue.year_15 is None or srevenue.year_15 == 0:
            optional = optional + 1
        if srevenue.year_14 is None or srevenue.year_14 == 0:
            optional = optional + 1
        if srevenue.year_13 is None or srevenue.year_13 == 0:
            optional = optional + 1
        if srevenue.no_emp is None or srevenue.no_emp == 0:
            optional = optional + 1
        if srevenue.cp_emp is None or srevenue.cp_emp == 0:
            optional = optional + 1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields
    if stype == 'Asset':
        type_fields = 6
        total_fields = int(basic_fields) + int(type_fields) + int(revenue_fields)
        optional = 0
        # if smodel.website:
        #     optional = optional +1
        if srevenue.year_16 is None or srevenue.year_16 == 0:
            optional = optional + 1
        if srevenue.year_17 is None or srevenue.year_17 == 0:
            optional = optional + 1
        if srevenue.year_15 is None or srevenue.year_15 == 0:
            optional = optional + 1
        if srevenue.year_14 is None or srevenue.year_14 == 0:
            optional = optional + 1
        if srevenue.year_13 is None or srevenue.year_13 == 0:
            optional = optional + 1
        if srevenue.no_emp is None or srevenue.no_emp == 0:
            optional = optional + 1
        if srevenue.cp_emp is None or srevenue.cp_emp == 0:
            optional = optional + 1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields
    if stype == 'Loan':
        type_fields = 6
        total_fields = int(basic_fields) + int(type_fields) + int(revenue_fields)
        optional = 0
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        if srevenue.year_16 is None or srevenue.year_16 == 0:
            optional = optional + 1
        if srevenue.year_17 is None or srevenue.year_17 == 0:
            optional = optional + 1
        if srevenue.year_15 is None or srevenue.year_15 == 0:
            optional = optional + 1
        if srevenue.year_14 is None or srevenue.year_14 == 0:
            optional = optional + 1
        if srevenue.year_13 is None or srevenue.year_13 == 0:
            optional = optional + 1
        if srevenue.no_emp is None or srevenue.no_emp == 0:
            optional = optional + 1
        if srevenue.cp_emp is None or srevenue.cp_emp == 0:
            optional = optional + 1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields
    if stype == 'Equity':
        type_fields = 6
        optional = 0
        total_fields = int(basic_fields) + int(type_fields) + int(revenue_fields)
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        if srevenue.year_16 is None or srevenue.year_16 == 0:
            optional = optional + 1
        if srevenue.year_17 is None or srevenue.year_17 == 0:
            optional = optional + 1
        if srevenue.year_15 is None or srevenue.year_15 == 0:
            optional = optional + 1
        if srevenue.year_14 is None or srevenue.year_14 == 0:
            optional = optional + 1
        if srevenue.year_13 is None or srevenue.year_13 == 0:
            optional = optional + 1
        if srevenue.no_emp is None or srevenue.no_emp == 0:
            optional = optional + 1
        if srevenue.cp_emp is None or srevenue.cp_emp == 0:
            optional = optional + 1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness

    if stype == 'Startup':
        type_fields = 6
        optional = 0
        total_fields = int(basic_fields) + int(type_fields) + int(revenue_fields)
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        if srevenue.year_16 is None or srevenue.year_16 == 0:
            optional = optional + 1
        if srevenue.year_17 is None or srevenue.year_17 == 0:
            optional = optional + 1
        if srevenue.year_15 is None or srevenue.year_15 == 0:
            optional = optional + 1
        if srevenue.year_14 is None or srevenue.year_14 == 0:
            optional = optional + 1
        if srevenue.year_13 is None or srevenue.year_13 == 0:
            optional = optional + 1
        if srevenue.no_emp is None or srevenue.no_emp == 0:
            optional = optional + 1
        if srevenue.cp_emp is None or srevenue.cp_emp == 0:
            optional = optional + 1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields

    if stype == 'Application':
        type_fields = 17
        optional = 0
        total_fields = int(basic_fields) + int(type_fields)
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        if smodel.email_app is None or smodel.email_app == '':
            optional = optional + 1
        if smodel.monitization_method is None or smodel.monitization_method == '':
            optional = optional + 1
        if smodel.platform_used is None or smodel.platform_used == '':
            optional = optional + 1
        if smodel.y1_views is None or smodel.y1_views == 0:
            optional = optional + 1
        if smodel.y2_views is None or smodel.y2_views == 0:
            optional = optional + 1
        if smodel.y3_views is None or smodel.y3_views == 0:
            optional = optional + 1
        if smodel.y1_users is None or smodel.y1_users == 0:
            optional = optional + 1
        if smodel.y2_users is None or smodel.y2_users == 0:
            optional = optional + 1
        if smodel.y3_users is None or smodel.y3_users == 0:
            optional = optional + 1
        # if srevenue.year_16 or srevenue.year_16==0:
        #     optional = optional +1
        # if srevenue.year_17 or srevenue.year_17==0:
        #     optional = optional +1
        # if srevenue.year_15 or srevenue.year_15==0:
        #     optional = optional +1
        # if srevenue.year_14 or srevenue.year_14==0:
        #     optional = optional +1
        # if srevenue.year_13 or srevenue.year_13==0:
        #     optional = optional +1
        # if srevenue.no_emp or srevenue.no_emp==0:
        #     optional = optional +1
        # if srevenue.cp_emp or srevenue.cp_emp==0:
        #     optional = optional +1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields

    if stype == 'Ipcode':
        type_fields = 6
        optional = 0
        total_fields = int(basic_fields) + int(type_fields)
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        if smodel.product_type is None or smodel.product_type == '':
            optional = optional + 1
        # if srevenue.year_16 or srevenue.year_16==0:
        #     optional = optional +1
        # if srevenue.year_17 or srevenue.year_17==0:
        #     optional = optional +1
        # if srevenue.year_15 or srevenue.year_15==0:
        #     optional = optional +1
        # if srevenue.year_14 or srevenue.year_14==0:
        #     optional = optional +1
        # if srevenue.year_13 or srevenue.year_13==0:
        #     optional = optional +1
        # if srevenue.no_emp or srevenue.no_emp==0:
        #     optional = optional +1
        # if srevenue.cp_emp or srevenue.cp_emp==0:
        #     optional = optional +1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields

    if stype == 'Franchise':
        type_fields = 7
        optional = 0
        total_fields = int(basic_fields) + int(type_fields)
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        if smodel.cap_req is None or smodel.cap_req == 0:
            optional = optional + 1
        # if srevenue.year_16 or srevenue.year_16==0:
        #     optional = optional +1
        # if srevenue.year_17 or srevenue.year_17==0:
        #     optional = optional +1
        # if srevenue.year_15 or srevenue.year_15==0:
        #     optional = optional +1
        # if srevenue.year_14 or srevenue.year_14==0:
        #     optional = optional +1
        # if srevenue.year_13 or srevenue.year_13==0:
        #     optional = optional +1
        # if srevenue.no_emp or srevenue.no_emp==0:
        #     optional = optional +1
        # if srevenue.cp_emp or srevenue.cp_emp==0:
        #     optional = optional +1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields

    if stype == 'Supplier':
        type_fields = 3
        optional = 0
        total_fields = int(basic_fields) + int(type_fields)
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        # if smodel.cap_req is None or smodel.cap_req==0:
        #     optional = optional +1
        # if srevenue.year_16 or srevenue.year_16==0:
        #     optional = optional +1
        # if srevenue.year_17 or srevenue.year_17==0:
        #     optional = optional +1
        # if srevenue.year_15 or srevenue.year_15==0:
        #     optional = optional +1
        # if srevenue.year_14 or srevenue.year_14==0:
        #     optional = optional +1
        # if srevenue.year_13 or srevenue.year_13==0:
        #     optional = optional +1
        # if srevenue.no_emp or srevenue.no_emp==0:
        #     optional = optional +1
        # if srevenue.cp_emp or srevenue.cp_emp==0:
        #     optional = optional +1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields
    print('check_completeness_here')
    print(fdata['completeness'])

    return render(request, 'seller1/detail.html', fdata)

@login_required(login_url='profiles:index')
def just_sell_type(request, business_id):
    seller = Seller1.objects.get(business_id=business_id)
    category=seller.category1
    sub_category=seller.category2
    sell = Sell.objects.get(seller=seller)
    print(sell)
    stype = sell.type
    base_type='Business'
    sell_list = ['Application', 'Ipcode', 'Startup']
    if stype in sell_list:
        base_type='Startup'


    smodel = model_list[stype].objects.get(seller=seller)
    sserializer = serializer_list[stype](smodel)
    sdata = sserializer.data
    serializer = SellerSerializer(seller)
    data = serializer.data
    cdata = data.copy()

    # cdata.update(sdata)
    main_album_id = seller.album_id
    main_album = KAlbumForFile(album_id=main_album_id)
    main_files = main_album.files.all()
    srevenue = None
    rdata = None
    try:
        srevenue = RevenueModel.objects.get(seller=seller)
        rserializer = RevenueModelSerializer(srevenue)
        rdata = rserializer.data
        cdata.update(rdata)
    except:
        print('no revenue')
    # jdata = json.load(cdata)
    fdata = {}
    fdata['seller']=cdata
    fdata['business']=sdata
    fdata['inst_invest']=[]
    fdata['inst_advisor']=[]
    fdata['cart_investor']=[]
    fdata['cart_advisor']=[]
    fdata['cart']=[]
    fdata['inst']=[]
    fdata['base_type'] = base_type
    inst_invest = sell.inst_investors.all()
    inst_advisor = sell.inst_advisor.all()
    cart_investor = sell.cart_investor.all()
    cart_advisor = sell.cart_advisor.all()

    fdata['images'] = []
    for file in main_files:
        name = file.name
        name_dict = {
            'file_name': name
        }
        fdata['images'].append(name_dict)
    fdata['same']='False'
    user = request.user
    fdata['first_image']=main_files[0].name
    for xseller in user.profile.sell_type.all():
        if xseller == seller:
            fdata['same'] = 'True'

    fdata['cart'] = list(chain(fdata['cart_investor'], fdata['cart_advisor']))
    print('adjvhb')
    print(fdata['cart'])
    random.shuffle(fdata['cart'])
    print(fdata['cart'])
    fdata['inst'] = list(chain(fdata['inst_advisor'], fdata['inst_invest']))
    print(fdata['inst'])
    random.shuffle(fdata['cart'])
    print(fdata['inst'])

    user = request.user
    investor = user.profile.user_invest.all()
    # iserializer = None
    # invest = None
    all_isell = {}
    # if investor is not None:
    #     iserializer=InvestorSerializer(investor)
    #     invest = Invest.objects.get(investor=investor)
    #     invest_sell = invest.cart_seller.all()
    #     all_isell= SellerSerializer(invest_sell, many=True).data
    data_investor = []
    for invest in investor:
        iserializer = InvestorSerializer(invest.investor).data
        data_investor.append(iserializer)
        iname = 'investor_' + str(invest.investor.investor_id)
        all_isell[iname] = SellerSerializer(invest.cart_seller.all(), many=True).data
    # data_investor = None
    # if iserializer is not None:
    #     data_investor = iserializer.data
    #     exist = {
    #         'exist': 'True'
    #     }
    #     cdata = data_investor.copy()
    #     cdata.update(exist)
    #     data_investor = cdata
    # else:
    #     data_investor = {
    #         'exist': 'False'
    #     }
    sellers = user.profile.sell_type.all()
    data_sellers = []
    if sellers is not None:
        data_sellers = SellerSerializer(sellers, many=True).data
    print(data_sellers)
    data_advisors = []

    advisors = user.profile.user_advise.all()

    for advisor in advisors:
        if stype=='Franchise':
            asreializer = AdvisorSerializer(advisor.advisor)
            data_advisors.append(asreializer.data)
        else:
            if advisor.advisor.type==base_type:
                asreializer = AdvisorSerializer(advisor.advisor)
                data_advisors.append(asreializer.data)
    # if advisors is not None:
    #     data_advisors= AdvisorSerializer(advisors, many=True)
    print(data_advisors)
    just_sell = user.profile.just_sell.all()
    all_jsell = []
    all_jsell = SellerSerializer(just_sell, many=True).data
    his_sell = user.profile.user_sell.all()
    all_hsell = []
    all_supsell=[]
    all_sup_sell=[]
    for sell in his_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data
        all_hsell.append(dseller)
        if stype=='Supplier':
            if sell_seller.type != 'Supplier':
                all_supsell.append(dseller)
                all_sup_sell.append(sell)
        else:
            if sell_seller.type == 'Supplier':
                all_supsell.append(dseller)
                all_sup_sell.append(sell)
    # advises = user.profile.user_advise.all()
    all_sup_sellers = {}
    for sell in all_sup_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data
        sell_advisors=[]
        if stype=='Supplier':
            sell_advisors = sell.cart_suppliers.all()
        else:
            sell_advisors = sell.cart_sellers.all()
        name = 'seller_' + str(sell_seller.business_id)
        all_sup_sellers[name] = []
        for one_advisor in sell_advisors:
            done_advisor = SellerSerializer(one_advisor).data
            all_sup_sellers[name].append(done_advisor)
    advises = user.profile.user_advise.all()
    all_aisell = {}
    # all_aisell['startup'] = {}
    # all_aisell['business'] = {}
    for advise in advises:
        if stype=='Franchise':
            aname = 'advisor_' + str(advise.advisor.advisor_id)
            all_aisell[aname] = SellerSerializer(advise.cart_seller, many=True).data
        else:
            if advise.type == base_type:
                aname = 'advisor_' + str(advise.advisor.advisor_id)
                all_aisell[aname] = SellerSerializer(advise.cart_seller, many=True).data
        # if advise.type == 'Business':
        #     aname = 'advisor_' + str(advise.advisor.advisor_id)
        #     all_aisell['business'][aname] = SellerSerializer(advise.cart_seller, many=True).data
    # print(fdata)
    fdata['data_investor']= json.dumps(data_investor)
    fdata['supp_sellers']=json.dumps(all_supsell)
    fdata['seller_sellers']=json.dumps(all_sup_sellers)
    # fdata['data_sellers']: data_sellers
    fdata['data_advisors']= json.dumps(data_advisors)
    fdata['just_sellers']= json.dumps(all_jsell)
    fdata['advise_sellers']= json.dumps(all_aisell)
    fdata['invest_sellers']= json.dumps(all_isell)
    fdata['my_sellers']= json.dumps(all_hsell)
    fdata['similar_seller']=[]
    # similar_seller = Seller1.objects.filter(category1=category, category2=sub_category, type=stype)
    similar_sell = Sell.objects.all()
    # similar_seller = []
    for similar_seller in similar_sell:
        investor = similar_seller.seller
        if seller == investor:
            continue
        serializer = SellerSerializer(investor)
        x = serializer.data
        album_id = investor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type':'Seller'
        }
        itype = investor.type
        seller_id = investor.business_id
        r = None
        try:
            srevenue = RevenueModel.objects.get(seller=investor)
            rserializer = RevenueModelSerializer(srevenue)
            r = rserializer.data
        except:
            r = {}
            print('no revenue')
        imodel = model_list[itype].objects.get(seller=investor)
        iserializer = serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        k = {
            'seller_id': seller_id
        }
        cx.update(y)
        # cx.update(z)
        cx.update(r)
        data = {}
        data['seller'] = cx
        data['business'] = z
        fdata['similar_seller'].append(data)

    print(fdata['supp_sellers'])
    unlock_sell = Sell.objects.get(seller=seller)
    fdata['unlock_status'] = False
    if unlock_sell in user.profile.sell_unlocks.all():
        fdata['unlock_status'] = True
    print(user.profile.user_sell.all())
    print(unlock_sell)
    if unlock_sell in user.profile.user_sell.all():
        fdata['unlock_status'] = True
    # print(user.profile.sell_unlocks.all())
    # print('check sell id')
    # print(sell)
    #
    # for unlocked_sell in user.profile.sell_unlocks.all():
    #     print(unlocked_sell.sell_id)
    #     if unlocked_sell.sell_id == sell.sell_id:
    #         print(unlocked_sell.sell_id)
    #         print(sell.sell_id)
    #         fdata['unlock_status'] = True
    #         break

    print('check unlock status')
    print(fdata['unlock_status'])
    seller = Seller1.objects.get(business_id=business_id)
    sell = Sell.objects.get(seller=seller)
    print(sell)
    stype = sell.type
    srevenue = None
    try:
        srevenue = RevenueModel.objects.get(seller=seller)
    except:
        pass
    basic_fields = 11
    # type_fields = 0
    # optional = 0
    revenue_fields = 8
    fdata['optional'] = 0
    fdata['total_fields'] = 0
    fdata['completeness'] = None
    if stype == 'Business':
        type_fields = 5
        total_fields = int(basic_fields) + int(type_fields) + int(revenue_fields)
        optional = 0
        print(srevenue)
        if smodel.website is None or smodel.website == '':
            print(smodel.website)
            optional = optional + 1
        if srevenue.year_16 is None or srevenue.year_16 == 0:
            print(srevenue.year_16)
            optional = optional + 1
        if srevenue.year_17 is None or srevenue.year_17 == 0:
            optional = optional + 1
        if srevenue.year_15 is None or srevenue.year_15 == 0:
            optional = optional + 1
        if srevenue.year_14 is None or srevenue.year_14 == 0:
            optional = optional + 1
        if srevenue.year_13 is None or srevenue.year_13 == 0:
            optional = optional + 1
        if srevenue.no_emp is None or srevenue.no_emp == 0:
            optional = optional + 1
        if srevenue.cp_emp is None or srevenue.cp_emp == 0:
            optional = optional + 1
        completeness = 100*(total_fields-optional)/total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields
    if stype == 'Asset':
        type_fields = 6
        total_fields = int(basic_fields) + int(type_fields) + int(revenue_fields)
        optional = 0
        # if smodel.website:
        #     optional = optional +1
        if srevenue.year_16 is None or srevenue.year_16 == 0:
            optional = optional + 1
        if srevenue.year_17 is None or srevenue.year_17 == 0:
            optional = optional + 1
        if srevenue.year_15 is None or srevenue.year_15 == 0:
            optional = optional + 1
        if srevenue.year_14 is None or srevenue.year_14 == 0:
            optional = optional + 1
        if srevenue.year_13 is None or srevenue.year_13 == 0:
            optional = optional + 1
        if srevenue.no_emp is None or srevenue.no_emp == 0:
            optional = optional + 1
        if srevenue.cp_emp is None or srevenue.cp_emp == 0:
            optional = optional + 1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields
    if stype == 'Loan':
        type_fields = 6
        total_fields = int(basic_fields) + int(type_fields) + int(revenue_fields)
        optional = 0
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        if srevenue.year_16 is None or srevenue.year_16 == 0:
            optional = optional + 1
        if srevenue.year_17 is None or srevenue.year_17 == 0:
            optional = optional + 1
        if srevenue.year_15 is None or srevenue.year_15 == 0:
            optional = optional + 1
        if srevenue.year_14 is None or srevenue.year_14 == 0:
            optional = optional + 1
        if srevenue.year_13 is None or srevenue.year_13 == 0:
            optional = optional + 1
        if srevenue.no_emp is None or srevenue.no_emp == 0:
            optional = optional + 1
        if srevenue.cp_emp is None or srevenue.cp_emp == 0:
            optional = optional + 1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields
    if stype == 'Equity':
        type_fields = 6
        optional = 0
        total_fields = int(basic_fields) + int(type_fields) + int(revenue_fields)
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        if srevenue.year_16 is None or srevenue.year_16 == 0:
            optional = optional + 1
        if srevenue.year_17 is None or srevenue.year_17 == 0:
            optional = optional + 1
        if srevenue.year_15 is None or srevenue.year_15 == 0:
            optional = optional + 1
        if srevenue.year_14 is None or srevenue.year_14 == 0:
            optional = optional + 1
        if srevenue.year_13 is None or srevenue.year_13 == 0:
            optional = optional + 1
        if srevenue.no_emp is None or srevenue.no_emp == 0:
            optional = optional + 1
        if srevenue.cp_emp is None or srevenue.cp_emp == 0:
            optional = optional + 1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness

    if stype == 'Startup':
        type_fields = 6
        optional = 0
        total_fields = int(basic_fields) + int(type_fields) + int(revenue_fields)
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        if srevenue.year_16 is None or srevenue.year_16 == 0:
            optional = optional + 1
        if srevenue.year_17 is None or srevenue.year_17 == 0:
            optional = optional + 1
        if srevenue.year_15 is None or srevenue.year_15 == 0:
            optional = optional + 1
        if srevenue.year_14 is None or srevenue.year_14 == 0:
            optional = optional + 1
        if srevenue.year_13 is None or srevenue.year_13 == 0:
            optional = optional + 1
        if srevenue.no_emp is None or srevenue.no_emp == 0:
            optional = optional + 1
        if srevenue.cp_emp is None or srevenue.cp_emp == 0:
            optional = optional + 1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields

    if stype == 'Application':
        type_fields = 17
        optional = 0
        total_fields = int(basic_fields) + int(type_fields)
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        if smodel.email_app is None or smodel.email_app == '':
            optional = optional + 1
        if smodel.monitization_method is None or smodel.monitization_method == '':
            optional = optional + 1
        if smodel.platform_used is None or smodel.platform_used == '':
            optional = optional + 1
        if smodel.y1_views is None or smodel.y1_views == 0:
            optional = optional + 1
        if smodel.y2_views is None or smodel.y2_views == 0:
            optional = optional + 1
        if smodel.y3_views is None or smodel.y3_views == 0:
            optional = optional + 1
        if smodel.y1_users is None or smodel.y1_users == 0:
            optional = optional + 1
        if smodel.y2_users is None or smodel.y2_users == 0:
            optional = optional + 1
        if smodel.y3_users is None or smodel.y3_users == 0:
            optional = optional + 1
        # if srevenue.year_16 or srevenue.year_16==0:
        #     optional = optional +1
        # if srevenue.year_17 or srevenue.year_17==0:
        #     optional = optional +1
        # if srevenue.year_15 or srevenue.year_15==0:
        #     optional = optional +1
        # if srevenue.year_14 or srevenue.year_14==0:
        #     optional = optional +1
        # if srevenue.year_13 or srevenue.year_13==0:
        #     optional = optional +1
        # if srevenue.no_emp or srevenue.no_emp==0:
        #     optional = optional +1
        # if srevenue.cp_emp or srevenue.cp_emp==0:
        #     optional = optional +1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields

    if stype == 'Ipcode':
        type_fields = 6
        optional = 0
        total_fields = int(basic_fields) + int(type_fields)
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        if smodel.product_type is None or smodel.product_type == '':
            optional = optional + 1
        # if srevenue.year_16 or srevenue.year_16==0:
        #     optional = optional +1
        # if srevenue.year_17 or srevenue.year_17==0:
        #     optional = optional +1
        # if srevenue.year_15 or srevenue.year_15==0:
        #     optional = optional +1
        # if srevenue.year_14 or srevenue.year_14==0:
        #     optional = optional +1
        # if srevenue.year_13 or srevenue.year_13==0:
        #     optional = optional +1
        # if srevenue.no_emp or srevenue.no_emp==0:
        #     optional = optional +1
        # if srevenue.cp_emp or srevenue.cp_emp==0:
        #     optional = optional +1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields

    if stype == 'Franchise':
        type_fields = 7
        optional = 0
        total_fields = int(basic_fields) + int(type_fields)
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        if smodel.cap_req is None or smodel.cap_req == 0:
            optional = optional + 1
        # if srevenue.year_16 or srevenue.year_16==0:
        #     optional = optional +1
        # if srevenue.year_17 or srevenue.year_17==0:
        #     optional = optional +1
        # if srevenue.year_15 or srevenue.year_15==0:
        #     optional = optional +1
        # if srevenue.year_14 or srevenue.year_14==0:
        #     optional = optional +1
        # if srevenue.year_13 or srevenue.year_13==0:
        #     optional = optional +1
        # if srevenue.no_emp or srevenue.no_emp==0:
        #     optional = optional +1
        # if srevenue.cp_emp or srevenue.cp_emp==0:
        #     optional = optional +1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields

    if stype == 'Supplier':
        type_fields = 3
        optional = 0
        total_fields = int(basic_fields) + int(type_fields)
        if smodel.website is None or smodel.website == '':
            optional = optional + 1
        # if smodel.cap_req is None or smodel.cap_req==0:
        #     optional = optional +1
        # if srevenue.year_16 or srevenue.year_16==0:
        #     optional = optional +1
        # if srevenue.year_17 or srevenue.year_17==0:
        #     optional = optional +1
        # if srevenue.year_15 or srevenue.year_15==0:
        #     optional = optional +1
        # if srevenue.year_14 or srevenue.year_14==0:
        #     optional = optional +1
        # if srevenue.year_13 or srevenue.year_13==0:
        #     optional = optional +1
        # if srevenue.no_emp or srevenue.no_emp==0:
        #     optional = optional +1
        # if srevenue.cp_emp or srevenue.cp_emp==0:
        #     optional = optional +1
        completeness = 100 * (total_fields - optional) / total_fields
        fdata['completeness'] = completeness
        fdata['optional'] = optional
        fdata['total_fields'] = total_fields

    print(fdata)


    return render(request, 'seller1/sell_detail.html', fdata)


def just_advise_type(request, business_id):
    seller = Advisor.objects.get(business_id=business_id)
    sell = Advise.objects.get(advisor=seller)
    print(sell)
    stype = sell.type
    smodel = adv_model_list[stype].objects.get(advisor=seller)
    sserializer = adv_serializer_list[stype](smodel)
    sdata = sserializer.data
    serializer = AdvisorSerializer(seller)
    data = serializer.data
    cdata = data.copy()
    # cdata.update(sdata)
    main_album_id = seller.album_id
    main_album = KAlbumForFile(album_id=main_album_id)
    main_files = main_album.files.all()
    srevenue = None
    # rdata = None
    # try:
    #     srevenue = RevenueModel.objects.get(seller=seller)
    #     rserializer = RevenueModelSerializer(srevenue)
    #     rdata = rserializer.data
    #     cdata.update(rdata)
    # except:
    #     print('no revenue')
    # jdata = json.load(cdata)
    fdata = {}
    fdata['seller']=cdata
    fdata['business']=sdata
    fdata['inst_invest']=[]
    fdata['inst_seller']=[]
    fdata['cart_invest']=[]
    fdata['cart_seller']=[]
    inst_invest = sell.inst_invest.all()
    inst_seller = sell.inst_seller.all()
    cart_investor = sell.cart_invest.all()
    cart_seller = sell.cart_seller.all()
    for investor in inst_invest:
        serializer = InvestorSerializer(investor)
        x=serializer.data
        album_id = investor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y={
            'file_name':file_name
        }
        itype = investor.type

        imodel = inv_model_list[itype].objects.get(investor=investor)
        iserializer = inv_serializer_list[itype](imodel)
        z=iserializer.data
        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx
        data['business'] = z
        fdata['inst_invest'].append(data)

    for investor in cart_investor:
        serializer = InvestorSerializer(investor)
        x=serializer.data
        album_id = investor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y={
            'file_name':file_name
        }
        itype = investor.type

        imodel = inv_model_list[itype].objects.get(investor=investor)
        iserializer = inv_serializer_list[itype](imodel)
        z=iserializer.data
        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx
        data['business'] = z
        fdata['cart_invest'].append(data)

    for advisor in inst_seller:
        serializer = SellerSerializer(advisor)
        x=serializer.data
        album_id = advisor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y={
            'file_name':file_name
        }
        itype = advisor.type

        imodel = model_list[itype].objects.get(seller=advisor)
        iserializer = serializer_list[itype](imodel)
        z=iserializer.data
        cx = x.copy()
        cx.update(y)
        r = None
        try:
            srevenue = RevenueModel.objects.get(seller=investor)
            rserializer = RevenueModelSerializer(srevenue)
            r = rserializer.data
            cx.update(r)
        except:
            r = {}
            print('no revenue')
        # cx.update(z)
        data = {}
        data['seller']=cx
        data['business']=z
        fdata['inst_seller'].append(data)


    for advisor in cart_seller:
        serializer = SellerSerializer(advisor)
        x=serializer.data
        album_id = advisor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y={
            'file_name':file_name
        }
        itype = advisor.type

        imodel = adv_model_list[itype].objects.get(advisor=advisor)
        iserializer = adv_serializer_list[itype](imodel)
        z=iserializer.data
        cx = x.copy()
        cx.update(y)
        r = None
        try:
            srevenue = RevenueModel.objects.get(seller=investor)
            rserializer = RevenueModelSerializer(srevenue)
            r = rserializer.data
            cx.update(r)
        except:
            r = {}
            print('no revenue')
        # cx.update(z)
        data['seller'] = cx
        data['business'] = z
        fdata['cart_seller'].append(data)

    fdata['images'] = []
    for file in main_files:
        name = file.name
        name_dict = {
            'file_name': name
        }
        fdata['images'].append(name_dict)
    fdata['same']='False'
    user = request.user
    for xseller in user.profile.sell_type.all():
        if xseller == seller:
            fdata['same'] = 'True'


    print(fdata)
    return render(request, 'seller1/sell_detail.html', fdata)

def get_models_by_category(type, category, sub_category='', country='', state='', city=''):
    print(type)
    print(category)
    print(sub_category)
    print(country)
    print(state)
    print(city)
    all_sellers = []
    # print(all_sellers)
    all_sub_sellers = []
    # print(all_sub_sellers)
    all_country_sellers=[]
    # all_country_sellers = Seller1.objects.filter(category1=category, type=type, country=country)
    all_state_sellers = []
    # if state != '':
    #     all_state_sellers = Seller1.objects.filter(category1=category, type=type,
    #                                                country=country,
    #                                                region=state)
    all_city_sellers = []
    # if city != '':
    #     all_city_sellers = Seller1.objects.filter(category1=category, type=type,
    #                                               country=country,
    #                                               region=state, city=city)
    if category !='':
        if city !='':
            all_city_sellers = Seller1.objects.filter(category1=category, type=type,
                                                      country=country,
                                                      region=state, city=city)

            print(all_city_sellers)
            print('all_city')
            add_state_sellers = Seller1.objects.filter(category1=category, type=type,
                                                      country=country,
                                                      region=state).exclude(city=city)
            print('all_state')
            print(add_state_sellers)
            add_country_sellers = Seller1.objects.filter(category1=category, type=type,
                                                      country=country).exclude(region=state)
            print('all_country')
            print(add_country_sellers)
            other_country_sellers = Seller1.objects.filter(category1=category,
                                                           type=type).exclude(country=country)
            same_country_sellers = Seller1.objects.filter(country=country,
                                                          type=type).exclude(category1=category)
            other_sellers = Seller1.objects.filter(type=type).exclude(category1=category).exclude(country=country)
            print(same_country_sellers)
            print(other_sellers)
            all_city_sellers=list(chain(all_city_sellers, add_state_sellers, add_country_sellers, other_country_sellers,
                                        same_country_sellers, other_sellers))
            # all_city_sellers.append(add_state_sellers)
            # all_city_sellers.append(add_country_sellers)
            # all_city_sellers.append(other_country_sellers)
            # all_city_sellers.append(same_country_sellers)
            # all_city_sellers.append(other_sellers)
            data = {}
            # data['all_sellers'] = all_sellers
            # data['all_sub_sellers'] = all_sub_sellers
            # data['all_country_sellers'] = all_country_sellers
            # data['all_state_sellers'] = all_state_sellers
            data['all_city_sellers'] = all_city_sellers
            return data
        if state !='':
            # all_city_sellers = Seller1.objects.filter(category1=category, type=type,
            #                                           country=country,
            #                                           region=state, city=city)
            add_state_sellers = Seller1.objects.filter(category1=category, type=type,
                                                      country=country,
                                                      region=state)
            add_country_sellers = Seller1.objects.filter(category1=category, type=type,
                                                      country=country).exclude(region=state)
            other_country_sellers = Seller1.objects.filter(category1=category,
                                                           type=type).exclude(country=country)
            same_country_sellers = Seller1.objects.filter(country=country,
                                                          type=type).exclude(category1=category)
            other_sellers = Seller1.objects.filter(type=type).exclude(country=country).exclude(category1=category)
            all_city_sellers=list(chain(add_state_sellers, add_country_sellers,
                                        other_country_sellers, same_country_sellers, other_sellers))
            # all_city_sellers.append(add_state_sellers)
            # all_city_sellers.append(add_country_sellers)
            # all_city_sellers.append(other_country_sellers)
            # all_city_sellers.append(same_country_sellers)
            # all_city_sellers.append(other_sellers)
            data = {}
            # data['all_sellers'] = all_sellers
            # data['all_sub_sellers'] = all_sub_sellers
            # data['all_country_sellers'] = all_country_sellers
            # data['all_state_sellers'] = all_state_sellers
            data['all_city_sellers'] = all_city_sellers
            return data
        if country !='':
            # all_city_sellers = Seller1.objects.filter(category1=category, type=type,
            #                                           country=country,
            #                                           region=state, city=city)
            # add_state_sellers = Seller1.objects.filter(category1=category, type=type,
            #                                           country=country,
            #                                           region=state)
            add_country_sellers = Seller1.objects.filter(category1=category, type=type,
                                                      country=country)
            other_country_sellers = Seller1.objects.filter(category1=category, type=type).exclude(country=country)
            same_country_sellers = Seller1.objects.filter(country=country, type=type).exclude(category1=category)
            other_sellers = Seller1.objects.filter(type=type).exclude(country=country).exclude(category1=category)
            all_city_sellers=list(chain(add_country_sellers, other_country_sellers, same_country_sellers, other_sellers))
            # all_city_sellers.append(add_state_sellers)
            # all_city_sellers.append(add_country_sellers)
            # all_city_sellers.append(other_country_sellers)
            # all_city_sellers.append(same_country_sellers)
            # all_city_sellers.append(other_sellers)
            data = {}
            # data['all_sellers'] = all_sellers
            # data['all_sub_sellers'] = all_sub_sellers
            # data['all_country_sellers'] = all_country_sellers
            # data['all_state_sellers'] = all_state_sellers
            data['all_city_sellers'] = all_city_sellers
            return data
        other_country_sellers = Seller1.objects.filter(category1=category, type=type)
        other_sellers = Seller1.objects.filter(type=type).exclude(category1=category)
        all_city_sellers = list(chain(other_country_sellers, other_sellers))
        # all_city_sellers.append(add_state_sellers)
        # all_city_sellers.append(add_country_sellers)
        # all_city_sellers.append(other_country_sellers)
        # all_city_sellers.append(same_country_sellers)
        # all_city_sellers.append(other_sellers)
        data = {}
        # data['all_sellers'] = all_sellers
        # data['all_sub_sellers'] = all_sub_sellers
        # data['all_country_sellers'] = all_country_sellers
        # data['all_state_sellers'] = all_state_sellers
        data['all_city_sellers'] = all_city_sellers
        return data
    else:
        if city !='':
            all_city_sellers = Seller1.objects.filter(type=type,
                                                      country=country,
                                                      region=state, city=city)
            add_state_sellers = Seller1.objects.filter(type=type,
                                                      country=country,
                                                      region=state).exclude(city=city)
            add_country_sellers = Seller1.objects.filter(type=type,
                                                      country=country).exclude(region=state)
            other_country_sellers = Seller1.objects.filter(type=type).exclude(country=country)
            # same_country_sellers = Seller1.objects.filter(country=country,
            #                                               type=type).exclude(city=city, region=state)
            # other_sellers = Seller1.objects.filter(type=type).exclude(city=city,
            #                                                           region=state, country=country)
            all_city_sellers=list(chain(all_city_sellers, add_state_sellers, add_country_sellers, other_country_sellers))
            # all_city_sellers.append(add_state_sellers)
            # all_city_sellers.append(add_country_sellers)
            # all_city_sellers.append(other_country_sellers)
            # all_city_sellers.append(same_country_sellers)
            # all_city_sellers.append(other_sellers)
            data = {}
            # data['all_sellers'] = all_sellers
            # data['all_sub_sellers'] = all_sub_sellers
            # data['all_country_sellers'] = all_country_sellers
            # data['all_state_sellers'] = all_state_sellers
            data['all_city_sellers'] = all_city_sellers
            return data
        if state !='':
            # all_city_sellers = Seller1.objects.filter(category1=category, type=type,
            #                                           country=country,
            #                                           region=state, city=city)
            add_state_sellers = Seller1.objects.filter(type=type,
                                                      country=country,
                                                      region=state)
            add_country_sellers = Seller1.objects.filter(type=type,
                                                      country=country).exclude(region=state)
            other_country_sellers = Seller1.objects.filter(type=type).exclude(country=country)
            # same_country_sellers = Seller1.objects.filter(country=country,
            #                                               type=type).exclude(region=state)
            # other_sellers = Seller1.objects.filter(type=type).exclude(region=state, country=country)
            all_city_sellers=list(chain(add_state_sellers, add_country_sellers,
                                        other_country_sellers))
            # all_city_sellers.append(add_state_sellers)
            # all_city_sellers.append(add_country_sellers)
            # all_city_sellers.append(other_country_sellers)
            # all_city_sellers.append(same_country_sellers)
            # all_city_sellers.append(other_sellers)
            data = {}
            # data['all_sellers'] = all_sellers
            # data['all_sub_sellers'] = all_sub_sellers
            # data['all_country_sellers'] = all_country_sellers
            # data['all_state_sellers'] = all_state_sellers
            data['all_city_sellers'] = all_city_sellers
            return data
        if country !='':
            # all_city_sellers = Seller1.objects.filter(category1=category, type=type,
            #                                           country=country,
            #                                           region=state, city=city)
            # add_state_sellers = Seller1.objects.filter(category1=category, type=type,
            #                                           country=country,
            #                                           region=state)
            add_country_sellers = Seller1.objects.filter(type=type,
                                                      country=country)
            other_country_sellers = Seller1.objects.filter(type=type).exclude(country=country)
            # same_country_sellers = Seller1.objects.filter(country=country, type=type)
            # other_sellers = Seller1.objects.filter(type=type).exclude(country=country)
            all_city_sellers=list(chain(add_country_sellers, other_country_sellers))
            # all_city_sellers.append(add_state_sellers)
            # all_city_sellers.append(add_country_sellers)
            # all_city_sellers.append(other_country_sellers)
            # all_city_sellers.append(same_country_sellers)
            # all_city_sellers.append(other_sellers)
            data = {}
            # data['all_sellers'] = all_sellers
            # data['all_sub_sellers'] = all_sub_sellers
            # data['all_country_sellers'] = all_country_sellers
            # data['all_state_sellers'] = all_state_sellers
            data['all_city_sellers'] = all_city_sellers
            return data
        other_sellers = Seller1.objects.filter(type=type)
        all_city_sellers = list(chain(other_sellers))
        # all_city_sellers.append(add_state_sellers)
        # all_city_sellers.append(add_country_sellers)
        # all_city_sellers.append(other_country_sellers)
        # all_city_sellers.append(same_country_sellers)
        # all_city_sellers.append(other_sellers)
        data = {}
        # data['all_sellers'] = all_sellers
        # data['all_sub_sellers'] = all_sub_sellers
        # data['all_country_sellers'] = all_country_sellers
        # data['all_state_sellers'] = all_state_sellers
        data['all_city_sellers'] = all_city_sellers
        return data




def get_models_by_category_advise(type, category, sub_category='', country='', state='', city=''):
    print(type)
    print(category)
    print(sub_category)
    print(country)
    print(state)
    print(city)

    result_list_city=[]
    if category != '':

        if city != '':
            all_city_sellers = BusinessAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
                                                              all_city__icontains=city, all_state__icontains=state,
                                                              all_country__icontains=country)
            all_state_sellers = BusinessAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
                                                               all_state__icontains=state,
                                                               all_country__icontains=country).exclude(
                all_city__icontains=city)
            all_country_sellers = BusinessAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                 all_country__icontains=country).exclude(
                all_state__icontains=state)
            other_country_sellers = BusinessAdvisor.objects.filter(all_category__icontains=category,
                                                                   about_seller=type).exclude(
                all_country__icontains=country)
            same_country_sellers = BusinessAdvisor.objects.filter(all_country__icontains=country,
                                                                  about_seller=type).exclude(
                all_category__icontains=category)
            other_sellers = BusinessAdvisor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country).exclude(all_category__icontains=category)
            result_list_city = list(
                chain(all_city_sellers, all_state_sellers, all_country_sellers, other_country_sellers,
                      same_country_sellers,
                      other_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data

        if state != '':
            # all_city_sellers = BusinessAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
            #                                                      all_city__icontains=city, all_state__icontains=state,
            #                                                      all_country__icontains=country)
            all_state_sellers = BusinessAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
                                                               all_state__icontains=state,
                                                               all_country__icontains=country)
            all_country_sellers = BusinessAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                 all_country__icontains=country).exclude(
                all_state__icontains=state)
            other_country_sellers = BusinessAdvisor.objects.filter(all_category__icontains=category,
                                                                   about_seller=type).exclude(
                all_country__icontains=country)
            same_country_sellers = BusinessAdvisor.objects.filter(all_country__icontains=country,
                                                                  about_seller=type).exclude(
                all_category__icontains=category)
            other_sellers = BusinessAdvisor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country).exclude(all_category__icontains=category)
            result_list_city = list(
                chain(all_state_sellers, all_country_sellers, other_country_sellers,
                      same_country_sellers, other_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data

        if country != '':
            # all_city_sellers = BusinessAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
            #                                                      all_city__icontains=city, all_state__icontains=state,
            #                                                      all_country__icontains=country)
            # all_state_sellers = BusinessAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
            #                                                       all_state__icontains=state,
            #                                                       all_country__icontains=country)
            all_country_sellers = BusinessAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                 all_country__icontains=country)
            other_country_sellers = BusinessAdvisor.objects.filter(all_category__icontains=category,
                                                                   about_seller=type).exclude(
                all_country__icontains=country)
            same_country_sellers = BusinessAdvisor.objects.filter(all_country__icontains=country,
                                                                  about_seller=type).exclude(
                all_category__icontains=category)
            other_sellers = BusinessAdvisor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country).exclude(all_category__icontains=category)
            result_list_city = list(
                chain(all_country_sellers, other_country_sellers,
                      same_country_sellers, other_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data

        other_sellers = BusinessAdvisor.objects.filter(about_seller=type, all_category__icontains=category)
        category_sellers = BusinessAdvisor.objects.filter(about_seller=type).exclude(all_category__icontains=category)
        result_list_city = list(
            chain(other_sellers, category_sellers))
        print(result_list_city)
        data = {}
        data['all_city_sellers'] = result_list_city
        return data
    else:
        if city != '':
            all_city_sellers = BusinessAdvisor.objects.filter(about_seller=type,
                                                              all_city__icontains=city, all_state__icontains=state,
                                                              all_country__icontains=country)
            all_state_sellers = BusinessAdvisor.objects.filter(about_seller=type,
                                                               all_state__icontains=state,
                                                               all_country__icontains=country).exclude(
                all_city__icontains=city)
            all_country_sellers = BusinessAdvisor.objects.filter(about_seller=type,
                                                                 all_country__icontains=country).exclude(
                all_state__icontains=state)
            other_country_sellers = BusinessAdvisor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country)
            # same_country_sellers = BusinessAdvisor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state)
            # other_sellers = BusinessAdvisor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(all_city_sellers, all_state_sellers, all_country_sellers, other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if state != '':
            # all_city_sellers = BusinessAdvisor.objects.filter(about_seller=type,
            #                                                   all_city__icontains=city, all_state__icontains=state,
            #                                                   all_country__icontains=country)
            all_state_sellers = BusinessAdvisor.objects.filter(about_seller=type,
                                                               all_state__icontains=state,
                                                               all_country__icontains=country)
            all_country_sellers = BusinessAdvisor.objects.filter(about_seller=type,
                                                                 all_country__icontains=country).exclude(
                all_state__icontains=state)
            other_country_sellers = BusinessAdvisor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country)
            # same_country_sellers = BusinessAdvisor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #                                                         all_state__icontains=state)
            # other_sellers = BusinessAdvisor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(all_state_sellers, all_country_sellers, other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if country != '':
            # all_city_sellers = BusinessAdvisor.objects.filter(about_seller=type,
            #                                                   all_city__icontains=city, all_state__icontains=state,
            #                                                   all_country__icontains=country)
            # all_state_sellers = BusinessAdvisor.objects.filter(about_seller=type,
            #                                                    all_state__icontains=state,
            #                                                    all_country__icontains=country)
            all_country_sellers = BusinessAdvisor.objects.filter(about_seller=type,
                                                                 all_country__icontains=country)
            other_country_sellers = BusinessAdvisor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country)
            # same_country_sellers = BusinessAdvisor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #                                                         all_state__icontains=state)
            # other_sellers = BusinessAdvisor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(all_country_sellers, other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data

        other_country_sellers = BusinessAdvisor.objects.filter(about_seller=type)
        # same_country_sellers = BusinessAdvisor.objects.filter(all_country__icontains=country,
        #                                                       about_seller=type).exclude(
        #                                                         all_state__icontains=state)
        # other_sellers = BusinessAdvisor.objects.filter(about_seller=type).exclude(
        #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
        result_list_city = list(
            chain(other_country_sellers))
        print(result_list_city)
        data = {}
        data['all_city_sellers'] = result_list_city
        return data



    # data = {}
    # data['all_sellers']=all_sellers
    # data['all_sub_sellers'] = all_sub_sellers
    # data['all_country_sellers']=result_list_country
    # data['all_state_sellers']=result_list_state
    # data['all_city_sellers']=result_list_city
    # return data


def get_models_by_category_advise_startup(type, category, sub_category='', country='', state='', city=''):
    print(type)
    print(category)
    print(sub_category)
    print(country)
    print(state)
    print(city)

    result_list_city=[]

    # if sub_category == '':
    #     all_city_sellers = StartupAdvisor.objects.filter(category1=category, about_seller=type)
    #
    #     all_city_advisor1 = StartupAdvisor.objects.filter(category2=category, about_seller=type)
    #
    #     all_city_advisor2 = StartupAdvisor.objects.filter(category3=category, about_seller=type)
    #
    #     result_list_city_2 = list(chain(all_city_sellers, all_city_advisor1, all_city_advisor2))
    #     print(result_list_city_2)
    #     data = {}
    #     data['all_city_sellers'] = result_list_city_2
    #     return data
    if category != '':

        if city != '':
            all_city_sellers = StartupAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
                                                             all_city__icontains=city, all_state__icontains=state,
                                                             all_country__icontains=country)
            all_state_sellers = StartupAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
                                                              all_state__icontains=state,
                                                              all_country__icontains=country).exclude(
                all_city__icontains=city)
            all_country_sellers = StartupAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                all_country__icontains=country).exclude(
                all_state__icontains=state)
            other_country_sellers = StartupAdvisor.objects.filter(all_category__icontains=category,
                                                                  about_seller=type).exclude(
            all_country__icontains=country)
            same_country_sellers = StartupAdvisor.objects.filter(all_country__icontains=country,
                                                                 about_seller=type).exclude(
                all_category__icontains=category)
            other_sellers = StartupAdvisor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country).exclude(all_category__icontains=category)
            result_list_city = list(
                chain(all_city_sellers, all_state_sellers, all_country_sellers, other_country_sellers,
                      same_country_sellers,
                      other_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data

        if state != '':
            # all_city_sellers = StartupAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
            #                                                      all_city__icontains=city, all_state__icontains=state,
            #                                                      all_country__icontains=country)
            all_state_sellers = StartupAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
                                                              all_state__icontains=state,
                                                              all_country__icontains=country)
            all_country_sellers = StartupAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                all_country__icontains=country).exclude(
                all_state__icontains=state)
            other_country_sellers = StartupAdvisor.objects.filter(all_category__icontains=category,
                                                                  about_seller=type).exclude(
                all_country__icontains=country)
            same_country_sellers = StartupAdvisor.objects.filter(all_country__icontains=country,
                                                                 about_seller=type).exclude(
                all_category__icontains=category)
            other_sellers = StartupAdvisor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country).exclude(all_category__icontains=category)
            result_list_city = list(
                chain(all_state_sellers, all_country_sellers, other_country_sellers,
                      same_country_sellers, other_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data

        if country != '':
            # all_city_sellers = StartupAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
            #                                                      all_city__icontains=city, all_state__icontains=state,
            #                                                      all_country__icontains=country)
            # all_state_sellers = StartupAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
            #                                                       all_state__icontains=state,
            #                                                       all_country__icontains=country)
            all_country_sellers = StartupAdvisor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                all_country__icontains=country)
            other_country_sellers = StartupAdvisor.objects.filter(all_category__icontains=category,
                                                                  about_seller=type).exclude(
                all_country__icontains=country)
            same_country_sellers = StartupAdvisor.objects.filter(all_country__icontains=country,
                                                                 about_seller=type).exclude(
                all_category__icontains=category)
            other_sellers = StartupAdvisor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country).exclude(all_category__icontains=category)
            result_list_city = list(
                chain(all_country_sellers, other_country_sellers,
                      same_country_sellers, other_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data

        other_sellers = StartupAdvisor.objects.filter(about_seller=type, all_category__icontains=category)
        category_sellers = StartupAdvisor.objects.filter(about_seller=type).exclude(all_category__icontains=category)
        result_list_city = list(
            chain(other_sellers, category_sellers))
        print(result_list_city)
        data = {}
        data['all_city_sellers'] = result_list_city
        return data
    else:
        if city != '':
            all_city_sellers = StartupAdvisor.objects.filter(about_seller=type,
                                                             all_city__icontains=city, all_state__icontains=state,
                                                             all_country__icontains=country)
            all_state_sellers = StartupAdvisor.objects.filter(about_seller=type,
                                                              all_state__icontains=state,
                                                              all_country__icontains=country).exclude(
                all_city__icontains=city)
            all_country_sellers = StartupAdvisor.objects.filter(about_seller=type,
                                                                all_country__icontains=country).exclude(
                all_state__icontains=state)
            other_country_sellers = StartupAdvisor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country)
            # same_country_sellers = StartupAdvisor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state)
            # other_sellers = StartupAdvisor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(all_city_sellers, all_state_sellers, all_country_sellers, other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if state != '':
            # all_city_sellers = StartupAdvisor.objects.filter(about_seller=type,
            #                                                   all_city__icontains=city, all_state__icontains=state,
            #                                                   all_country__icontains=country)
            all_state_sellers = StartupAdvisor.objects.filter(about_seller=type,
                                                              all_state__icontains=state,
                                                              all_country__icontains=country)
            all_country_sellers = StartupAdvisor.objects.filter(about_seller=type,
                                                                all_country__icontains=country).exclude(
                all_state__icontains=state)
            other_country_sellers = StartupAdvisor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country)
            # same_country_sellers = StartupAdvisor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #                                                         all_state__icontains=state)
            # other_sellers = StartupAdvisor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(all_state_sellers, all_country_sellers, other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if country != '':
            # all_city_sellers = StartupAdvisor.objects.filter(about_seller=type,
            #                                                   all_city__icontains=city, all_state__icontains=state,
            #                                                   all_country__icontains=country)
            # all_state_sellers = StartupAdvisor.objects.filter(about_seller=type,
            #                                                    all_state__icontains=state,
            #                                                    all_country__icontains=country)
            all_country_sellers = StartupAdvisor.objects.filter(about_seller=type,
                                                                all_country__icontains=country)
            other_country_sellers = StartupAdvisor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country)
            # same_country_sellers = StartupAdvisor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #                                                         all_state__icontains=state)
            # other_sellers = StartupAdvisor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(all_country_sellers, other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data

        other_country_sellers = StartupAdvisor.objects.filter(about_seller=type)
        # same_country_sellers = StartupAdvisor.objects.filter(all_country__icontains=country,
        #                                                       about_seller=type).exclude(
        #                                                         all_state__icontains=state)
        # other_sellers = StartupAdvisor.objects.filter(about_seller=type).exclude(
        #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
        result_list_city = list(
            chain(other_country_sellers))
        print(result_list_city)
        data = {}
        data['all_city_sellers'] = result_list_city
        return data

    # print(all_sub_sellers)
    # print(all_country_sellers)
    # print(all_state_sellers)
    # data = {}
    # data['all_sellers']=all_sellers
    # data['all_sub_sellers'] = all_sub_sellers
    # data['all_country_sellers']=result_list_country
    # data['all_state_sellers']=result_list_state
    # data['all_city_sellers']=result_list_city
    # return data




def get_models_by_category_invest(type, category, sub_category='', country='', state='', city='', base_type='Individual'):
    print(type)
    print(category)
    print(sub_category)
    print(country)
    print(state)
    print(city)
    print(base_type)

    result_list_city=[]
    # if sub_category == '' and base_type == 'Individual':
    #     all_city_sellers = IndividualInvestor.objects.filter(category1=category, about_seller=type)
    #
    #     all_city_advisor1 = IndividualInvestor.objects.filter(category2=category, about_seller=type)
    #
    #     all_city_advisor2 = IndividualInvestor.objects.filter(category3=category, about_seller=type)
    #
    #     result_list_city_2 = list(chain(all_city_sellers, all_city_advisor1, all_city_advisor2))
    #     print(result_list_city_2)
    #     data = {}
    #     data['all_city_sellers'] = result_list_city_2
    #     return data
    if category !='':

        if city != '' and base_type=='Individual':
            all_city_sellers = IndividualInvestor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                 all_city__icontains=city, all_state__icontains=state,
                                                                 all_country__icontains=country)
            all_state_sellers = IndividualInvestor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                 all_state__icontains=state,
                                                                 all_country__icontains=country).exclude(all_city__icontains=city)
            all_country_sellers = IndividualInvestor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                  all_country__icontains=country).exclude(
                                                                all_state__icontains=state)
            other_country_sellers = IndividualInvestor.objects.filter(all_category__icontains=category,
                                                                      about_seller=type).exclude(
                                    all_country__icontains=country)
            same_country_sellers = IndividualInvestor.objects.filter(all_country__icontains=country,
                                                                      about_seller=type).exclude(
                all_category__icontains=category)
            other_sellers = IndividualInvestor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country).exclude(all_category__icontains=category)
            result_list_city = list(chain(all_city_sellers, all_state_sellers, all_country_sellers, other_country_sellers, same_country_sellers, other_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data


        if state !='' and base_type=='Individual':
            # all_city_sellers = IndividualInvestor.objects.filter(all_category__icontains=category, about_seller=type,
            #                                                      all_city__icontains=city, all_state__icontains=state,
            #                                                      all_country__icontains=country)
            all_state_sellers = IndividualInvestor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                  all_state__icontains=state,
                                                                  all_country__icontains=country)
            all_country_sellers = IndividualInvestor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                    all_country__icontains=country).exclude(all_state__icontains=state)
            other_country_sellers = IndividualInvestor.objects.filter(all_category__icontains=category,
                                                                      about_seller=type).exclude(
                                                    all_country__icontains=country)
            same_country_sellers = IndividualInvestor.objects.filter(all_country__icontains=country,
                                                                     about_seller=type).exclude(
                                    all_category__icontains=category)
            other_sellers = IndividualInvestor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country).exclude(all_category__icontains=category)
            result_list_city = list(
                chain(all_state_sellers, all_country_sellers, other_country_sellers,
                      same_country_sellers, other_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data

        if country !='' and base_type=='Individual':
            # all_city_sellers = IndividualInvestor.objects.filter(all_category__icontains=category, about_seller=type,
            #                                                      all_city__icontains=city, all_state__icontains=state,
            #                                                      all_country__icontains=country)
            # all_state_sellers = IndividualInvestor.objects.filter(all_category__icontains=category, about_seller=type,
            #                                                       all_state__icontains=state,
            #                                                       all_country__icontains=country)
            all_country_sellers = IndividualInvestor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                    all_country__icontains=country)
            other_country_sellers = IndividualInvestor.objects.filter(all_category__icontains=category,
                                                                      about_seller=type).exclude(
                                                                    all_country__icontains=country)
            same_country_sellers = IndividualInvestor.objects.filter(all_country__icontains=country,
                                                                     about_seller=type).exclude(
                                                                    all_category__icontains=category)
            other_sellers = IndividualInvestor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country).exclude(all_category__icontains=category)
            result_list_city = list(
                chain(all_country_sellers, other_country_sellers,
                      same_country_sellers, other_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if base_type=='Individual':
            other_sellers = IndividualInvestor.objects.filter(about_seller=type, all_category__icontains=category)
            category_sellers = IndividualInvestor.objects.filter(about_seller=type).exclude(all_category__icontains=category)
            result_list_city = list(
                chain(other_sellers, category_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if city != '' and base_type == 'Company':
            all_city_sellers = CompanyInvestor.objects.filter(all_category__icontains=category, about_seller=type,
                                                              all_city__icontains=city, all_state__icontains=state,
                                                              all_country__icontains=country)
            all_state_sellers = CompanyInvestor.objects.filter(all_category__icontains=category, about_seller=type,
                                                               all_state__icontains=state,
                                                               all_country__icontains=country).exclude(
                all_city__icontains=city)
            all_country_sellers = CompanyInvestor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                 all_country__icontains=country).exclude(
                all_state__icontains=state)
            other_country_sellers = CompanyInvestor.objects.filter(all_category__icontains=category,
                                                                   about_seller=type).exclude(
                all_country__icontains=country)
            same_country_sellers = CompanyInvestor.objects.filter(all_country__icontains=country,
                                                                  about_seller=type).exclude(
                all_category__icontains=category)
            other_sellers = CompanyInvestor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country).exclude(all_category__icontains=category)
            result_list_city = list(
                chain(all_city_sellers, all_state_sellers, all_country_sellers, other_country_sellers,
                      same_country_sellers,
                      other_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data

        if state != '' and base_type == 'Company':
            # all_city_sellers = CompanyInvestor.objects.filter(all_category__icontains=category, about_seller=type,
            #                                                      all_city__icontains=city, all_state__icontains=state,
            #                                                      all_country__icontains=country)
            all_state_sellers = CompanyInvestor.objects.filter(all_category__icontains=category, about_seller=type,
                                                               all_state__icontains=state,
                                                               all_country__icontains=country)
            all_country_sellers = CompanyInvestor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                 all_country__icontains=country).exclude(
                all_state__icontains=state)
            other_country_sellers = CompanyInvestor.objects.filter(all_category__icontains=category,
                                                                   about_seller=type).exclude(
                all_country__icontains=country)
            same_country_sellers = CompanyInvestor.objects.filter(all_country__icontains=country,
                                                                  about_seller=type).exclude(
                all_category__icontains=category)
            other_sellers = CompanyInvestor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country).exclude(all_category__icontains=category)
            result_list_city = list(
                chain(all_state_sellers, all_country_sellers, other_country_sellers,
                      same_country_sellers, other_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data

        if country != '' and base_type == 'Company':
            # all_city_sellers = CompanyInvestor.objects.filter(all_category__icontains=category, about_seller=type,
            #                                                      all_city__icontains=city, all_state__icontains=state,
            #                                                      all_country__icontains=country)
            # all_state_sellers = CompanyInvestor.objects.filter(all_category__icontains=category, about_seller=type,
            #                                                       all_state__icontains=state,
            #                                                       all_country__icontains=country)
            all_country_sellers = CompanyInvestor.objects.filter(all_category__icontains=category, about_seller=type,
                                                                 all_country__icontains=country)
            other_country_sellers = CompanyInvestor.objects.filter(all_category__icontains=category,
                                                                   about_seller=type).exclude(
                all_country__icontains=country)
            same_country_sellers = CompanyInvestor.objects.filter(all_country__icontains=country,
                                                                  about_seller=type).exclude(
                all_category__icontains=category)
            other_sellers = CompanyInvestor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country).exclude(all_category__icontains=category)
            result_list_city = list(
                chain(all_country_sellers, other_country_sellers,
                      same_country_sellers, other_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if base_type == 'Company':
            print('inside investor Company ')
            other_sellers = CompanyInvestor.objects.filter(about_seller=type, all_category__icontains=category)
            category_sellers = CompanyInvestor.objects.filter(about_seller=type).exclude(all_category__icontains=category)
            result_list_city = list(
                chain(other_sellers, category_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
    else:
        if city !='' and base_type=='Company':
            all_city_sellers = CompanyInvestor.objects.filter(about_seller=type,
                                                              all_city__icontains=city, all_state__icontains=state,
                                                              all_country__icontains=country)
            all_state_sellers = CompanyInvestor.objects.filter(about_seller=type,
                                                               all_state__icontains=state,
                                                               all_country__icontains=country).exclude(
                all_city__icontains=city)
            all_country_sellers = CompanyInvestor.objects.filter(about_seller=type,
                                                                 all_country__icontains=country).exclude(
                all_state__icontains=state)
            other_country_sellers = CompanyInvestor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country)
            # same_country_sellers = CompanyInvestor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state)
            # other_sellers = CompanyInvestor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(all_city_sellers, all_state_sellers, all_country_sellers, other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if state !='' and base_type=='Company':
            # all_city_sellers = CompanyInvestor.objects.filter(about_seller=type,
            #                                                   all_city__icontains=city, all_state__icontains=state,
            #                                                   all_country__icontains=country)
            all_state_sellers = CompanyInvestor.objects.filter(about_seller=type,
                                                               all_state__icontains=state,
                                                               all_country__icontains=country)
            all_country_sellers = CompanyInvestor.objects.filter(about_seller=type,
                                                                 all_country__icontains=country).exclude(
                                                                    all_state__icontains=state)
            other_country_sellers = CompanyInvestor.objects.filter(about_seller=type).exclude(
                                        all_country__icontains=country)
            # same_country_sellers = CompanyInvestor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #                                                         all_state__icontains=state)
            # other_sellers = CompanyInvestor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(all_state_sellers, all_country_sellers, other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if country !='' and base_type=='Company':
            # all_city_sellers = CompanyInvestor.objects.filter(about_seller=type,
            #                                                   all_city__icontains=city, all_state__icontains=state,
            #                                                   all_country__icontains=country)
            # all_state_sellers = CompanyInvestor.objects.filter(about_seller=type,
            #                                                    all_state__icontains=state,
            #                                                    all_country__icontains=country)
            all_country_sellers = CompanyInvestor.objects.filter(about_seller=type,
                                                                 all_country__icontains=country)
            other_country_sellers = CompanyInvestor.objects.filter(about_seller=type).exclude(
                                                                    all_country__icontains=country)
            # same_country_sellers = CompanyInvestor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #                                                         all_state__icontains=state)
            # other_sellers = CompanyInvestor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(all_country_sellers, other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if base_type=='Company':
            other_country_sellers = CompanyInvestor.objects.filter(about_seller=type)
            # same_country_sellers = CompanyInvestor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #                                                         all_state__icontains=state)
            # other_sellers = CompanyInvestor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if city != '' and base_type == 'Individual':
            all_city_sellers = IndividualInvestor.objects.filter(about_seller=type,
                                                                 all_city__icontains=city, all_state__icontains=state,
                                                                 all_country__icontains=country)
            all_state_sellers = IndividualInvestor.objects.filter(about_seller=type,
                                                                  all_state__icontains=state,
                                                                  all_country__icontains=country).exclude(
                all_city__icontains=city)
            all_country_sellers = IndividualInvestor.objects.filter(about_seller=type,
                                                                    all_country__icontains=country).exclude(
                all_state__icontains=state)
            other_country_sellers = IndividualInvestor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country)
            # same_country_sellers = IndividualInvestor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state)
            # other_sellers = IndividualInvestor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(all_city_sellers, all_state_sellers, all_country_sellers, other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if state != '' and base_type == 'Individual':
            # all_city_sellers = IndividualInvestor.objects.filter(about_seller=type,
            #                                                   all_city__icontains=city, all_state__icontains=state,
            #                                                   all_country__icontains=country)
            all_state_sellers = IndividualInvestor.objects.filter(about_seller=type,
                                                                  all_state__icontains=state,
                                                                  all_country__icontains=country)
            all_country_sellers = IndividualInvestor.objects.filter(about_seller=type,
                                                                    all_country__icontains=country).exclude(
                all_state__icontains=state)
            other_country_sellers = IndividualInvestor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country)
            # same_country_sellers = IndividualInvestor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #                                                         all_state__icontains=state)
            # other_sellers = IndividualInvestor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(all_state_sellers, all_country_sellers, other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if country != '' and base_type == 'Individual':
            # all_city_sellers = IndividualInvestor.objects.filter(about_seller=type,
            #                                                   all_city__icontains=city, all_state__icontains=state,
            #                                                   all_country__icontains=country)
            # all_state_sellers = IndividualInvestor.objects.filter(about_seller=type,
            #                                                    all_state__icontains=state,
            #                                                    all_country__icontains=country)
            all_country_sellers = IndividualInvestor.objects.filter(about_seller=type,
                                                                    all_country__icontains=country)
            other_country_sellers = IndividualInvestor.objects.filter(about_seller=type).exclude(
                all_country__icontains=country)
            # same_country_sellers = IndividualInvestor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #                                                         all_state__icontains=state)
            # other_sellers = IndividualInvestor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(all_country_sellers, other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data
        if base_type == 'Individual':
            other_country_sellers = IndividualInvestor.objects.filter(about_seller=type)
            # same_country_sellers = IndividualInvestor.objects.filter(all_country__icontains=country,
            #                                                       about_seller=type).exclude(
            #                                                         all_state__icontains=state)
            # other_sellers = IndividualInvestor.objects.filter(about_seller=type).exclude(
            #     all_city__icontains=city, all_state__icontains=state, all_country__icontains=country)
            result_list_city = list(
                chain(other_country_sellers))
            print(result_list_city)
            data = {}
            data['all_city_sellers'] = result_list_city
            return data

        # if sub_category != '' and base_type == 'Individual':
        #     all_city_sellers = IndividualInvestor.objects.filter(category1=category, about_seller=type,
        #                                                       sub_category1=sub_category)
        #
        #     all_city_advisor1 = IndividualInvestor.objects.filter(category2=category, about_seller=type,
        #                                                        sub_category2=sub_category)
        #
        #     all_city_advisor2 = IndividualInvestor.objects.filter(category3=category, about_seller=type,
        #                                                        sub_category3=sub_category)
        #
        #     result_list_city_2 = list(chain(all_city_sellers, all_city_advisor1, all_city_advisor2))
        #     print(result_list_city_2)
        #     data = {}
        #     data['all_city_sellers'] = result_list_city_2
        #     return data





    result_list_city_2 = []
    if sub_category == '' and base_type=='Company':
        all_city_sellers = CompanyInvestor.objects.filter(category1=category, about_seller=type)

        all_city_advisor1 = CompanyInvestor.objects.filter(category2=category, about_seller=type)

        all_city_advisor2 = CompanyInvestor.objects.filter(category3=category, about_seller=type)

        result_list_city_2 = list(chain(all_city_sellers, all_city_advisor1, all_city_advisor2))
        print(result_list_city_2)
        data = {}
        data['all_city_sellers'] = result_list_city_2
        return data

    if city != '' and base_type=='Company':
        all_city_sellers = CompanyInvestor.objects.filter(category1=category, about_seller=type, sub_category1=sub_category,
                                                  country1=country,
                                                          state1=state, city1=city)
        all_city_advisor1 = CompanyInvestor.objects.filter(category2=category, about_seller=type, sub_category2=sub_category,
                                                    country1=country,
                                                    state1=state, city1=city)
        all_city_advisor2 = CompanyInvestor.objects.filter(category3=category, about_seller=type, sub_category3=sub_category,
                                                    country1=country,
                                                    state1=state, city1=city)
        all_city_sellers_ad2 = CompanyInvestor.objects.filter(category1=category, about_seller=type, sub_category1=sub_category,
                                                          country2=country,
                                                          state2=state, city2=city)
        all_city_advisor1_ad2 = CompanyInvestor.objects.filter(category2=category, about_seller=type,
                                                           sub_category2=sub_category,
                                                           country2=country,
                                                           state2=state, city2=city)
        all_city_advisor2_ad2 = CompanyInvestor.objects.filter(category3=category, about_seller=type,
                                                           sub_category3=sub_category,
                                                           country2=country,
                                                           state2=state, city2=city)
        all_city_sellers_ad3 = CompanyInvestor.objects.filter(category1=category, about_seller=type,
                                                              sub_category1=sub_category,
                                                              country3=country,
                                                              state3=state, city3=city)
        all_city_advisor1_ad3 = CompanyInvestor.objects.filter(category2=category, about_seller=type,
                                                               sub_category2=sub_category,
                                                               country3=country,
                                                               state3=state, city3=city)
        all_city_advisor2_ad3 = CompanyInvestor.objects.filter(category3=category, about_seller=type,
                                                               sub_category3=sub_category,
                                                               country3=country,
                                                               state3=state, city3=city)

        result_list_city_2 = list(chain(all_city_sellers, all_city_advisor1, all_city_advisor2, all_city_sellers_ad2, all_city_advisor2_ad2, all_city_advisor1_ad2, all_city_sellers_ad3, all_city_advisor1_ad3, all_city_advisor2_ad3))
        print(result_list_city_2)
        data = {}
        data['all_city_sellers'] = result_list_city_2
        return data

    if state != '' and base_type == 'Company':
        all_city_sellers = CompanyInvestor.objects.filter(category1=category, about_seller=type,
                                                          sub_category1=sub_category,
                                                          country1=country,
                                                          state1=state)
        all_city_advisor1 = CompanyInvestor.objects.filter(category2=category, about_seller=type,
                                                           sub_category2=sub_category,
                                                           country1=country,
                                                           state1=state)
        all_city_advisor2 = CompanyInvestor.objects.filter(category3=category, about_seller=type,
                                                           sub_category3=sub_category,
                                                           country1=country,
                                                           state1=state)
        all_city_sellers_ad2 = CompanyInvestor.objects.filter(category1=category, about_seller=type,
                                                              sub_category1=sub_category,
                                                              country2=country,
                                                              state2=state)
        all_city_advisor1_ad2 = CompanyInvestor.objects.filter(category2=category, about_seller=type,
                                                               sub_category2=sub_category,
                                                               country2=country,
                                                               state2=state)
        all_city_advisor2_ad2 = CompanyInvestor.objects.filter(category3=category, about_seller=type,
                                                               sub_category3=sub_category,
                                                               country2=country,
                                                               state2=state)
        all_city_sellers_ad3 = CompanyInvestor.objects.filter(category1=category, about_seller=type,
                                                              sub_category1=sub_category,
                                                              country3=country,
                                                              state3=state)
        all_city_advisor1_ad3 = CompanyInvestor.objects.filter(category2=category, about_seller=type,
                                                               sub_category2=sub_category,
                                                               country3=country,
                                                               state3=state)
        all_city_advisor2_ad3 = CompanyInvestor.objects.filter(category3=category, about_seller=type,
                                                               sub_category3=sub_category,
                                                               country3=country,
                                                               state3=state)
        result_list_city_2 = list(
            chain(all_city_sellers, all_city_advisor1, all_city_advisor2, all_city_sellers_ad2, all_city_advisor2_ad2,
                  all_city_advisor1_ad2, all_city_sellers_ad3, all_city_advisor1_ad3, all_city_advisor2_ad3))
        print(result_list_city_2)
        data = {}
        data['all_city_sellers'] = result_list_city_2
        return data

    if country != '' and base_type == 'Company':
        all_city_sellers = CompanyInvestor.objects.filter(category1=category, about_seller=type,
                                                          sub_category1=sub_category,
                                                          country1=country,
                                                          )
        all_city_advisor1 = CompanyInvestor.objects.filter(category2=category, about_seller=type,
                                                           sub_category2=sub_category,
                                                           country1=country,
                                                           )
        all_city_advisor2 = CompanyInvestor.objects.filter(category3=category, about_seller=type,
                                                           sub_category3=sub_category,
                                                           country1=country,
                                                           )
        all_city_sellers_ad2 = CompanyInvestor.objects.filter(category1=category, about_seller=type,
                                                              sub_category1=sub_category,
                                                              country2=country,
                                                              )
        all_city_advisor1_ad2 = CompanyInvestor.objects.filter(category2=category, about_seller=type,
                                                               sub_category2=sub_category,
                                                               country2=country,
                                                               )
        all_city_advisor2_ad2 = CompanyInvestor.objects.filter(category3=category, about_seller=type,
                                                               sub_category3=sub_category,
                                                               country2=country,
                                                               )
        all_city_sellers_ad3 = CompanyInvestor.objects.filter(category1=category, about_seller=type,
                                                              sub_category1=sub_category,
                                                              country3=country,
                                                              )
        all_city_advisor1_ad3 = CompanyInvestor.objects.filter(category2=category, about_seller=type,
                                                               sub_category2=sub_category,
                                                               country3=country,
                                                               )
        all_city_advisor2_ad3 = CompanyInvestor.objects.filter(category3=category, about_seller=type,
                                                               sub_category3=sub_category,
                                                               country3=country,
                                                               )
        result_list_city_2 = list(
            chain(all_city_sellers, all_city_advisor1, all_city_advisor2, all_city_sellers_ad2, all_city_advisor2_ad2,
                  all_city_advisor1_ad2, all_city_sellers_ad3, all_city_advisor1_ad3, all_city_advisor2_ad3))
        print(result_list_city_2)
        data = {}
        data['all_city_sellers'] = result_list_city_2
        return data

    if sub_category != '' and base_type == 'Company':
        all_city_sellers = CompanyInvestor.objects.filter(category1=category, about_seller=type,
                                                          sub_category1=sub_category)

        all_city_advisor1 = CompanyInvestor.objects.filter(category2=category, about_seller=type,
                                                           sub_category2=sub_category)

        all_city_advisor2 = CompanyInvestor.objects.filter(category3=category, about_seller=type,
                                                           sub_category3=sub_category)

        result_list_city_2 = list(chain(all_city_sellers, all_city_advisor1, all_city_advisor2))
        print(result_list_city_2)
        data = {}
        data['all_city_sellers'] = result_list_city_2
        return data




    final_result = []
    final_result.append(result_list_city)
    final_result.append(result_list_city_2)
    # print(all_sub_sellers)
    # print(all_country_sellers)
    # print(all_state_sellers)
    print(result_list_city)
    data = {}
    # data['all_sellers']=all_sellers
    # data['all_sub_sellers'] = all_sub_sellers
    # data['all_country_sellers']=result_list_country
    # data['all_state_sellers']=result_list_state
    data['all_city_sellers']=final_result
    return data


def search_dict(request, business_id):
    seller = Seller1.objects.get(business_id=business_id)
    type = seller.type
    print(type)
    smodel = model_list[type].objects.get(seller=seller)
    sserializer = serializer_list[type](smodel)
    sdata = sserializer.data
    serializer = SellerSerializer(seller)
    data = serializer.data
    cdata = data.copy()
    # cdata.update(sdata)
    main_album_id = seller.album_id
    main_album = KAlbumForFile(album_id=main_album_id)
    main_files = main_album.files.all()
    srevenue = None
    rdata = None
    try:
        srevenue = RevenueModel.objects.get(seller=seller)
        rserializer = RevenueModelSerializer(srevenue)
        rdata = rserializer.data
        cdata.update(rdata)
    except:
        print('no revenue')
    # jdata = json.load(cdata)
    fdata = {}
    fdata['seller']=cdata
    fdata['business']=sdata
    fdata['rating']=8.5
    fdata['images'] = []
    for file in main_files:
        name = file.name
        name_dict = {
            'file_name': name
        }
        fdata['images'].append(name_dict)
    fdata['same']='False'
    fdata['investor'] = 'False'
    try:
        user = request.user
        sells_all = user.profile.user_sell.all()
        sell_arr=[]
        for sell_1 in sells_all:
            sell_arr.append(sell_1.seller)
        for xseller in sell_arr:
            if xseller == seller:
                fdata['same'] = 'True'
            if user.profile.invest_type is not None:
                fdata['investor'] = 'True'
    except:
        pass
    print(fdata)
    return fdata


def search_dict_advise(request, business_id):
    seller = Advisor.objects.get(advisor_id=business_id)
    type = seller.type
    smodel = adv_model_list[type].objects.get(advisor=seller)
    sserializer = adv_serializer_list[type](smodel)
    sdata = sserializer.data
    serializer = AdvisorSerializer(seller)
    data = serializer.data
    cdata = data.copy()
    # cdata.update(sdata)
    main_album_id = seller.album_id
    main_album = KAlbumForFile(album_id=main_album_id)
    main_files = main_album.files.all()
    srevenue = None
    rdata = None
    # try:
    #     srevenue = RevenueModel.objects.get(seller=seller)
    #     rserializer = RevenueModelSerializer(srevenue)
    #     rdata = rserializer.data
    #     cdata.update(rdata)
    # except:
    #     print('no revenue')
    # jdata = json.load(cdata)
    fdata = {}
    fdata['advisor']=cdata
    fdata['business']=sdata

    fdata['images'] = []
    for file in main_files:
        name = file.name
        name_dict = {
            'file_name': name
        }
        fdata['images'].append(name_dict)
    fdata['same']='False'
    fdata['investor'] = 'False'
    # try:
    #     user = request.user
    #     for xseller in user.profile.sell_type.all():
    #         if xseller == seller:
    #             fdata['same'] = 'True'
    #         if user.profile.invest_type is not None:
    #             fdata['investor'] = 'True'
    # except:
    #     pass
    print(fdata)
    return fdata



def search_dict_invest(request, business_id):
    seller = Investor.objects.get(investor_id=business_id)
    type = seller.type
    smodel = inv_model_list[type].objects.get(investor=seller)
    sserializer = inv_serializer_list[type](smodel)
    sdata = sserializer.data
    serializer = InvestorSerializer(seller)
    data = serializer.data
    cdata = data.copy()
    # cdata.update(sdata)
    main_album_id = seller.album_id
    main_album = KAlbumForFile(album_id=main_album_id)
    main_files = main_album.files.all()
    srevenue = None
    rdata = None
    # try:
    #     srevenue = RevenueModel.objects.get(seller=seller)
    #     rserializer = RevenueModelSerializer(srevenue)
    #     rdata = rserializer.data
    #     cdata.update(rdata)
    # except:
    #     print('no revenue')
    # jdata = json.load(cdata)
    fdata = {}
    fdata['investor']=cdata
    fdata['business']=sdata

    fdata['images'] = []
    for file in main_files:
        name = file.name
        name_dict = {
            'file_name': name
        }
        fdata['images'].append(name_dict)
    # fdata['same']='False'
    # fdata['investor'] = 'False'
    # try:
    #     user = request.user
    #     for xseller in user.profile.sell_type.all():
    #         if xseller == seller:
    #             fdata['same'] = 'True'
    #         if user.profile.invest_type is not None:
    #             fdata['investor'] = 'True'
    # except:
    #     pass
    print('output of search dict invest')
    print(fdata)
    return fdata

@login_required(login_url='profiles:index')
def show_sellers(request):
    if request.method == 'GET':
        # print(request.GET)
        category = request.GET['category']
        sub_category = request.GET['sub_category']
        country = request.GET['country']
        state = request.GET['state']
        city = request.GET['city']
        type = request.GET['type']
        page = request.GET['page']
        # base_type = request.GET['base_type']
        # print(country)
        # print(category)
        # print(sub_category)
        # print(city)
        # print(state)
        # print(type)
        user=request.user
        search = Search_log()
        search.city=city
        search.state=state
        search.country=country
        search.type=type
        search.base_type='Seller'
        search.save()
        user.profile.searches.add(search)
        user.save()
        data = get_models_by_category(type=type, category=category, sub_category=sub_category, country=country, city=city, state=state)
        sellers = None

        # if len(data['all_city_sellers'])==0 :
            # print('some sellers in city')
            # if len(data['all_state_sellers'])==0 :
            #     print('entered state')
            #     if len(data['all_country_sellers']) == 0:

            #         if len(data['all_sub_sellers']) == 0:
            #             sellers = data['all_sellers']
            #             print('entered')
            #             print(sellers)
            #         else:
            #             sellers = data['all_sub_sellers']

            #             print('entered sub')
            #             print(sellers)


            #     else:
            #         sellers = data['all_country_sellers']
            # else:
            #     sellers = data['all_state_sellers']
        # else:
        sellers = data['all_city_sellers']
        # print(sellers)
        fdata = []
        for seller in sellers:
            business_id = seller.business_id
            dict = search_dict(request=request, business_id=business_id)
            if dict['same']=='False':
                fdata.append(dict)

        # print(fdata)
        page_fdata = Paginator(fdata, 10)
        page_dict ={
            'pages':page_fdata.num_pages
        }
        ffdata={}
        ffdata['sellers'] = page_fdata.get_page(page).object_list

        ffdata['pages']= page_fdata.num_pages
        # print(page_fdata.num_pages)
        # print(ffdata['pages'])
        # print(ffdata)
        # jdata = json.dumps(ffdata)
        return JsonResponse(ffdata, safe=False)

@login_required(login_url='profiles:index')
def show_advisors(request):
    if request.method == 'GET':
        print(request.GET)
        category = request.GET['category']
        sub_category = request.GET['sub_category']
        country = request.GET['country']
        state = request.GET['state']
        city = request.GET['city']
        type = request.GET['type']
        page = request.GET['page']
        # skill = request.GET['skill']
        print(country)
        print(category)
        print(sub_category)
        print(city)
        print(state)
        print(type)
        user = request.user
        search = Search_log()
        search.city = city
        search.state = state
        search.country = country
        search.type = type
        search.base_type = 'Business_Advisor'
        search.save()
        user.profile.searches.add(search)
        user.save()
        data = get_models_by_category_advise(type=type, category=category, sub_category=sub_category, country=country, city=city, state=state)
        sellers = None
        # if len(data['all_city_sellers'])==0 :
        #     print('some sellers in city')
        #     if len(data['all_state_sellers'])==0 :
        #         sellers = data['all_country_sellers']
        #     else:
        #         sellers = data['all_state_sellers']
        # else:
        sellers = data['all_city_sellers']
        print(sellers)
        fdata = []
        for seller in sellers:
            business_id = seller.advisor_id
            dict = search_dict_advise(request=request, business_id=business_id)
            fdata.append(dict)
        print(fdata)
        page_fdata = Paginator(fdata, 20)
        page_dict ={
            'pages':page_fdata.num_pages
        }
        ffdata={}
        ffdata['sellers'] = page_fdata.get_page(page).object_list

        ffdata['pages']= page_fdata.num_pages
        print(page_fdata.num_pages)
        print(ffdata['pages'])
        print(ffdata)
        # jdata = json.dumps(ffdata)
        return JsonResponse(ffdata, safe=False)

@login_required(login_url='profiles:index')
def show_advisors_startup(request):
    if request.method == 'GET':
        print(request.GET)
        category = request.GET['category']
        sub_category = request.GET['sub_category']
        country = request.GET['country']
        state = request.GET['state']
        city = request.GET['city']
        type = request.GET['type']
        page = request.GET['page']
        # skill = request.GET['skill']
        print(country)
        print(category)
        print(sub_category)
        print(city)
        print(state)
        print(type)
        user = request.user
        search = Search_log()
        search.city = city
        search.state = state
        search.country = country
        search.type = type
        search.base_type = 'Startup_Advisor'
        search.save()
        user.profile.searches.add(search)
        user.save()
        data = get_models_by_category_advise_startup(type=type, category=category, sub_category=sub_category, country=country, city=city, state=state)
        sellers = None

        sellers = data['all_city_sellers']
        print(sellers)
        fdata = []
        for seller in sellers:
            business_id = seller.advisor_id
            dict = search_dict_advise(request=request, business_id=business_id)
            fdata.append(dict)
        print(fdata)
        page_fdata = Paginator(fdata, 20)
        page_dict ={
            'pages':page_fdata.num_pages
        }
        ffdata={}
        ffdata['sellers'] = page_fdata.get_page(page).object_list

        ffdata['pages']= page_fdata.num_pages
        print(page_fdata.num_pages)
        print(ffdata['pages'])
        print(ffdata)
        # jdata = json.dumps(ffdata)
        return JsonResponse(ffdata, safe=False)

@login_required(login_url='profiles:index')
def show_investors(request):
    if request.method == 'GET':
        print(request.GET)
        category = request.GET['category']
        sub_category = request.GET['sub_category']
        country = request.GET['country']
        state = request.GET['state']
        city = request.GET['city']
        type = request.GET['type']
        page = request.GET['page']
        # skill = request.GET['skill']
        print(country)
        print(category)
        print(sub_category)
        print(city)
        print(state)
        print(type)
        user = request.user
        search = Search_log()
        search.city = city
        search.state = state
        search.country = country
        search.type = type
        search.base_type = 'Investor'
        search.save()
        user.profile.searches.add(search)
        user.save()
        data = get_models_by_category_invest(type=type, category=category, sub_category=sub_category, country=country, city=city, state=state, base_type=request.GET['base_type'])
        sellers = None

        sellers = data['all_city_sellers']
        print(sellers)
        fdata = []
        for seller in sellers:
            business_id = seller.investor_id
            print(business_id)
            dict = search_dict_invest(request=request, business_id=business_id)
            fdata.append(dict)
        print(fdata)
        page_fdata = Paginator(fdata, 20)
        page_dict ={
            'pages':page_fdata.num_pages
        }
        ffdata={}
        ffdata['sellers'] = page_fdata.get_page(page).object_list

        ffdata['pages']= page_fdata.num_pages
        print(page_fdata.num_pages)
        print(ffdata['pages'])
        print(ffdata)
        # jdata = json.dumps(ffdata)
        return JsonResponse(ffdata, safe=False)

@login_required(login_url='profiles:index')
def display_busi(request):
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    user = request.user
    investor = user.profile.user_invest.all()
    iserializer = None
    # invest = None
    all_isell = {}
    # if investor is not None:
    #     iserializer=InvestorSerializer(investor)
    #     invest = Invest.objects.get(investor=investor)
    #     invest_sell = invest.cart_seller.all()
    #     all_isell= SellerSerializer(invest_sell, many=True).data
    data_investor = []
    for invest in investor:
        iserializer = InvestorSerializer(invest.investor).data
        data_investor.append(iserializer)
        iname = 'investor_' + str(invest.investor.investor_id)
        all_isell[iname] = SellerSerializer(invest.cart_seller.all(), many=True).data
    # if iserializer is not None:
    #     data_investor=iserializer.data
    #     exist = {
    #         'exist': 'True'
    #     }
    #     cdata = data_investor.copy()
    #     cdata.update(exist)
    #     data_investor=cdata
    # else:
    #     data_investor={
    #         'exist':'False'
    #     }
    sellers = user.profile.sell_type.all()
    data_sellers = []
    if sellers is not None:
        data_sellers = SellerSerializer(sellers, many=True).data
    # print(data_sellers)
    data_advisors = []

    advisors = user.profile.user_advise.all()
    for advisor in advisors:
        asreializer = AdvisorSerializer(advisor.advisor)
        data_advisors.append(asreializer.data)
    # if advisors is not None:
    #     data_advisors= AdvisorSerializer(advisors, many=True)
    # print(data_advisors)
    just_sell = user.profile.just_sell.all()
    all_jsell=[]
    all_jsell = SellerSerializer(just_sell, many=True).data
    his_sell = user.profile.user_sell.all()
    all_hsell = []
    all_supsell=[]
    all_sup_sell = []
    for sell in his_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data
        all_hsell.append(dseller)
        if sell_seller.type=='Supplier':
            all_supsell.append(dseller)
            all_sup_sell.append(sell)
    advises = user.profile.user_advise.all()
    all_sup_sellers={}
    for sell in all_sup_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data

        sell_advisors = sell.cart_sellers.all()
        name = 'seller_' + str(sell_seller.business_id)
        all_sup_sellers[name]=[]
        for one_advisor in sell_advisors:
            done_advisor = SellerSerializer(one_advisor).data
            all_sup_sellers[name].append(done_advisor)
    all_aisell={}
    all_aisell['startup']={}
    all_aisell['business']={}
    for advise in advises:
        if advise.type == 'Startup':
            aname='advisor_'+str(advise.advisor.advisor_id)
            all_aisell['startup'][aname]=SellerSerializer(advise.cart_seller, many=True).data
        if advise.type == 'Business':
            aname = 'advisor_' + str(advise.advisor.advisor_id)
            all_aisell['business'][aname]=SellerSerializer(advise.cart_seller, many=True).data
    category=''
    sub_category=''
    city = ''
    state = ''
    country = ''
    type='Business'
    try:
        category=request.GET['category']
    except:
        pass
    # try:
    #     sub_category = request.GET['sub_category']
    # except:
    #     pass
    try:
        city = request.GET['city']
    except:
        pass
    try:
        state = request.GET['state']
    except:
        pass
    try:
        country = request.GET['country']
    except:
        pass
    try:
        type=request.GET['type']
    except:
        pass


    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'code_data': code_data,
        'year_data': yeardata,
        'data_investor': json.dumps(data_investor),
        'data_sellers':data_sellers,
        'data_advisors':json.dumps(data_advisors),
        'just_sellers': json.dumps(all_jsell),
        'advise_sellers': json.dumps(all_aisell),
        'invest_sellers': json.dumps(all_isell),
        'my_sellers': json.dumps(all_hsell),
        'sup_sellers': json.dumps(all_supsell),
        'seller_sup_sellers': json.dumps(all_sup_sellers),
        'category': category,
        'sub_category': sub_category,
        'city': city,
        'state': state,
        'country': country,
        'type': type,
    }
    # print(context['data_investor'])
    # print(context['just_sellers'])
    # print(context['advise_sellers'])
    # print(context['invest_sellers'])
    # print(context['my_sellers'])
    return render(request, 'seller1/display_busi.html', context)

@login_required(login_url='profiles:index')
def display_web(request):
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    user = request.user
    investor = user.profile.user_invest.all()
    iserializer = None
    # invest = None
    all_isell = {}
    # if investor is not None:
    #     iserializer=InvestorSerializer(investor)
    #     invest = Invest.objects.get(investor=investor)
    #     invest_sell = invest.cart_seller.all()
    #     all_isell= SellerSerializer(invest_sell, many=True).data
    data_investor = []
    for invest in investor:
        iserializer = InvestorSerializer(invest.investor).data
        data_investor.append(iserializer)
        iname = 'investor_' + str(invest.investor.investor_id)
        all_isell[iname] = SellerSerializer(invest.cart_seller.all(), many=True).data
    # data_investor = None
    # if iserializer is not None:
    #     data_investor=iserializer.data
    #     exist = {
    #         'exist': 'True'
    #     }
    #     cdata = data_investor.copy()
    #     cdata.update(exist)
    #     data_investor=cdata
    # else:
    #     data_investor={
    #         'exist':'False'
    #     }
    sellers = user.profile.sell_type.all()
    data_sellers = []
    if sellers is not None:
        data_sellers = SellerSerializer(sellers, many=True).data
    print(data_sellers)
    data_advisors = []

    advisors = user.profile.user_advise.all()
    for advisor in advisors:
        asreializer = AdvisorSerializer(advisor.advisor)
        data_advisors.append(asreializer.data)
    # if advisors is not None:
    #     data_advisors= AdvisorSerializer(advisors, many=True)
    print(data_advisors)
    just_sell = user.profile.just_sell.all()
    all_jsell=[]
    all_jsell = SellerSerializer(just_sell, many=True).data
    his_sell = user.profile.user_sell.all()
    all_hsell = []
    all_supsell = []
    all_sup_sell = []
    for sell in his_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data
        all_hsell.append(dseller)
        if sell_seller.type == 'Supplier':
            all_supsell.append(dseller)
            all_sup_sell.append(sell)
    advises = user.profile.user_advise.all()
    all_sup_sellers = {}
    for sell in all_sup_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data

        sell_advisors = sell.cart_sellers.all()
        name = 'seller_' + str(sell_seller.business_id)
        all_sup_sellers[name] = []
        for one_advisor in sell_advisors:
            done_advisor = SellerSerializer(one_advisor).data
            all_sup_sellers[name].append(done_advisor)
    all_aisell={}
    all_aisell['startup']={}
    all_aisell['business']={}
    for advise in advises:
        if advise.type == 'Startup':
            aname='advisor_'+str(advise.advisor.advisor_id)
            all_aisell['startup'][aname]=SellerSerializer(advise.cart_seller, many=True).data
        if advise.type == 'Business':
            aname = 'advisor_' + str(advise.advisor.advisor_id)
            all_aisell['business'][aname]=SellerSerializer(advise.cart_seller, many=True).data

    category = ''
    sub_category = ''
    city = ''
    state = ''
    country = ''
    type = 'Application'
    try:
        type = request.GET['type']
        category = request.GET['category']
        # sub_category = request.GET['sub_category']
        city = request.GET['city']
        state = request.GET['state']
        country = request.GET['country']

    except:
        pass


    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'code_data': code_data,
        'year_data': yeardata,
        'data_investor': json.dumps(data_investor),
        # 'data_sellers':data_sellers,
        'data_advisors':json.dumps(data_advisors),
        'just_sellers': json.dumps(all_jsell),
        'advise_sellers': json.dumps(all_aisell),
        'invest_sellers': json.dumps(all_isell),
        'my_sellers': json.dumps(all_hsell),
        'sup_sellers': json.dumps(all_supsell),
        'seller_sup_sellers': json.dumps(all_sup_sellers),
        'category': category,
        'sub_category': sub_category,
        'city': city,
        'state': state,
        'country': country,
        'type': type,
    }
    print(context['data_investor'])
    print(context['just_sellers'])
    print(context['advise_sellers'])
    print(context['invest_sellers'])
    print(context['my_sellers'])
    return render(request, 'seller1/display_web.html', context)

@login_required(login_url='profiles:index')
def display_advise(request):
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    user = request.user
    investor=user.profile.user_invest.all()
    # iserializer = None
    # invest = None
    all_isell = {}
    # if investor is not None:
    #     iserializer=InvestorSerializer(investor)
    #     invest = Invest.objects.get(investor=investor)
    #     invest_sell = invest.cart_seller.all()
    #     all_isell= SellerSerializer(invest_sell, many=True).data
    data_investor = []
    for invest in investor:
        iserializer = InvestorSerializer(invest.investor).data
        data_investor.append(iserializer)
        iname = 'investor_' + str(invest.investor.investor_id)
        all_isell[iname] = SellerSerializer(invest.cart_seller.all(), many=True).data
    # data_investor = None
    # if iserializer is not None:
    #     data_investor=iserializer.data
    #     exist = {
    #         'exist': 'True'
    #     }
    #     cdata = data_investor.copy()
    #     cdata.update(exist)
    #     data_investor=cdata
    # else:
    #     data_investor={
    #         'exist':'False'
    #     }
    sellers = user.profile.sell_type.all()
    data_sellers = []
    if sellers is not None:
        data_sellers = SellerSerializer(sellers, many=True).data
    print(data_sellers)
    data_advisors = []

    advisors = user.profile.advise_type.all()
    for advisor in advisors:
        asreializer = AdvisorSerializer(advisor)
        data_advisors.append(asreializer.data)
    # if advisors is not None:
    #     data_advisors= AdvisorSerializer(advisors, many=True)
    print(data_advisors)
    just_sell = user.profile.just_advise.all()
    all_jsell=[]
    all_jsell = AdvisorSerializer(just_sell, many=True).data
    his_sell = user.profile.user_sell.all()
    all_hsell = []
    all_hsell_advisor = {}
    for sell in his_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data
        all_hsell.append(dseller)
        sell_advisors = sell.cart_advisor.all()
        name = 'seller_' + str(sell_seller.business_id)
        all_hsell_advisor[name]=[]
        for one_advisor in sell_advisors:
            done_advisor = AdvisorSerializer(one_advisor).data
            all_hsell_advisor[name].append(done_advisor)
    advises = user.profile.user_advise.all()
    all_aisell={}
    all_aisell['startup']=[]
    all_aisell['business']=[]
    all_advise={}
    all_advise['startup']=[]
    all_advise['business']=[]
    for advise in advises:
        if advise.type == 'Startup':
            all_advise['startup'].append(AdvisorSerializer(advise.advisor).data)
        if advise.type == 'Business':
            all_advise['business'].append(AdvisorSerializer(advise.advisor).data)

    category = ''
    sub_category = ''
    city = ''
    state = ''
    country = ''
    type = 'Incubators'
    try:
        type = request.GET['type']
        category = request.GET['category']
        sub_category = request.GET['sub_category']
        city = request.GET['city']
        state = request.GET['state']
        country = request.GET['country']

    except:
        pass



    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'code_data': code_data,
        'year_data': yeardata,
        'data_investor': json.dumps(data_investor),
        'data_sellers':data_sellers,
        'data_advisors':json.dumps(all_advise),
        'just_advisors': json.dumps(all_jsell),
        'invest_advisors':json.dumps(all_isell),
        'my_sellers': json.dumps(all_hsell),
        'sellers_advisors':json.dumps(all_hsell_advisor),
        'category': category,
        'sub_category': sub_category,
        'city': city,
        'state': state,
        'country': country,
        'type': type,
    }
    print(context['data_investor'])
    print(context['just_advisors'])
    print(context['invest_advisors'])
    print(context['sellers_advisors'])
    print(context['my_sellers'])
    return render(request, 'seller1/display_advise.html', context)


@login_required(login_url='profiles:index')
def display_advise_startup(request):
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    user = request.user
    investor=user.profile.user_invest.all()
    # iserializer = None
    # invest = None
    all_isell = {}
    # if investor is not None:
    #     iserializer=InvestorSerializer(investor)
    #     invest = Invest.objects.get(investor=investor)
    #     invest_sell = invest.cart_seller.all()
    #     all_isell= SellerSerializer(invest_sell, many=True).data
    data_investor = []
    for invest in investor:
        iserializer = InvestorSerializer(invest.investor).data
        data_investor.append(iserializer)
        iname = 'investor_' + str(invest.investor.investor_id)
        all_isell[iname] = SellerSerializer(invest.cart_seller.all(), many=True).data
    # data_investor = None
    # if iserializer is not None:
    #     data_investor=iserializer.data
    #     exist = {
    #         'exist': 'True'
    #     }
    #     cdata = data_investor.copy()
    #     cdata.update(exist)
    #     data_investor=cdata
    # else:
    #     data_investor={
    #         'exist':'False'
    #     }
    sellers = user.profile.sell_type.all()
    data_sellers = []
    if sellers is not None:
        data_sellers = SellerSerializer(sellers, many=True).data
    print(data_sellers)
    data_advisors = []

    advisors = user.profile.advise_type.all()
    for advisor in advisors:
        asreializer = AdvisorSerializer(advisor)
        data_advisors.append(asreializer.data)
    # if advisors is not None:
    #     data_advisors= AdvisorSerializer(advisors, many=True)
    print(data_advisors)
    just_sell = user.profile.just_advise.all()
    all_jsell=[]
    all_jsell = AdvisorSerializer(just_sell, many=True).data
    his_sell = user.profile.user_sell.all()
    all_hsell = []
    all_hsell_advisor = {}
    for sell in his_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data
        all_hsell.append(dseller)
        sell_advisors = sell.cart_advisor.all()
        name = 'seller_' + str(sell_seller.business_id)
        all_hsell_advisor[name]=[]
        for one_advisor in sell_advisors:
            done_advisor = AdvisorSerializer(one_advisor).data
            all_hsell_advisor[name].append(done_advisor)
    advises = user.profile.user_advise.all()
    all_advise={}
    all_advise['startup']=[]
    all_advise['business']=[]
    for advise in advises:
        if advise.type == 'Startup':
            all_advise['startup'].append(AdvisorSerializer(advise.advisor).data)
        if advise.type == 'Business':
            all_advise['business'].append(AdvisorSerializer(advise.advisor).data)

    category = ''
    sub_category = ''
    city = ''
    state = ''
    country = ''
    type = 'Incubators'
    try:
        type = request.GET['type']
        category = request.GET['category']
        sub_category = request.GET['sub_category']
        city = request.GET['city']
        state = request.GET['state']
        country = request.GET['country']

    except:
        pass


    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'code_data': code_data,
        'year_data': yeardata,
        'data_investor': json.dumps(data_investor),
        'data_sellers':data_sellers,
        'data_advisors':json.dumps(all_advise),
        'just_advisors': json.dumps(all_jsell),
        'invest_advisors':json.dumps(all_isell),
        'my_sellers': json.dumps(all_hsell),
        'sellers_advisors':json.dumps(all_hsell_advisor),
        'category': category,
        'sub_category': sub_category,
        'city': city,
        'state': state,
        'country': country,
        'type': type,
    }
    print(context['data_investor'])
    print(context['just_advisors'])
    print(context['invest_advisors'])
    print(context['sellers_advisors'])
    print(context['my_sellers'])
    return render(request, 'seller1/display_advise_startup.html', context)

@login_required(login_url='profiles:index')
def display_invest(request):
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    user = request.user
    investor=user.profile.user_invest.all()
    iserializer = None
    invest = None
    # all_isell = []
    # if investor is not None:
    #     iserializer=InvestorSerializer(investor)
        # invest = Invest.objects.get(investor=investor)
        # invest_sell = invest.cart_advisor.all()
        # all_isell= AdvisorSerializer(invest_sell, many=True).data
    data_investor = []
    for invest in investor:
        iserializer = InvestorSerializer(invest.investor).data
        data_investor.append(iserializer)
        # iname = 'investor_' + str(invest.investor.investor_id)
        # all_isell[iname] = SellerSerializer(invest.cart_seller.all(), many=True).data
    # data_investor = None
    # if iserializer is not None:
    #     data_investor=iserializer.data
    #     exist = {
    #         'exist': 'True'
    #     }
    #     cdata = data_investor.copy()
    #     cdata.update(exist)
    #     data_investor=cdata
    # else:
    #     data_investor={
    #         'exist':'False'
    #     }
    sellers = user.profile.sell_type.all()
    data_sellers = []
    if sellers is not None:
        data_sellers = SellerSerializer(sellers, many=True).data
    print(data_sellers)
    data_advisors = []

    advisors = user.profile.user_advise.all()
    for advisor in advisors:
        asreializer = AdvisorSerializer(advisor.advisor)
        data_advisors.append(asreializer.data)
    # if advisors is not None:
    #     data_advisors= AdvisorSerializer(advisors, many=True)
    print(data_advisors)
    just_sell = user.profile.just_invest.all()
    all_jsell=[]
    all_jsell = InvestorSerializer(just_sell, many=True).data
    his_sell = user.profile.user_sell.all()
    all_hsell = []
    all_hsell_advisor = {}
    for sell in his_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data
        all_hsell.append(dseller)
        sell_advisors = sell.cart_investor.all()
        name = 'seller_' + str(sell_seller.business_id)
        all_hsell_advisor[name]=[]
        for one_advisor in sell_advisors:
            done_advisor = InvestorSerializer(one_advisor).data
            all_hsell_advisor[name].append(done_advisor)
    advises = user.profile.user_advise.all()
    all_aisell={}
    # all_aisell['startup']={}
    # all_aisell['business']={}
    for advise in advises:
        # if advise.type == 'Startup':
        aname='advisor_'+str(advise.advisor.advisor_id)
        all_aisell[aname]=InvestorSerializer(advise.cart_invest, many=True).data
        # if advise.type == 'Business':
        #     aname = 'advisor_' + str(advise.advisor.advisor_id)
        #     all_aisell['business'][aname]=InvestorSerializer(advise.cart_invest, many=True).data
    category = ''
    sub_category = ''
    city = ''
    state = ''
    country = ''
    type = 'Financier'

    try:
        category=request.GET['category']
    except:
        pass
    # try:
    #     sub_category = request.GET['sub_category']
    # except:
    #     pass
    try:
        city = request.GET['city']
    except:
        pass
    try:
        state = request.GET['state']
    except:
        pass
    try:
        country = request.GET['country']
    except:
        pass
    try:
        type=request.GET['type']
    except:
        pass

    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'code_data': code_data,
        'year_data': yeardata,
        'data_investor': json.dumps(data_investor),
        'data_sellers':data_sellers,
        'data_advisors':json.dumps(data_advisors),
        'just_investors': json.dumps(all_jsell),
        'advise_investors':json.dumps(all_aisell),
        'my_sellers': json.dumps(all_hsell),
        'sellers_investors':json.dumps(all_hsell_advisor),
        'category': category,
        'sub_category': sub_category,
        'city': city,
        'state': state,
        'country': country,
        'type': type,
    }
    print(context['data_advisors'])
    print(context['just_investors'])
    print(context['advise_investors'])
    print(context['sellers_investors'])
    print(context['my_sellers'])
    return render(request, 'seller1/display_invest.html', context)

@login_required(login_url='profiles:index')
def display_franchise(request):
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    user = request.user
    investor = user.profile.user_invest.all()
    # iserializer = None
    # invest = None
    all_isell = {}
    # if investor is not None:
    #     iserializer=InvestorSerializer(investor)
    #     invest = Invest.objects.get(investor=investor)
    #     invest_sell = invest.cart_seller.all()
    #     all_isell= SellerSerializer(invest_sell, many=True).data
    data_investor = []
    for invest in investor:
        iserializer = InvestorSerializer(invest.investor).data
        data_investor.append(iserializer)
        iname = 'investor_' + str(invest.investor.investor_id)
        all_isell[iname] = SellerSerializer(invest.cart_seller.all(), many=True).data
    # data_investor = None
    # if iserializer is not None:
    #     data_investor = iserializer.data
    #     exist = {
    #         'exist': 'True'
    #     }
    #     cdata = data_investor.copy()
    #     cdata.update(exist)
    #     data_investor = cdata
    # else:
    #     data_investor = {
    #         'exist': 'False'
    #     }
    sellers = user.profile.sell_type.all()
    data_sellers = []
    if sellers is not None:
        data_sellers = SellerSerializer(sellers, many=True).data
    print(data_sellers)
    data_advisors = []

    advisors = user.profile.advise_type.all()
    for advisor in advisors:
        asreializer = AdvisorSerializer(advisor)
        data_advisors.append(asreializer.data)
    # if advisors is not None:
    #     data_advisors= AdvisorSerializer(advisors, many=True)
    print(data_advisors)
    just_sell = user.profile.just_sell.all()
    all_jsell = []
    all_jsell = SellerSerializer(just_sell, many=True).data
    his_sell = user.profile.user_sell.all()
    all_hsell = []
    all_supsell = []
    all_sup_sell = []
    for sell in his_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data
        all_hsell.append(dseller)
        if sell_seller.type == 'Supplier':
            all_supsell.append(dseller)
            all_sup_sell.append(sell)
    advises = user.profile.user_advise.all()
    all_sup_sellers = {}
    for sell in all_sup_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data

        sell_advisors = sell.cart_sellers.all()
        name = 'seller_' + str(sell_seller.business_id)
        all_sup_sellers[name] = []
        for one_advisor in sell_advisors:
            done_advisor = SellerSerializer(one_advisor).data
            all_sup_sellers[name].append(done_advisor)

    all_aisell = {}

    for advise in advises:

        aname = 'advisor_' + str(advise.advisor.advisor_id)
        all_aisell[aname] = SellerSerializer(advise.cart_seller, many=True).data

    category = ''
    sub_category = ''
    city = ''
    state = ''
    country = ''
    type = 'Franchise'
    try:
        # type = request.GET['type']
        category = request.GET['category']
        sub_category = request.GET['sub_category']
        city = request.GET['city']
        state = request.GET['state']
        country = request.GET['country']

    except:
        pass
    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'code_data': code_data,
        'year_data': yeardata,
        'data_investor': json.dumps(data_investor),
        'data_sellers': data_sellers,
        'data_advisors': json.dumps(data_advisors),
        'just_sellers': json.dumps(all_jsell),
        'advise_sellers': json.dumps(all_aisell),
        'invest_sellers': json.dumps(all_isell),
        'my_sellers': json.dumps(all_hsell),
        'sup_sellers': json.dumps(all_supsell),
        'seller_sup_sellers': json.dumps(all_sup_sellers),
        'category': category,
        'sub_category': sub_category,
        'city': city,
        'state': state,
        'country': country,
        'type': type,
    }
    print(context['data_investor'])
    print(context['just_sellers'])
    print(context['advise_sellers'])
    print(context['invest_sellers'])
    print(context['my_sellers'])
    return render(request, 'seller1/display_franchise.html', context)


@login_required(login_url='profiles:index')
def display_supplier(request):
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    user = request.user
    investor = user.profile.user_invest.all()
    # iserializer = None
    # invest = None
    all_isell = {}
    # if investor is not None:
    #     iserializer=InvestorSerializer(investor)
    #     invest = Invest.objects.get(investor=investor)
    #     invest_sell = invest.cart_seller.all()
    #     all_isell= SellerSerializer(invest_sell, many=True).data
    data_investor = []
    for invest in investor:
        iserializer = InvestorSerializer(invest.investor).data
        data_investor.append(iserializer)
        iname = 'investor_' + str(invest.investor.investor_id)
        all_isell[iname] = SellerSerializer(invest.cart_seller.all(), many=True).data
    # data_investor = None
    # if iserializer is not None:
    #     data_investor = iserializer.data
    #     exist = {
    #         'exist': 'True'
    #     }
    #     cdata = data_investor.copy()
    #     cdata.update(exist)
    #     data_investor = cdata
    # else:
    #     data_investor = {
    #         'exist': 'False'
    #     }
    sellers = user.profile.sell_type.all()
    data_sellers = []
    if sellers is not None:
        data_sellers = SellerSerializer(sellers, many=True).data
    print(data_sellers)
    data_advisors = []

    advisors = user.profile.advise_type.all()
    for advisor in advisors:
        asreializer = AdvisorSerializer(advisor)
        data_advisors.append(asreializer.data)
    # if advisors is not None:
    #     data_advisors= AdvisorSerializer(advisors, many=True)
    print(data_advisors)
    just_sell = user.profile.just_sell.all()
    all_jsell = []
    all_jsell = SellerSerializer(just_sell, many=True).data
    his_sell = user.profile.user_sell.all()
    all_hsell = []
    all_supsell = []
    all_sup_sell=[]
    for sell in his_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data
        all_hsell.append(dseller)
        if sell_seller.type != 'Supplier':
            all_supsell.append(dseller)
            all_sup_sell.append(sell)
    advises = user.profile.user_advise.all()
    all_sup_sellers = {}
    for sell in all_sup_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data

        sell_advisors = sell.cart_suppliers.all()
        name = 'seller_' + str(sell_seller.business_id)
        all_sup_sellers[name] = []
        for one_advisor in sell_advisors:
            done_advisor = SellerSerializer(one_advisor).data
            all_sup_sellers[name].append(done_advisor)
    advises = user.profile.user_advise.all()
    all_aisell = {}
    all_aisell['startup'] = {}
    all_aisell['business'] = {}
    for advise in advises:
        if advise.type == 'Startup':
            aname = 'advisor_' + str(advise.advisor.advisor_id)
            all_aisell['startup'][aname] = SellerSerializer(advise.cart_seller, many=True).data
        if advise.type == 'Business':
            aname = 'advisor_' + str(advise.advisor.advisor_id)
            all_aisell['business'][aname] = SellerSerializer(advise.cart_seller, many=True).data
    category = ''
    sub_category = ''
    city = ''
    state = ''
    country = ''
    type = 'Supplier'
    try:
        category = request.GET['category']
        sub_category = request.GET['sub_category']
        city = request.GET['city']
        state = request.GET['state']
        country = request.GET['country']
        # type = request.GET['type']
    except:
        pass
    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'code_data': code_data,
        'year_data': yeardata,
        'data_investor': json.dumps(data_investor),
        'data_sellers': data_sellers,
        'data_advisors': json.dumps(data_advisors),
        'just_sellers': json.dumps(all_jsell),
        'advise_sellers': json.dumps(all_aisell),
        'invest_sellers': json.dumps(all_isell),
        'my_sellers': json.dumps(all_hsell),
        'seller_sellers': json.dumps(all_sup_sellers),
        'supp_sellers': json.dumps(all_supsell),
        'category': category,
        'sub_category': sub_category,
        'city': city,
        'state': state,
        'country': country,
        'type': type,
    }
    print(context['data_investor'])
    print(context['just_sellers'])
    print(context['advise_sellers'])
    print(context['invest_sellers'])
    print(context['my_sellers'])
    return render(request, 'seller1/display_supplier.html', context)

@login_required(login_url='profiles:index')
def display_startup(request):
    sectors = business_sector()
    types_companies = companies()
    code_data = codedata()
    user = request.user
    investor = user.profile.user_invest.all()
    # iserializer = None
    # invest = None
    all_isell = {}
    # if investor is not None:
    #     iserializer=InvestorSerializer(investor)
    #     invest = Invest.objects.get(investor=investor)
    #     invest_sell = invest.cart_seller.all()
    #     all_isell= SellerSerializer(invest_sell, many=True).data
    data_investor = []
    for invest in investor:
        iserializer = InvestorSerializer(invest.investor).data
        data_investor.append(iserializer)
        iname = 'investor_' + str(invest.investor.investor_id)
        all_isell[iname] = SellerSerializer(invest.cart_seller.all(), many=True).data
    # data_investor = None
    # if iserializer is not None:
    #     data_investor = iserializer.data
    #     exist = {
    #         'exist': 'True'
    #     }
    #     cdata = data_investor.copy()
    #     cdata.update(exist)
    #     data_investor = cdata
    # else:
    #     data_investor = {
    #         'exist': 'False'
    #     }
    sellers = user.profile.sell_type.all()
    data_sellers = []
    if sellers is not None:
        data_sellers = SellerSerializer(sellers, many=True).data
    print(data_sellers)
    data_advisors = []

    advisors = user.profile.advise_type.all()
    for advisor in advisors:
        asreializer = AdvisorSerializer(advisor)
        data_advisors.append(asreializer.data)
    # if advisors is not None:
    #     data_advisors= AdvisorSerializer(advisors, many=True)
    print(data_advisors)
    just_sell = user.profile.just_sell.all()
    all_jsell = []
    all_jsell = SellerSerializer(just_sell, many=True).data
    his_sell = user.profile.user_sell.all()
    all_hsell = []
    all_supsell = []
    all_sup_sell = []
    for sell in his_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data
        all_hsell.append(dseller)
        if sell_seller.type == 'Supplier':
            all_supsell.append(dseller)
            all_sup_sell.append(sell)
    advises = user.profile.user_advise.all()
    all_sup_sellers = {}
    for sell in all_sup_sell:
        sell_seller = sell.seller
        dseller = SellerSerializer(sell_seller).data

        sell_advisors = sell.cart_sellers.all()
        name = 'seller_' + str(sell_seller.business_id)
        all_sup_sellers[name] = []
        for one_advisor in sell_advisors:
            done_advisor = SellerSerializer(one_advisor).data
            all_sup_sellers[name].append(done_advisor)
    all_aisell = {}
    all_aisell['startup'] = {}
    all_aisell['business'] = {}
    for advise in advises:
        if advise.type == 'Startup':
            aname = 'advisor_' + str(advise.advisor.advisor_id)
            all_aisell['startup'][aname] = SellerSerializer(advise.cart_seller, many=True).data
        if advise.type == 'Business':
            aname = 'advisor_' + str(advise.advisor.advisor_id)
            all_aisell['business'][aname] = SellerSerializer(advise.cart_seller, many=True).data
    category = ''
    sub_category = ''
    city = ''
    state = ''
    country = ''
    type = 'Startup'
    try:
        category = request.GET['category']
        sub_category = request.GET['sub_category']
        city = request.GET['city']
        state = request.GET['state']
        country = request.GET['country']
        # type = request.GET['type']
    except:
        pass
    context = {
        'sectors': sectors,
        'types_companies': types_companies,
        'code_data': code_data,
        'year_data': yeardata,
        'data_investor': json.dumps(data_investor),
        'data_sellers': data_sellers,
        'data_advisors': json.dumps(data_advisors),
        'just_sellers': json.dumps(all_jsell),
        'advise_sellers': json.dumps(all_aisell),
        'invest_sellers': json.dumps(all_isell),
        'my_sellers': json.dumps(all_hsell),
        'sup_sellers': json.dumps(all_supsell),
        'seller_sup_sellers': json.dumps(all_sup_sellers),
        'category': category,
        'sub_category': sub_category,
        'city': city,
        'state': state,
        'country': country,
        'type': type,
    }
    print(context['data_investor'])
    print(context['just_sellers'])
    print(context['advise_sellers'])
    print(context['invest_sellers'])
    print(context['my_sellers'])
    return render(request, 'seller1/display_startup.html', context)


@login_required(login_url='profiles:index')
def just_add_cart(request):
    if request.method=='POST':
        user = request.user
        seller_id = request.POST['seller_id']
        base_type=request.POST['base_type']
        if base_type=='Seller':
            seller = Seller1.objects.get(business_id=seller_id)
            user.profile.just_sell.add(seller)
            user.save()

            return JsonResponse({'title':seller.title, 'status':'success'})
        if base_type=='Advisor':
            seller = Advisor.objects.get(advisor_id=seller_id)
            user.profile.just_advise.add(seller)
            user.save()
            return JsonResponse({'title':seller.first_name, 'status':'success'})
        if base_type=='Investor':
            seller = Investor.objects.get(investor_id=seller_id)
            user.profile.just_invest.add(seller)
            user.save()
            return JsonResponse({'title':seller.first_name, 'status':'success'})
        return JsonResponse({'status':'fail'}, safe=False)

@login_required(login_url='profiles:index')
def just_remove_cart(request):
    if request.method=='POST':
        user = request.user
        seller_id = request.POST['seller_id']
        base_type=request.POST['base_type']
        if base_type=='Seller':
            seller = Seller1.objects.get(business_id=seller_id)
            user.profile.just_sell.remove(seller)
            user.save()
            return JsonResponse({'title':seller.title, 'status':'success'})
        if base_type=='Advisor':
            seller = Advisor.objects.get(advisor_id=seller_id)
            user.profile.just_advise.remove(seller)
            user.save()
            return JsonResponse({'title':seller.first_name, 'status':'success'})
        if base_type=='Investor':
            seller = Investor.objects.get(investor_id=seller_id)
            user.profile.just_invest.remove(seller)
            user.save()
            return JsonResponse({'title':seller.first_name, 'status':'success'})
        return JsonResponse({'status':'fail'}, safe=False)


@login_required(login_url='profiles:index')
def add_invest_cart(request):
    if request.method=='POST':
        user = request.user

        base_type=request.POST['base_type']
        investor_id = request.POST['investor_id']
        investor = Investor.objects.get(investor_id=investor_id)
        if base_type=='Seller':
            seller_id = request.POST['seller_id']
            seller = Seller1.objects.get(business_id=seller_id)
            user.profile.sell_type.add(seller)
            user.save()
            user_sell = Sell.objects.get(seller=seller)
            user_sell.inst_investors.add(investor)
            user_sell.save()
            invest = Invest.objects.get(investor=investor)
            invest.cart_seller.add(seller)
            invest.save()
            notif = Notification()
            notif.notif_type = 'Cart'
            notif.notif_on = 'seller'
            notif.notif_on_id=seller_id
            notif.notif_statement = ''+ investor.first_name + ' ' + investor.last_name + ', is interested in ' + seller.title
            notif.save()
            seller_user=user_sell.profile_set.all()[0].user
            seller_user.profile.notifs.add(notif)
            seller_user.save()

            return JsonResponse({'title':seller.title, 'status':'success'})
        if base_type=='Advisor':
            advisor_id = request.POST['advisor_id']
            advisor = Advisor.objects.get(advisor_id=advisor_id)
            user.profile.advise_type.add(advisor)
            user.save()
            user_advise = Advise.objects.get(advisor=advisor)
            user_advise.inst_invest.add(investor)
            user_advise.save()
            invest = Invest.objects.get(investor=investor)
            invest.cart_advisor.add(advisor)
            invest.save()
            notif = Notification()
            notif.notif_type = 'Cart'
            notif.notif_on = 'advisor'
            notif.notif_on_id = advisor_id
            notif.notif_statement = '' + investor.first_name + ' ' + investor.last_name + ', is interested in your advising as' + advisor.first_name + ' ' + advisor.last_name
            notif.save()
            seller_user = user_advise.profile_set.all()[0].user
            seller_user.profile.notifs.add(notif)
            seller_user.save()
        # if base_type=='Investor':
        #     seller = Investor.objects.get(investor_id=seller_id)
        #     user.profile.just_invest.add(seller)
        #     user.save()
        #     return Response({'title':seller.first_name, 'status':'success'})
        return Response({'status':'fail'})

@login_required(login_url='profiles:index')
def remove_invest_cart(request):
    if request.method=='POST':
        user = request.user

        base_type=request.POST['base_type']
        investor_id = request.POST['investor_id']
        investor = Investor.objects.get(investor_id=investor_id)
        if base_type=='Seller':
            seller_id = request.POST['seller_id']
            seller = Seller1.objects.get(business_id=seller_id)
            user.profile.sell_type.remove(seller)
            user.save()
            user_sell = Sell.objects.get(seller=seller)
            user_sell.inst_investors.remove(investor)
            user_sell.save()
            invest = Invest.objects.get(investor=investor)
            invest.cart_seller.remove(seller)
            invest.save()

            return JsonResponse({'title':seller.title, 'status':'success'})
        if base_type=='Advisor':
            advisor_id = request.POST['advisor_id']
            advisor = Advisor.objects.get(advisor_id=advisor_id)
            user.profile.advise_type.remove(advisor)
            user.save()
            user_advise = Advise.objects.get(advisor=advisor)
            user_advise.inst_invest.remove(investor)
            user_advise.save()
            invest = Invest.objects.get(investor=investor)
            invest.cart_advisor.remove(advisor)
            invest.save()

            return JsonResponse({'title':advisor.first_name, 'status':'success'})
        # if base_type=='Investor':
        #     seller = Investor.objects.get(investor_id=seller_id)
        #     user.profile.just_invest.add(seller)
        #     user.save()
        #     return Response({'title':seller.first_name, 'status':'success'})
        return Response({'status':'fail'})

@login_required(login_url='profiles:index')
def add_advise_cart(request):
    if request.method == 'POST':
        user = request.user

        base_type = request.POST['base_type']
        advisor_id = request.POST['advisor_id']
        advisor = Advisor.objects.get(advisor_id=advisor_id)
        # investor = user.profile.invest_type
        if base_type == 'Seller':
            seller_id = request.POST['seller_id']
            seller = Seller1.objects.get(business_id=seller_id)
            # user.profile.sell_type.add(seller)
            # user.save()
            user_sell = Sell.objects.get(seller=seller)
            user_sell.inst_advisor.add(advisor)
            user_sell.save()
            advise = Advise.objects.get(advisor=advisor)
            advise.cart_seller.add(seller)
            advise.save()
            notif = Notification()
            notif.notif_type = 'Cart'
            notif.notif_on = 'seller'
            notif.notif_on_id = seller_id
            notif.notif_statement = '' + advisor.first_name + ' ' + advisor.last_name + ', is interested in ' +seller.title
            notif.save()
            seller_user = user_sell.profile_set.all()[0].user
            seller_user.profile.notifs.add(notif)
            seller_user.save()
            return JsonResponse({'title': seller.title, 'status': 'success'})
        if base_type == 'Investor':
            investor_id = request.POST['investor_id']
            investor = Investor.objects.get(investor_id=investor_id)
            # user.profile.investors_type.add(investor)
            # user.save()
            user_invest = Invest.objects.get(investor=investor)
            user_invest.inst_advisor.add(advisor)
            user_invest.save()
            advise = Advise.objects.get(advisor=advisor)
            advise.cart_invest.add(investor)
            advise.save()
            notif = Notification()
            notif.notif_type = 'Cart'
            notif.notif_on = 'investor'
            notif.notif_on_id = investor_id
            notif.notif_statement = '' + advisor.first_name + ' ' + advisor.last_name + ', is interested in your investing'
            notif.save()
            seller_user = user_invest.profile_set.all()[0].user
            seller_user.profile.notifs.add(notif)
            seller_user.save()
            return JsonResponse({'title': investor.first_name, 'status': 'success'})
        # if base_type=='Investor':
        #     seller = Investor.objects.get(investor_id=seller_id)
        #     user.profile.just_invest.add(seller)
        #     user.save()
        #     return Response({'title':seller.first_name, 'status':'success'})
        return Response({'status': 'fail'})

@login_required(login_url='profiles:index')
def remove_advise_cart(request):
    if request.method == 'POST':
        user = request.user

        base_type = request.POST['base_type']
        advisor_id = request.POST['advisor_id']
        advisor = Advisor.objects.get(advisor_id=advisor_id)
        # investor = user.profile.invest_type
        if base_type == 'Seller':
            seller_id = request.POST['seller_id']
            seller = Seller1.objects.get(business_id=seller_id)
            user.profile.sell_type.remove(seller)
            user.save()
            user_sell = Sell.objects.get(seller=seller)
            user_sell.inst_advisor.remove(advisor)
            user_sell.save()
            advise = Advise.objects.get(advisor=advisor)
            advise.cart_seller.remove(seller)
            advise.save()

            return JsonResponse({'title': seller.title, 'status': 'success'})
        if base_type == 'Investor':
            investor_id = request.POST['investor_id']
            investor = Investor.objects.get(investor_id=investor_id)
            user.profile.investors_type.remove(investor)
            user.save()
            user_invest = Invest.objects.get(investor=investor)
            user_invest.inst_advisor.remove(advisor)
            user_invest.save()
            advise = Advise.objects.get(advisor=advisor)
            advise.cart_invest.remove(investor)
            advise.save()
            return JsonResponse({'title': investor.first_name, 'status': 'success'})
        # if base_type=='Investor':
        #     seller = Investor.objects.get(investor_id=seller_id)
        #     user.profile.just_invest.add(seller)
        #     user.save()
        #     return Response({'title':seller.first_name, 'status':'success'})
        return Response({'status': 'fail'})

@login_required(login_url='profiles:index')
def add_sell_cart(request):
    if request.method == 'POST':
        user = request.user

        base_type = request.POST['base_type']
        seller_id = request.POST['seller_id']
        seller = Seller1.objects.get(business_id=seller_id)
        # investor = user.profile.invest_type
        if base_type == 'Seller':
            advisor_id = request.POST['add_seller_id']
            advisor = Seller1.objects.get(business_id=advisor_id)
            # user.profile.advise_type.add(advisor)
            # user.save()
            user_advise = Sell.objects.get(seller=advisor)
            user_advise.inst_suppliers.add(seller)
            user_advise.save()
            sell = Sell.objects.get(seller=seller)
            sell.cart_sellers.add(advisor)
            sell.save()
            notif = Notification()
            notif.notif_type = 'Cart'
            notif.notif_on = 'seller'
            notif.notif_on_id = advisor_id
            notif.notif_statement = '' + seller.title + ', is interested in your listing ' + advisor.title
            notif.save()
            seller_user = user_advise.profile_set.all()[0].user
            seller_user.profile.notifs.add(notif)
            seller_user.save()
            return JsonResponse({'title': advisor.first_name, 'status': 'success'})
        if base_type == 'Supplier':
            advisor_id = request.POST['supplier_id']
            advisor = Seller1.objects.get(business_id=advisor_id)
            # user.profile.advise_type.add(advisor)
            # user.save()
            user_advise = Sell.objects.get(seller=advisor)
            user_advise.inst_sellers.add(seller)
            user_advise.save()
            sell = Sell.objects.get(seller=seller)
            sell.cart_suppliers.add(advisor)
            sell.save()
            notif = Notification()
            notif.notif_type = 'Cart'
            notif.notif_on = 'seller'
            notif.notif_on_id = advisor_id
            notif.notif_statement = '' + seller.title + ', is interested in your listing ' + advisor.title
            notif.save()
            seller_user = user_advise.profile_set.all()[0].user
            seller_user.profile.notifs.add(notif)
            seller_user.save()
            return JsonResponse({'title': advisor.first_name, 'status': 'success'})
        if base_type == 'Advisor':
            advisor_id = request.POST['advisor_id']
            advisor = Advisor.objects.get(advisor_id=advisor_id)
            user.profile.advise_type.add(advisor)
            user.save()
            user_advise = Advise.objects.get(advisor=advisor)
            user_advise.inst_seller.add(seller)
            user_advise.save()
            sell = Sell.objects.get(seller=seller)
            sell.cart_advisor.add(advisor)
            sell.save()
            notif = Notification()
            notif.notif_type = 'Cart'
            notif.notif_on = 'advisor'
            notif.notif_on_id = advisor_id
            notif.notif_statement = '' + seller.title + ', is interested in your advising ' + advisor.first_name + ' ' + advisor.last_name
            notif.save()
            seller_user = user_advise.profile_set.all()[0].user
            seller_user.profile.notifs.add(notif)
            seller_user.save()
            return JsonResponse({'title': advisor.first_name, 'status': 'success'})
        if base_type == 'Investor':
            investor_id = request.POST['investor_id']
            investor = Investor.objects.get(investor_id=investor_id)
            user.profile.investors_type.add(investor)
            user.save()
            user_invest = Invest.objects.get(investor=investor)
            user_invest.inst_seller.add(seller)
            user_invest.save()
            sell = Sell.objects.get(seller=seller)
            sell.cart_investor.add(investor)
            sell.save()
            notif = Notification()
            notif.notif_type = 'Cart'
            notif.notif_on = 'investor'
            notif.notif_on_id = investor_id
            notif.notif_statement = '' + seller.title + ', is interested in your investing'
            notif.save()
            seller_user = user_invest.profile_set.all()[0].user
            seller_user.profile.notifs.add(notif)
            seller_user.save()
            return JsonResponse({'title': investor.first_name, 'status': 'success'})
        # if base_type=='Investor':
        #     seller = Investor.objects.get(investor_id=seller_id)
        #     user.profile.just_invest.add(seller)
        #     user.save()
        #     return Response({'title':seller.first_name, 'status':'success'})
        return Response({'status': 'fail'})

@login_required(login_url='profiles:index')
def remove_sell_cart(request):
    if request.method == 'POST':
        user = request.user

        base_type = request.POST['base_type']
        seller_id = request.POST['seller_id']
        seller = Seller1.objects.get(business_id=seller_id)
        # investor = user.profile.invest_type
        if base_type == 'Seller':
            advisor_id = request.POST['add_seller_id']
            advisor = Seller1.objects.get(business_id=advisor_id)
            # user.profile.advise_type.remove(advisor)
            # user.save()
            user_advise = Sell.objects.get(seller=advisor)
            user_advise.inst_suppliers.remove(seller)
            user_advise.save()
            sell = Sell.objects.get(seller=seller)
            sell.cart_sellers.remove(advisor)
            sell.save()
            print('removed')
            return JsonResponse({'title': advisor.first_name, 'status': 'success'})
        if base_type == 'Supplier':
            advisor_id = request.POST['supplier_id']
            advisor = Seller1.objects.get(business_id=advisor_id)
            # user.profile.advise_type.remove(advisor)
            # user.save()
            user_advise = Sell.objects.get(seller=advisor)
            user_advise.inst_sellers.remove(seller)
            user_advise.save()
            sell = Sell.objects.get(seller=seller)
            sell.cart_suppliers.remove(advisor)
            sell.save()
            print('removed')
            return JsonResponse({'title': advisor.first_name, 'status': 'success'})
        if base_type == 'Advisor':
            advisor_id = request.POST['advisor_id']
            advisor = Advisor.objects.get(advisor_id=advisor_id)
            user.profile.advise_type.remove(advisor)
            user.save()
            user_advise = Advise.objects.get(advisor=advisor)
            user_advise.inst_seller.remove(seller)
            user_advise.save()
            sell = Sell.objects.get(seller=seller)
            sell.cart_advisor.remove(advisor)
            sell.save()
            print('removed')
            return JsonResponse({'title': advisor.first_name, 'status': 'success'})
        if base_type == 'Investor':
            investor_id = request.POST['investor_id']
            investor = Investor.objects.get(investor_id=investor_id)
            user.profile.investors_type.remove(investor)
            user.save()
            user_invest = Invest.objects.get(investor=investor)
            user_invest.inst_seller.remove(seller)
            user_invest.save()
            sell = Sell.objects.get(seller=seller)
            sell.cart_investor.remove(investor)
            sell.save()
            return JsonResponse({'title': investor.first_name, 'status': 'success'})
        # if base_type=='Investor':
        #     seller = Investor.objects.get(investor_id=seller_id)
        #     user.profile.just_invest.add(seller)
        #     user.save()
        #     return Response({'title':seller.first_name, 'status':'success'})
        return Response({'status': 'fail'})



def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
        print('media path')
        print(path)
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path

def seller_render_to_pdf(request,business_id):
    fs = FileSystemStorage()
    bcard_pdf_name =  os.path.join(settings.MEDIA_ROOT, 'seller_pdf_'+str(business_id)+'.pdf')
    # bcard_img_name = 'seller_img_'+str(business_id)
    # bcard_pdf = ''
    if fs.exists(bcard_pdf_name):
        image = pdf2image.convert_from_path(fs.path(bcard_pdf_name))
        response = HttpResponse(content_type="image/png")
        print(image)
        area = (0, 0, 620, 1000)
        cropped_img = image[0].crop(area)
        cropped_img.save(response, "png")
        return response
    else:
        seller = Seller1.objects.get(business_id=business_id)
        sell = Sell.objects.get(seller=seller)
        print(sell)
        stype = sell.type
        smodel = model_list[stype].objects.get(seller=seller)
        sserializer = serializer_list[stype](smodel)
        sdata = sserializer.data
        serializer = SellerSerializer(seller)
        data = serializer.data
        cdata = data.copy()
        # cdata.update(sdata)
        main_album_id = seller.album_id
        main_album = KAlbumForFile(album_id=main_album_id)
        main_files = main_album.files.all()
        srevenue = None
        rdata = None
        try:
            srevenue = RevenueModel.objects.get(seller=seller)
            rserializer = RevenueModelSerializer(srevenue)
            rdata = rserializer.data
            cdata.update(rdata)
        except:
            print('no revenue')
        # jdata = json.load(cdata)
        fdata = {}
        fdata['seller'] = cdata
        fdata['business'] = sdata

        fdata['first_image'] = main_files[0].name


        template = get_template('seller1/bcard.html')
        context = fdata
        html = template.render(context)
        print('html here')
        print(html)
        pdf_file = open(bcard_pdf_name, "w+b")
        pisaStatus = pisa.CreatePDF(html,dest=pdf_file, link_callback=link_callback)
        pdf_file.close()
        image = pdf2image.convert_from_path(bcard_pdf_name)
        response = HttpResponse(image,content_type="image/png")
        area = (0, 0, 620, 1000)
        cropped_img = image[0].crop(area)
        cropped_img.save(response, "png")
        # image.save(response, "png")
        return response

@login_required(login_url='profiles:index')
def indiv_dash(request):
    user = request.user
    just_sell = user.profile.just_sell.all()
    just_invest = user.profile.just_invest.all()
    just_advise = user.profile.just_advise.all()
    fdata={}
    fdata['cart']= []
    for sadvisor in just_sell:
        # print('debug start')
        # print(sadvisor)
        serializer = SellerSerializer(sadvisor)
        x = serializer.data
        print(x)
        album_id = sadvisor.album_id
        print(album_id)
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Seller'
        }
        itype = sadvisor.type

        imodel = model_list[itype].objects.get(seller=sadvisor)
        iserializer = serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        cx.update(y)
        print(cx)
        print(z)
        r = None
        try:
            srevenue = RevenueModel.objects.get(seller=sadvisor)
            rserializer = RevenueModelSerializer(srevenue)
            r = rserializer.data
            cx.update(r)
        except:
            r = {}
            print('no revenue')

        print(cx)
        # cx.update(z)
        data={}
        data['seller'] = cx
        data['business'] = z
        print(data)

        fdata['cart'].append(data)
    for investor in just_invest:
        serializer = InvestorSerializer(investor)
        x = serializer.data
        album_id = investor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Investor'
        }
        itype = investor.type

        imodel = inv_model_list[itype].objects.get(investor=investor)
        iserializer = inv_serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx
        data['business'] = z
        fdata['cart'].append(data)
    for advisor in just_advise:
        serializer = AdvisorSerializer(advisor)
        x = serializer.data
        album_id = advisor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Advisor'
        }
        itype = advisor.type

        imodel = adv_model_list[itype].objects.get(advisor=advisor)
        iserializer = adv_serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx
        data['business'] = z
        fdata['cart'].append(data)

    random.shuffle(fdata['cart'])
    fdata['list']=[]
    user_sell = user.profile.user_sell.all()
    user_advise = user.profile.user_advise.all()
    user_invest = user.profile.user_invest.all()

    for sell in user_sell:
        sadvisor = sell.seller
        # print('debug start')
        # print(sadvisor)
        serializer = SellerSerializer(sadvisor)
        x = serializer.data
        print(x)
        album_id = sadvisor.album_id
        print(album_id)
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Seller'
        }
        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx
        fdata['list'].append(data)
    for advise in user_advise:
        advisor = advise.advisor
        serializer = AdvisorSerializer(advisor)
        x = serializer.data
        album_id = advisor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Advisor'
        }

        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx

        fdata['list'].append(data)
    for invest in user_invest:
        investor=invest.investor
        serializer = InvestorSerializer(investor)
        x = serializer.data
        album_id = investor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Investor'
        }

        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx

        fdata['list'].append(data)


    return render(request, 'seller1/individual-investor-dashboard.html', fdata)

def user_profile(request):
    return render(request, 'seller1/buyer-profile.html', {})

@login_required(login_url='profiles:index')
def add_viewer(request):
    user = request.user
    seller_id = request.GET['seller_id']
    seller = Seller1.objects.get(business_id=seller_id)
    if seller.viewers.all().filter(username=user.username).exists():
        data = {
            'status': 'not added'
        }
        return JsonResponse(data, safe=False)
    else:
        seller.viewers.add(user)
        seller.save()
        data = {
            'status': 'added'
        }
        return JsonResponse(data, safe=False)


def indiv_dash2(request):
    user = request.user
    just_sell = user.profile.just_sell.all()
    just_invest = user.profile.just_invest.all()
    just_advise = user.profile.just_advise.all()
    fdata={}
    fdata['cart']= []
    for sadvisor in just_sell:
        # print('debug start')
        # print(sadvisor)
        serializer = SellerSerializer(sadvisor)
        x = serializer.data
        print(x)
        album_id = sadvisor.album_id
        print(album_id)
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Seller'
        }
        itype = sadvisor.type

        imodel = model_list[itype].objects.get(seller=sadvisor)
        iserializer = serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        cx.update(y)
        print(cx)
        print(z)
        r = None
        try:
            srevenue = RevenueModel.objects.get(seller=sadvisor)
            rserializer = RevenueModelSerializer(srevenue)
            r = rserializer.data
            cx.update(r)
        except:
            r = {}
            print('no revenue')

        print(cx)
        # cx.update(z)
        data={}
        data['seller'] = cx
        data['business'] = z
        print(data)

        fdata['cart'].append(data)
    for investor in just_invest:
        serializer = InvestorSerializer(investor)
        x = serializer.data
        album_id = investor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Investor'
        }
        itype = investor.type

        imodel = inv_model_list[itype].objects.get(investor=investor)
        iserializer = inv_serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx
        data['business'] = z
        fdata['cart'].append(data)
    for advisor in just_advise:
        serializer = AdvisorSerializer(advisor)
        x = serializer.data
        album_id = advisor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Advisor'
        }
        itype = advisor.type

        imodel = adv_model_list[itype].objects.get(advisor=advisor)
        iserializer = adv_serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx
        data['business'] = z
        fdata['cart'].append(data)

    random.shuffle(fdata['cart'])
    fdata['list']=[]
    user_sell = user.profile.user_sell.all()
    user_advise = user.profile.user_advise.all()
    user_invest = user.profile.user_invest.all()

    for sell in user_sell:
        sadvisor = sell.seller
        # print('debug start')
        # print(sadvisor)
        serializer = SellerSerializer(sadvisor)
        x = serializer.data
        print(x)
        album_id = sadvisor.album_id
        print(album_id)
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Seller'
        }
        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx
        fdata['list'].append(data)
    for advise in user_advise:
        advisor = advise.advisor
        serializer = AdvisorSerializer(advisor)
        x = serializer.data
        album_id = advisor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Advisor'
        }

        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx

        fdata['list'].append(data)
    for invest in user_invest:
        investor=invest.investor
        serializer = InvestorSerializer(investor)
        x = serializer.data
        album_id = investor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Investor'
        }

        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx

        fdata['list'].append(data)


    return JsonResponse(fdata, safe=False)


def fetch_sell_id(request,business_id):
    investor_id = business_id
    investor = Sell.objects.get(business_id=investor_id)
    invest = Profile.objects.get(user_sell=investor)
    profile_id = invest.profile_id
    photo_link = invest.photo.name
    first_name = invest.first_name
    last_name = invest.last_name
    contact_number = invest.contact_number
    social= invest.social
    country= invest.country
    premium = invest.premium


    datapack={
        'profile_id':profile_id,
        'photo_link':photo_link,
        'first_name':first_name,
        'last_name':last_name,
        'contact_number':contact_number,
        'social':social,
        'country':country,
        'premium':premium
    }

    return JsonResponse(datapack, safe=False)

def fetch_invest_id(request,business_id):
    investor_id = business_id
    investor = Invest.objects.get(investor_id=investor_id)
    invest = Profile.objects.get(user_invest=investor)
    profile_id = invest.profile_id
    photo_link = invest.photo.name
    first_name = invest.first_name
    last_name = invest.last_name
    contact_number = invest.contact_number
    social= invest.social
    country= invest.country
    premium = invest.premium


    datapack={
        'profile_id':profile_id,
        'photo_link':photo_link,
        'first_name':first_name,
        'last_name':last_name,
        'contact_number':contact_number,
        'social':social,
        'country':country,
        'premium':premium
    }

    return JsonResponse(datapack, safe=False)

def fetch_advise_id(request,business_id):
    investor_id = business_id
    investor = Advise.objects.get(advisor_id=investor_id)
    invest = Profile.objects.get(user_advise=investor)
    profile_id = invest.profile_id
    photo_link = invest.photo.name
    first_name = invest.first_name
    last_name = invest.last_name
    contact_number = invest.contact_number
    social= invest.social
    country= invest.country
    premium = invest.premium


    datapack={
        'profile_id':profile_id,
        'photo_link':photo_link,
        'first_name':first_name,
        'last_name':last_name,
        'contact_number':contact_number,
        'social':social,
        'country':country,
        'premium':premium
    }

    return JsonResponse(datapack, safe=False)


def fetch_sell_id(request,business_id):
    investor_id = business_id
    investor = Sell.objects.get(sell_id=investor_id)
    invest = Profile.objects.get(user_sell=investor)
    profile_id = invest.profile_id
    photo_link = invest.photo.name
    first_name = invest.first_name
    last_name = invest.last_name
    contact_number = invest.contact_number
    social= invest.social
    country= invest.country
    premium = invest.premium
    photo_url = invest.photo_url
    


    datapack={
        'profile_id':profile_id,
        'photo_link':photo_link,
        'first_name':first_name,
        'last_name':last_name,
        'contact_number':contact_number,
        'photo_url':photo_url,
        'social':social,
        'country':country,
        'premium':premium
    }

    return JsonResponse(datapack, safe=False)

def fetch_invest_id(request,business_id):
    investor_id = business_id
    investor = Invest.objects.get(investor_id=investor_id)
    invest = Profile.objects.get(user_invest=investor)
    profile_id = invest.profile_id
    photo_link = invest.photo.name
    first_name = invest.first_name
    last_name = invest.last_name
    photo_url = invest.photo_url
    contact_number = invest.contact_number
    social= invest.social
    country= invest.country
    premium = invest.premium


    datapack={
        'profile_id':profile_id,
        'photo_link':photo_link,
        'first_name':first_name,
        'last_name':last_name,
        'photo_url':photo_url,
        'contact_number':contact_number,
        'social':social,
        'country':country,
        'premium':premium
    }

    return JsonResponse(datapack, safe=False)

def fetch_advise_id(request,business_id):
    investor_id = business_id
    investor = Advise.objects.get(advisor_id=investor_id)
    invest = Profile.objects.get(user_advise=investor)
    profile_id = invest.profile_id
    photo_link = invest.photo.name
    first_name = invest.first_name
    last_name = invest.last_name
    contact_number = invest.contact_number
    social= invest.social
    country= invest.country
    premium = invest.premium
    photo_url = invest.photo_url


    datapack={
        'profile_id':profile_id,
        'photo_link':photo_link,
        'first_name':first_name,
        'last_name':last_name,
        'photo_url':photo_url,
        'contact_number':contact_number,
        'social':social,
        'country':country,
        'premium':premium
    }

    return JsonResponse(datapack, safe=False)


def fetch_detail_id(request,business_id):
    profile_id = business_id
    a=Profile.objects.get(profile_id=profile_id)
    user=a.user
    profile_id = a.profile_id
    photo_link = a.photo.name
    first_name = a.first_name
    last_name = a.last_name
    photo_url = a.photo_url

    just_sell = user.profile.just_sell.all()
    just_invest = user.profile.just_invest.all()
    just_advise = user.profile.just_advise.all()
    fdata={}
    fdata['cart']=[]

    datapack={
        'photo_link':photo_link,
        'first_name':first_name,
        'last_name':last_name,
        'photo_url':photo_url,
        
    }

    fdata['cart'].append(datapack)

    # fdata['metadata']= [photo_link,first_name,last_name]
    for sadvisor in just_sell:
        # print('debug start')
        # print(sadvisor)
        serializer = SellerSerializer(sadvisor)
        x = serializer.data
        print(x)
        album_id = sadvisor.album_id
        print(album_id)
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Seller'
        }
        itype = sadvisor.type

        imodel = model_list[itype].objects.get(seller=sadvisor)
        iserializer = serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        cx.update(y)
        print(cx)
        print(z)
        r = None
        try:
            srevenue = RevenueModel.objects.get(seller=sadvisor)
            rserializer = RevenueModelSerializer(srevenue)
            r = rserializer.data
            cx.update(r)
        except:
            r = {}
            print('no revenue')

        print(cx)
        # cx.update(z)
        data={}
        data['seller'] = cx
        data['business'] = z
        print(data)

        fdata['cart'].append(data)
    for investor in just_invest:
        serializer = InvestorSerializer(investor)
        x = serializer.data
        album_id = investor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Investor'
        }
        itype = investor.type

        imodel = inv_model_list[itype].objects.get(investor=investor)
        iserializer = inv_serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx
        data['business'] = z
        fdata['cart'].append(data)
    for advisor in just_advise:
        serializer = AdvisorSerializer(advisor)
        x = serializer.data
        album_id = advisor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Advisor'
        }
        itype = advisor.type

        imodel = adv_model_list[itype].objects.get(advisor=advisor)
        iserializer = adv_serializer_list[itype](imodel)
        z = iserializer.data
        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx
        data['business'] = z
        fdata['cart'].append(data)

    random.shuffle(fdata['cart'])
    fdata['list']=[]
    user_sell = user.profile.user_sell.all()
    user_advise = user.profile.user_advise.all()
    user_invest = user.profile.user_invest.all()

    for sell in user_sell:
        sadvisor = sell.seller
        # print('debug start')
        # print(sadvisor)
        serializer = SellerSerializer(sadvisor)
        x = serializer.data
        print(x)
        album_id = sadvisor.album_id
        print(album_id)
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Seller'
        }
        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx
        fdata['list'].append(data)
    for advise in user_advise:
        advisor = advise.advisor
        serializer = AdvisorSerializer(advisor)
        x = serializer.data
        album_id = advisor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Advisor'
        }

        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx

        fdata['list'].append(data)
    for invest in user_invest:
        investor=invest.investor
        serializer = InvestorSerializer(investor)
        x = serializer.data
        album_id = investor.album_id
        album = KAlbumForFile.objects.get(album_id=album_id)
        file = album.files.all()[0]
        file_name = file.name
        y = {
            'file_name': file_name,
            'base_type': 'Investor'
        }

        cx = x.copy()
        cx.update(y)
        # cx.update(z)
        data = {}
        data['seller'] = cx

        fdata['list'].append(data)

    return render(request, 'seller1/buyer-profile.html', fdata)

@login_required(login_url='profiles:index')
def save_view(request):
    if request.method=='GET':
        user = request.user
        duration = request.GET['duration']
        duration = float(duration)
        base_type = request.GET['base_type']
        type = request.GET['type']
        id = request.GET['id']
        category = request.GET['category']
        time_spent = datetime.fromtimestamp(int(duration))
        view = View_log()
        view.time_spent = time_spent
        view.base_type=base_type
        view.type=type
        view.category=category
        view.id=id
        view.save()
        user.profile.views.add(view)
        user.save()

def unlock_premium(request):
    if request.method=='GET':
        business_id = request.GET['seller_id']
        base_type = request.GET['base_type']
        if base_type=='Seller':
            seller = Seller1.objects.get(business_id=business_id)
            sell = Sell.objects.get(seller=seller)
            user=request.user
            user.profile.sell_unlocks.add(sell)
            user.save()
            data={}
            data['status']='valid'
            return JsonResponse(data)
        if base_type=='Advisor':
            seller = Advisor.objects.get(advisor_id=business_id)
            sell = Advise.objects.get(advisor=seller)
            user=request.user
            user.profile.advise_unlocks.add(sell)
            user.save()
            data={}
            data['status']='valid'
            return JsonResponse(data)
        if base_type=='Investor':
            seller = Investor.objects.get(investor_id=business_id)
            sell = Invest.objects.get(investor=seller)
            user=request.user
            user.profile.invest_unlocks.add(sell)
            user.save()
            data={}
            data['status']='valid'
            return JsonResponse(data)