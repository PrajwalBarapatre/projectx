from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.conf import settings
import random
from itertools import chain
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
import os, shutil, errno
import glob
from django.conf import settings
from seller1.serializers import AblumSerializer
from album.models import KAlbumForFile
from album.serializers import KAblumSerializer, FileSerializer
from django.contrib.auth.decorators import login_required
from advisor.models import Advisor, BusinessAdvisor, StartupAdvisor
from advisor.forms import AdvisorForm, AdvisorUpdateForm, BusinessUpdateForm, BusinessForm, StartupForm, StartupUpdateForm
from investor.models import IndividualInvestor, CompanyInvestor, Investor
from investor.forms import IndividualForm, CompanyForm, InvestorForm, IndividualUpdateForm, CompanyUpdateForm, InvestorUpdateForm
from .serializers import BusinessSerializer, StartupSerializer
from user_seller.models import Sell, Invest, Advise

from seller1.serializers import SellerSerializer, RevenueModelSerializer, serializer_list
from advisor.serializers import AdvisorSerializer
# from investor.serializers import InvestorSerializer
from user_seller.views import make_invest, make_sell, make_advise
from investor.models import IndividualInvestor, CompanyInvestor, Investor
from investor.forms import IndividualForm, CompanyForm, InvestorForm, IndividualUpdateForm, CompanyUpdateForm, InvestorUpdateForm
from investor.serializers import IndividualSerializer, CompanySerializer, InvestorSerializer
# from investor.views import inv_serializer_list, inv_model_list



inv_model_list = {
    'Individual': IndividualInvestor,
    'Company': CompanyInvestor
}

inv_serializer_list = {
    'Individual': IndividualSerializer,
    'Company': CompanySerializer
}


model_list = {
    'Business': SellBusiness,
    'Asset': SellAsset,
    'Loan': RaiseLoan,
    'Equity': SellEquity,
    'Startup': SellStartup,
    'Ipcode': SellIpcode,
    'Application': SellApp
}

adv_model_list = {
    'Business': BusinessAdvisor,
    'Startup': StartupAdvisor
}

adv_serializer_list = {
    'Business': BusinessSerializer,
    'Startup': StartupSerializer
}


def BusinessUpdate(request, business_id):
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        # 'country_code_primary': 'country_code_primary',
        'website': 'website',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller': 'about_seller',
        'professional_link': 'professional_link',
        'portfolio_website':'portfolio_website', 
    }
    # if request.method == 'POST':
    business_id = business_id
    business_instance = get_object_or_404(BusinessAdvisor, business_id=business_id)
    ktype = business_instance.type
    # ktype='Business'
    seller_id = business_instance.advisor.advisor_id
    seller_instance = get_object_or_404(Advisor, advisor_id=seller_id)
    # revenue_instance = get_object_or_404(RevenueModel, seller=seller_instance)
    business_form = AdvisorUpdateForm(request.POST or None, instance=seller_instance)
    advisor_busi = BusinessUpdateForm(request.POST or None, instance=business_instance)
    # rev_form = RevenueModelUpdateForm(request.POST or None, instance=revenue_instance)
    if business_form.is_valid() and advisor_busi.is_valid():
        print('inside if 1')
        instance_seller = business_form.save(commit=False)
        print('inside if 2')
        instance_seller.save()
        print('inside if 3')
        instance_bsn = advisor_busi.save(commit=False)
        print('inside if 4')
        instance_bsn.save()
        # instance_rev = rev_form.save(commit=False)
        # instance_rev.save()
        # instance_rev.seller = instance_seller
        # # instance_rev.save()
        # print('rev done')
        instance_bsn.advisor=instance_seller
        instance_bsn.type=ktype
        instance_seller.type=ktype
        instance_bsn.save()
        instance_seller.save()
        print('inside if 5')
        return redirect('advisor:advisor-user-detail', business_id=instance_seller.advisor_id)
    else:
        print(business_form.errors)
        print(advisor_busi.errors)
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
        'years_exp': 'years_exp',
        'hour_fee': 'hour_fee',
        'total_advised':'total_advised',

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
        'advisor_busi': advisor_busi,
        'type_fields': type_fields,
        'files': files,
        'seller':seller_instance,
        'business':business_instance,
        'seller_id': seller_id,
        'revenue_fields': revenue_fields,
        # 'rev_form':rev_form
    }
    return render(request, 'advisor/updatebusi.html', context)




