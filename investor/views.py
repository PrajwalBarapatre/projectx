from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.conf import settings
from sorl.thumbnail import get_thumbnail
from django.core.files.uploadedfile import UploadedFile
import json
import random
from itertools import chain
import requests
from django.urls import reverse
from rest_framework.response import Response
from metadata.views import business_sector, companies,codedata,yeardata
from seller1.models import Seller1, Ablumfiles, SellBusiness, RevenueModel, \
    SellAsset, SellEquity, RaiseLoan, SellStartup, SellApp, SellIpcode, SellFranchise, Supplier
from seller1.forms import \
    SellerForm, BusinessForm, SellerUpdateForm, BusinessUpdateForm, \
    RevenueModelForm, RevenueModelUpdateForm, AssetForm, AssetUpdateForm,\
    EquityForm, EquityUpdateForm, LoanForm, LoanUpdateForm,\
    StartupForm, StartupUpdateForm, AppForm, AppUpdateForm, IpcodeForm, IpcodeUpdateForm
from album.models import File
from advisor.views import adv_model_list, adv_serializer_list
from django.core.exceptions import ValidationError
from django.http import JsonResponse
import os, shutil, errno
import glob
from django.conf import settings
from seller1.serializers import AblumSerializer
from album.models import KAlbumForFile
from album.serializers import KAblumSerializer, FileSerializer
from django.contrib.auth.decorators import login_required
from seller1.models import Seller1,Ablumfiles, SellBusiness, RevenueModel,\
    SellAsset, SellEquity, RaiseLoan, SellStartup, SellApp, SellIpcode
from investor.models import IndividualInvestor, CompanyInvestor, Investor
from investor.forms import IndividualForm, CompanyForm, InvestorForm, IndividualUpdateForm, CompanyUpdateForm, InvestorUpdateForm
from investor.serializers import IndividualSerializer, CompanySerializer, InvestorSerializer
from user_seller.models import Sell, Invest, Advise
from seller1.serializers import serializer_list
from seller1.serializers import SellerSerializer, RevenueModelSerializer
from advisor.serializers import AdvisorSerializer, BusinessSerializer, StartupSerializer
from user_seller.views import make_invest, make_sell, make_advise




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


inv_model_list = {
    'Individual': IndividualInvestor,
    'Company': CompanyInvestor
}

inv_serializer_list = {
    'Individual': IndividualSerializer,
    'Company': CompanySerializer
}



@login_required(login_url='profiles:index')
def IndividualUpdate(request, business_id):
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
        'total_invested': 'total_invested',
        # 'address_line': 'address_line',
    }
    # if request.method == 'POST':
    business_id = business_id
    business_instance = get_object_or_404(IndividualInvestor, individual_id=business_id)
    ktype = business_instance.type
    # ktype='Business'
    seller_id = business_instance.investor.investor_id
    seller_instance = get_object_or_404(Investor, investor_id=seller_id)
    sell = Invest.objects.get(investor=seller_instance)
    user = request.user
    user_sells = user.profile.user_invest.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    # revenue_instance = get_object_or_404(RevenueModel, seller=seller_instance)
    business_form = InvestorUpdateForm(request.POST or None, instance=seller_instance)
    invest_indiv = IndividualUpdateForm(request.POST or None, instance=business_instance)
    # rev_form = RevenueModelUpdateForm(request.POST or None, instance=revenue_instance)
    if business_form.is_valid() and invest_indiv.is_valid():
        print('inside if 1')
        instance_seller = business_form.save(commit=False)
        print('inside if 2')
        instance_seller.save()
        print('inside if 3')
        instance_bsn = invest_indiv.save(commit=False)
        print('inside if 4')
        instance_bsn.save()
        # instance_rev = rev_form.save(commit=False)
        # instance_rev.save()
        # instance_rev.seller = instance_seller
        # # instance_rev.save()
        # print('rev done')
        instance_bsn.investor=instance_seller
        instance_bsn.type=ktype
        instance_seller.type=ktype
        instance_bsn.save()
        instance_seller.save()
        print('inside if 5')
        return redirect('investor:investor-user-detail', business_id=instance_seller.investor_id)
    else:
        print(business_form.errors)
        print(invest_indiv.errors)
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
        'looking_for': 'looking_for',
        'investment_bracket': 'investment_bracket',
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
        'invest_indiv': invest_indiv,
        'type_fields': type_fields,
        'files': files,
        'seller':seller_instance,
        'business':business_instance,
        'seller_id': seller_id,
        'revenue_fields': revenue_fields,
        # 'rev_form':rev_form
    }
    return render(request, 'investor/updateindiv.html', context)



@login_required(login_url='profiles:index')
def investor_indiv(request):
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
        'total_invested':'total_invested',
        # 'address_line': 'address_line',
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
            seller = InvestorForm(request.POST)
            business = IndividualForm(request.POST)
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
                seller_1.type = 'Individual'
                seller_1.save()
                id = seller_1.investor_id
                print(id)

                print('seller is done')
                business_1 = business.save(commit=False)
                # business_1=business.save()
                business_1.investor = seller_1
                business_1.type = 'Individual'
                business_1.save()
                print('business is also done')
                user = request.user
                user.profile.invest_type=seller_1
                user.save()
                sell = make_invest(seller_1.investor_id)
                curr_user = request.user
                # curr_user.profile.advise_type.add(seller_1)
                curr_user.profile.user_invest.add(sell)
                curr_user.save()
                # revenue_1 = revenue.save(commit=False)
                # revenue_1.seller = seller_1
                # revenue_1.save()
                # print('revenue is also done')
                return redirect('investor:investor-user-detail', business_id=seller_1.investor_id)

            else:
                print(seller.errors)

        sectors = business_sector()
        types_companies = companies()
        code_data = codedata()
        business_form = InvestorForm()
        invest_indiv = IndividualForm()
        rev_form = RevenueModelForm()
        type_fields = {
            'about': 'about',
            'looking_for': 'looking_for',
            'investment_bracket': 'investment_bracket',
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
            'invest_indiv': invest_indiv,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form

        }
        return render(request, 'investor/investorindiv.html', context)

    else:
        return redirect('seller1/sellapp.html')

def validate(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = InvestorForm()
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

def validate_indiv(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = IndividualForm()
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


def validate_company(request):
    if request.method == 'GET':
        field_get = request.GET['field']
        field_val = request.GET['value']
        business_form = CompanyForm()
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
    seller=Investor.objects.get(investor_id=seller_id)
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
def CompanyUpdate(request, business_id):
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

        'total_invested': 'total_invested',
        # 'address_line': 'address_line',
    }
    # if request.method == 'POST':
    business_id = business_id
    business_instance = get_object_or_404(CompanyInvestor, company_id=business_id)
    ktype = business_instance.type
    # ktype='Business'
    seller_id = business_instance.investor.investor_id
    seller_instance = get_object_or_404(Investor, investor_id=seller_id)
    sell = Invest.objects.get(investor=seller_instance)
    user = request.user
    user_sells = user.profile.user_invest.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    # revenue_instance = get_object_or_404(RevenueModel, seller=seller_instance)
    business_form = InvestorUpdateForm(request.POST or None, instance=seller_instance)
    invest_company = CompanyUpdateForm(request.POST or None, instance=business_instance)
    # rev_form = RevenueModelUpdateForm(request.POST or None, instance=revenue_instance)
    if business_form.is_valid() and invest_company.is_valid():
        print('inside if 1')
        instance_seller = business_form.save(commit=False)
        print('inside if 2')
        instance_seller.save()
        print('inside if 3')
        instance_bsn = invest_company.save(commit=False)
        print('inside if 4')
        instance_bsn.save()
        # instance_rev = rev_form.save(commit=False)
        # instance_rev.save()
        # instance_rev.seller = instance_seller
        # # instance_rev.save()
        # print('rev done')
        instance_bsn.investor=instance_seller
        instance_bsn.type=ktype
        instance_seller.type=ktype
        instance_bsn.save()
        instance_seller.save()
        print('inside if 5')
        return redirect('investor:investor-user-detail', business_id=instance_seller.investor_id)
    else:
        print(business_form.errors)
        print(invest_company.errors)
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
        'looking_for': 'looking_for',
        'investment_bracket': 'investment_bracket',
        'website': 'website',
        'institution_name': 'institution_name',
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
        'invest_company': invest_company,
        'type_fields': type_fields,
        'files': files,
        'seller':seller_instance,
        'business':business_instance,
        'seller_id': seller_id,
        'revenue_fields': revenue_fields,
        # 'rev_form':rev_form
    }
    return render(request, 'investor/updatecompany.html', context)