def advisor_busi(request):
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        # 'country_code_primary': 'country_code_primary',
        'website': 'website',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller': 'about_seller',
        'professional_link': 'professional_link',
        'portfolio_website':'portfolio_website', 
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
            seller = AdvisorForm(request.POST)
            business = BusinessForm(request.POST)
            # revenue = RevenueModelForm(request.POST)
            print('submit is done')
            #      print("posting")
            #       print(seller.is_valid())
            if seller.is_valid() and business.is_valid():
                print('everythin is valid')
                seller_1 = seller.save(commit=False)
                #       print(seller)
                seller_1.save()
                seller_1.type = 'Business'
                seller_1.save()
                id = seller_1.advisor_id
                print(id)

                print('seller is done')
                business_1 = business.save(commit=False)
                # business_1=business.save()
                business_1.advisor = seller_1
                business_1.type = 'Business'
                business_1.save()
                print('business is also done')
                user = request.user
                user.profile.advise_type.add(seller_1)
                user.save()
                sell = make_advise(seller_1.advisor_id)
                curr_user = request.user
                # curr_user.profile.advise_type.add(seller_1)
                curr_user.profile.user_advise.add(sell)
                curr_user.save()
                # revenue_1 = revenue.save(commit=False)
                # revenue_1.seller = seller_1
                # revenue_1.save()
                # print('revenue is also done')
                return redirect('advisor:advisor-user-detail', business_id=seller_1.advisor_id)

            else:
                print(seller.errors)
                print(business.errors)

        sectors = business_sector()
        types_companies = companies()
        code_data = codedata()
        business_form = AdvisorForm()
        advisor_busi = BusinessForm()
        rev_form = RevenueModelForm()
        type_fields = {
            'about': 'about',
            'years_exp': 'years_exp',
            'hour_fee': 'hour_fee',
            'total_advised':'total_advised',

        }
        context = {
            'sectors': sectors,
            'types_companies': types_companies,
            'model_fields': model_fields,
            'code_data': code_data,
            'business_form': business_form,
            'year_data': yeardata,
            'text_fields': text_fields,
            'advisor_busi': advisor_busi,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form

        }
        return render(request, 'advisor/advisorbusi.html', context)

    else:
        return redirect('seller1/sellapp.html')