@login_required(login_url='profiles:index')
def investor_company(request):
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
        'total_invested':'total_invested',
        # 'address_line': 'address_line',
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
            seller = InvestorForm(request.POST)
            business = CompanyForm(request.POST)
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
                seller_1.type = 'Company'
                seller_1.save()
                id = seller_1.investor_id
                print(id)

                print('seller is done')
                business_1 = business.save(commit=False)
                # business_1=business.save()
                business_1.investor = seller_1
                business_1.type = 'Company'
                business_1.save()
                print('business is also done')
                user = request.user
                user.profile.invest_type = seller_1
                user.save()
                sell = make_invest(seller_1.investor_id)
                curr_user = request.user
                # curr_user.profile.advise_type.add(seller_1)
                curr_user.profile.user_invest.add(sell)
                curr_user.save()
                # revenue_1 = revenue.save(commit=False)
                # revenue_1.seller = seller_1
                # revenue_1.save()
                # print('revenue is also done')
                return redirect('investor:investor-user-detail', business_id=seller_1.investor_id)

            else:
                print(seller.errors)

        sectors = business_sector()
        types_companies = companies()
        code_data = codedata()
        business_form = InvestorForm()
        invest_company = CompanyForm()
        rev_form = RevenueModelForm()
        type_fields = {
            'about': 'about',
            'looking_for': 'looking_for',
            'investment_bracket': 'investment_bracket',
            'website': 'website',
            'institution_name': 'institution_name'
        }
        context = {
            'sectors': sectors,
            'types_companies': types_companies,
            'model_fields': model_fields,
            'code_data': code_data,
            'business_form': business_form,
            'year_data': yeardata,
            'text_fields': text_fields,
            'invest_company': invest_company,
            'type_fields': type_fields,
            'revenue_fields': revenue_fields,
            'rev_form': rev_form

        }
        return render(request, 'investor/investorcompany.html', context)

    else:
        return redirect('seller1/sellapp.html')

@login_required(login_url='profiles:index')
def InvestorIndivDelete(request, business_id):
    bsn_id = business_id
    bsn = IndividualInvestor.objects.get(individual_id=bsn_id)
    seller_id = bsn.investor.investor_id
    seller = Investor.objects.get(investor_id=seller_id)
    sell = Invest.objects.get(investor=seller)
    user = request.user
    user_sells = user.profile.user_invest.all()
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
def InvestorCompanyDelete(request, business_id):
    bsn_id = business_id
    bsn = CompanyInvestor.objects.get(company_id=bsn_id)
    seller_id = bsn.investor.investor_id
    seller = Investor.objects.get(investor_id=seller_id)
    sell = Invest.objects.get(investor=seller)
    user = request.user
    user_sells = user.profile.user_invest.all()
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
def just_invest_type(request, business_id):
    seller = Investor.objects.get(investor_id=business_id)
    sell = Invest.objects.get(investor=seller)
    print(sell)
    stype = sell.type
    smodel = inv_model_list[stype].objects.get(investor=seller)
    sserializer = inv_serializer_list[stype](smodel)
    sdata = sserializer.data
    serializer = InvestorSerializer(seller)
    data = serializer.data
    cdata = data.copy()
    # cdata.update(sdata)
    main_album_id = seller.album_id
    main_album = KAlbumForFile(album_id=main_album_id)
    main_files = main_album.files.all()
    # srevenue = None
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
    fdata['inst_seller']=[]
    fdata['inst_advisor']=[]
    fdata['cart_seller']=[]
    fdata['cart_advisor']=[]
    inst_seller = sell.inst_seller.all()
    inst_advisor = sell.inst_advisor.all()
    cart_seller = sell.cart_seller.all()
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

    if seller == user.profile.invest_type:
        fdata['same'] = 'True'

    fdata['cart'] = []
    fdata['inst'] = []
    fdata['cart'] = list(chain(fdata['cart_advisor'], fdata['cart_seller']))
    print('adjvhb')
    print(fdata['cart'])
    random.shuffle(fdata['cart'])
    print(fdata['cart'])
    fdata['inst'] = list(chain(fdata['inst_advisor'], fdata['inst_seller']))
    print(fdata['inst'])
    random.shuffle(fdata['cart'])
    print(fdata['inst'])

    user = request.user
    investor = user.profile.user_invest.all()
    # iserializer = None
    # invest = None
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
        asreializer = AdvisorSerializer(advisor.advisor)
        data_advisors.append(asreializer.data)
    # if advisors is not None:
    #     data_advisors= AdvisorSerializer(advisors, many=True)
    print(data_advisors)
    just_sell = user.profile.just_invest.all()
    all_jsell = []
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
        all_hsell_advisor[name] = []
        for one_advisor in sell_advisors:
            done_advisor = InvestorSerializer(one_advisor).data
            all_hsell_advisor[name].append(done_advisor)
    advises = user.profile.user_advise.all()
    all_aisell = {}
    # all_aisell['startup']={}
    # all_aisell['business']={}
    for advise in advises:
        # if advise.type == 'Startup':
        aname = 'advisor_' + str(advise.advisor.advisor_id)
        all_aisell[aname] = InvestorSerializer(advise.cart_invest, many=True).data
        # if advise.type == 'Business':
        #     aname = 'advisor_' + str(advise.advisor.advisor_id)

    fdata['data_investor']= json.dumps(data_investor)
    # 'data_sellers': data_sellers,
    fdata['data_advisors']= json.dumps(data_advisors)
    fdata['just_investors']= json.dumps(all_jsell)
    fdata['advise_investors']= json.dumps(all_aisell)
    fdata['my_sellers']= json.dumps(all_hsell)
    fdata['sellers_investors']= json.dumps(all_hsell_advisor)

    # similar_seller = Investor.objects.filter(type=stype)
    similar_sell = Invest.objects.all()
    fdata['similar_seller']=[]
    for similar_seller in similar_sell:
        investor = similar_seller.investor
        if seller == investor:
            continue
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
        fdata['similar_seller'].append(data)

    print(fdata)
    return render(request, 'investor/detail.html', fdata)