def validate(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = AdvisorForm()
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

def validate_busi(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = BusinessForm()
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


def validate_startup(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = StartupForm()
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


def UpdateFiles(request):
    seller_id = request.GET['seller_id']
    seller=Advisor.objects.get(advisor_id=seller_id)
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





def StartupUpdate(request, business_id):
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        # 'country_code_primary': 'country_code_primary',
        'website': 'website',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller': 'about_seller',
        'professional_link': 'professional_link',
        'portfolio_website':'portfolio_website', 
    }
    # if request.method == 'POST':
    business_id = business_id
    business_instance = get_object_or_404(StartupAdvisor, startup_id=business_id)
    ktype = business_instance.type
    # ktype='Business'
    seller_id = business_instance.advisor.advisor_id
    seller_instance = get_object_or_404(Advisor, advisor_id=seller_id)
    # revenue_instance = get_object_or_404(RevenueModel, seller=seller_instance)
    business_form = AdvisorUpdateForm(request.POST or None, instance=seller_instance)
    advisor_startup = StartupUpdateForm(request.POST or None, instance=business_instance)
    # rev_form = RevenueModelUpdateForm(request.POST or None, instance=revenue_instance)
    if business_form.is_valid() and advisor_startup.is_valid():
        print('inside if 1')
        instance_seller = business_form.save(commit=False)
        print('inside if 2')
        instance_seller.save()
        print('inside if 3')
        instance_bsn = advisor_startup.save(commit=False)
        print('inside if 4')
        instance_bsn.save()
        # instance_rev = rev_form.save(commit=False)
        # instance_rev.save()
        # instance_rev.seller = instance_seller
        # # instance_rev.save()
        # print('rev done')
        instance_bsn.advisor=instance_seller
        instance_bsn.type=ktype
        instance_seller.type=ktype
        instance_bsn.save()
        instance_seller.save()
        print('inside if 5')
        return redirect('advisor:advisor-user-detail', business_id=instance_seller.advisor_id)
    else:
        print(business_form.errors)
        print(advisor_startup.errors)
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
        'years_exp': 'years_exp',
        'hour_fee': 'hour_fee',
        'total_advised':'total_advised',
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
        'advisor_startup': advisor_startup,
        'type_fields': type_fields,
        'files': files,
        'seller':seller_instance,
        'business':business_instance,
        'seller_id': seller_id,
        'revenue_fields': revenue_fields,
        # 'rev_form':rev_form
    }
    return render(request, 'advisor/updatestartup.html', context)


def advisor_startup(request):
    model_fields = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email_adress': 'email_adress',
        'phone_number_primary': 'phone_number_primary',
        # 'country_code_primary': 'country_code_primary',
        'website': 'website',
        'title': 'title',
        'about_business': 'about_business',
        # 'about_seller': 'about_seller',
        'professional_link': 'professional_link',
        'portfolio_website':'portfolio_website',  
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
            seller = AdvisorForm(request.POST)
            business = StartupForm(request.POST)
            # revenue = RevenueModelForm(request.POST)
            print('submit is done')
            #      print("posting")
            #       print(seller.is_valid())
            if seller.is_valid() and business.is_valid():
                print('everythin is valid')
                seller_1 = seller.save(commit=False)
                #       print(seller)
                seller_1.save()
                seller_1.type = 'Startup'
                seller_1.save()
                id = seller_1.advisor_id
                print(id)

                print('seller is done')
                business_1 = business.save(commit=False)
                # business_1=business.save()
                business_1.advisor = seller_1
                business_1.type = 'Startup'
                business_1.save()
                print('business is also done')
                user = request.user
                user.profile.advise_type.add(seller_1)
                user.save()
                sell = make_advise(seller_1.advisor_id)
                curr_user = request.user
                # curr_user.profile.advise_type.add(seller_1)
                curr_user.profile.user_advise.add(sell)
                curr_user.save()
                # revenue_1 = revenue.save(commit=False)
                # revenue_1.seller = seller_1
                # revenue_1.save()
                # print('revenue is also done')
                return redirect('advisor:advisor-user-detail', business_id=seller_1.advisor_id)

            else:
                print(seller.errors)
                print(business.errors)

        sectors = business_sector()
        types_companies = companies()
        code_data = codedata()
        business_form = AdvisorForm()
        advisor_startup = StartupForm()
        rev_form = RevenueModelForm()
        type_fields = {
            'about': 'about',
            'years_exp': 'years_exp',
            'hour_fee': 'hour_fee',
            'total_advised':'total_advised',

        }
        context = {
            'sectors': sectors,
            'types_companies': types_companies,
            'model_fields': model_fields,
            'code_data': code_data,
            'business_form': business_form,
            'year_data': yeardata,
            'text_fields': text_fields,
            'advisor_startup': advisor_startup,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form

        }
        return render(request, 'advisor/advisorstartup.html', context)

    else:
        return redirect('seller1/sellapp.html')


def AdvisorBusiDelete(request, business_id):
    bsn_id = business_id
    bsn = BusinessAdvisor.objects.get(business_id=bsn_id)
    seller_id = bsn.advisor.advisor_id
    seller = Advisor.objects.get(advisor_id=seller_id)

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

def AdvisorStartupDelete(request, business_id):
    bsn_id = business_id
    bsn = StartupAdvisor.objects.get(startup_id=bsn_id)
    seller_id = bsn.advisor.advisor_id
    seller = Advisor.objects.get(advisor_id=seller_id)

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


def detail_advise_type(request, business_id):
    seller = Advisor.objects.get(advisor_id=business_id)
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
    if seller.trial:
        seller.trial = False
        seller.save()
    fdata = {}
    fdata['seller'] = cdata
    fdata['business'] = sdata
    fdata['inst_invest'] = []
    fdata['inst_seller'] = []
    fdata['cart_invest'] = []
    fdata['cart_seller'] = []
    inst_invest = sell.inst_invest.all()
    inst_seller = sell.inst_seller.all()
    cart_investor = sell.cart_invest.all()
    cart_seller = sell.cart_seller.all()
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
        # cx.update(z)
        data = {}
        data['seller'] = cx
        data['business'] = z
        fdata['inst_invest'].append(data)

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
        # cx.update(z)
        data = {}
        data['seller'] = cx
        data['business'] = z
        fdata['cart_invest'].append(data)

    for sadvisor in inst_seller:
        serializer = SellerSerializer(sadvisor)
        x = serializer.data
        album_id = sadvisor.album_id
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
        r = None
        try:
            srevenue = RevenueModel.objects.get(seller=sadvisor)
            rserializer = RevenueModelSerializer(srevenue)
            r = rserializer.data
            cx.update(r)
        except:
            r = {}
            print('no revenue')
        # cx.update(z)
        data = {}
        data['seller'] = cx
        data['business'] = z
        fdata['inst_seller'].append(data)
    print(fdata['cart_seller'])
    for sadvisor in cart_seller:
        print('debug start')
        print(sadvisor)
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
        print('check cart_seller')
        print(fdata['cart_seller'])
        fdata['cart_seller'].append(data)
    print(fdata['cart_seller'])
    print('debug finish')

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

    print(fdata)
    fdata['cart'] = []
    fdata['inst'] = []
    fdata['cart'] = list(chain(fdata['cart_invest'], fdata['cart_seller']))
    print('adjvhb')
    print(fdata['cart'])
    random.shuffle(fdata['cart'])
    print(fdata['cart'])
    fdata['inst'] = list(chain(fdata['inst_invest'], fdata['inst_seller']))
    print(fdata['inst'])
    random.shuffle(fdata['cart'])
    print(fdata['inst'])
    print(fdata['cart'])
    fdata['jcart']=[]
    fdata['jcart']=json.dumps((fdata['cart']))
    print(cart_seller)
    return render(request, 'advisor/sell_detail.html', fdata)


def just_advise_type(request, business_id):
    seller = Advisor.objects.get(advisor_id=business_id)
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
    fdata['seller'] = cdata
    fdata['business'] = sdata
    fdata['inst_invest'] = []
    fdata['inst_seller'] = []
    fdata['cart_invest'] = []
    fdata['cart_seller'] = []
    inst_invest = sell.inst_invest.all()
    inst_seller = sell.inst_seller.all()
    cart_investor = sell.cart_invest.all()
    cart_seller = sell.cart_seller.all()


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
    fdata['cart']=[]
    fdata['inst']=[]
    fdata['cart'] = list(chain(fdata['cart_invest'], fdata['cart_seller']))
    print('adjvhb')
    print(fdata['cart'])
    random.shuffle(fdata['cart'])
    print(fdata['cart'])
    fdata['inst'] = list(chain(fdata['inst_invest'], fdata['inst_seller']))
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

    advisors = user.profile.advise_type.all()
    for advisor in advisors:
        asreializer = AdvisorSerializer(advisor)
        data_advisors.append(asreializer.data)
    # if advisors is not None:
    #     data_advisors= AdvisorSerializer(advisors, many=True)
    print(data_advisors)
    just_sell = user.profile.just_advise.all()
    all_jsell = []
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
        all_hsell_advisor[name] = []
        for one_advisor in sell_advisors:
            done_advisor = AdvisorSerializer(one_advisor).data
            all_hsell_advisor[name].append(done_advisor)
    advises = user.profile.user_advise.all()
    all_aisell = {}
    all_aisell['startup'] = []
    all_aisell['business'] = []
    all_advise = {}
    for advise in advises:
        if advise.type == 'Startup':
            all_advise['startup'] = AdvisorSerializer(advise.advisor).data
        if advise.type == 'Business':
            all_advise['business'] = AdvisorSerializer(advise.advisor).data

    fdata['data_investor']= json.dumps(data_investor)

    fdata['data_advisors']= json.dumps(all_advise)
    fdata['just_advisors']= json.dumps(all_jsell)
    fdata['invest_advisors']= json.dumps(all_isell)
    fdata['my_sellers']= json.dumps(all_hsell)
    fdata['sellers_advisors']= json.dumps(all_hsell_advisor)
    fdata['similar_seller']=[]
    similar_seller = Advisor.objects.filter(type=stype)
    for advisor in similar_seller:
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
        fdata['similar_seller'].append(cx)
    print(fdata)
    return render(request, 'advisor/detail.html', fdata)