@login_required(login_url='profiles:index')
def detail_invest_type(request, business_id):
    seller = Investor.objects.get(investor_id=business_id)
    sell = Invest.objects.get(investor=seller)
    user = request.user
    user_sells = user.profile.user_invest.all()
    found = False
    for each_sell in user_sells:
        if each_sell == sell:
            found = True
            break
    if not found:
        return redirect('profiles:index')
    sell = Invest.objects.get(investor=seller)
    print(sell)
    stype = sell.type
    smodel = inv_model_list[stype].objects.get(investor=seller)
    sserializer = inv_serializer_list[stype](smodel)
    sdata = sserializer.data
    serializer = InvestorSerializer(seller)
    data = serializer.data
    cdata = data.copy()
    # cdata.update(sdata)
    main_album_id = seller.album_id
    main_album = KAlbumForFile(album_id=main_album_id)
    main_files = main_album.files.all()
    # srevenue = None
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
    fdata['inst_seller'] = []
    fdata['inst_advisor'] = []
    fdata['cart_seller'] = []
    fdata['cart_advisor'] = []
    inst_seller = sell.inst_seller.all()
    inst_advisor = sell.inst_advisor.all()
    cart_seller = sell.cart_seller.all()
    cart_advisor = sell.cart_advisor.all()
    for investor in inst_seller:
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

    for investor in cart_seller:
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
        fdata['cart_seller'].append(data)

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
        # cx.update(z)
        data = {}
        data['seller'] = cx
        data['business'] = z
        fdata['inst_advisor'].append(data)
        # fdata['inst_advisor'].append(cx)

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
        data = {}
        data['seller'] = cx
        data['business'] = z
        # fdata['inst_invest'].append(data)
        fdata['cart_advisor'].append(data)

    fdata['images'] = []
    for file in main_files:
        name = file.name
        name_dict = {
            'file_name': name
        }
        fdata['images'].append(name_dict)
    fdata['same'] = 'False'
    user = request.user

    if seller == user.profile.invest_type:
        fdata['same'] = 'True'

    print(fdata)
    fdata['cart'] = []
    fdata['inst'] = []
    fdata['cart'] = list(chain(fdata['cart_advisor'], fdata['cart_seller']))
    print('adjvhb')
    print(fdata['cart'])
    random.shuffle(fdata['cart'])
    print(fdata['cart'])
    fdata['inst'] = list(chain(fdata['inst_advisor'], fdata['inst_seller']))
    print(fdata['inst'])
    random.shuffle(fdata['cart'])
    print(fdata['inst'])
    print(fdata)
    return render(request, 'investor/sell_detail.html', fdata)
