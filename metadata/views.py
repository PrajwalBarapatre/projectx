from django.shortcuts import render
from .models import BusinessSectors, company,codes,years,currency
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
import json
from django.http import JsonResponse
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

# Create your views here.
def business_sector():
    data = BusinessSectors.objects.values('sectors').distinct()
    print(data)
    # print("yolo")
    # print(data)
    return data

def companies():
    data = company.objects.all()
    # print("yolo")
    # print(data)
    return data

def codedata():
    data = codes.objects.all()
    # print("yolo")
    # print(data)
    return data

def yeardata():
    data = years.objects.all()
    # print("yolo")
    # print(data)
    return data


def get_sub_sector(request):
    print("zjajaj")
    if request.is_ajax():
        sector = BusinessSectors.objects.filter(sectors=request.GET.get('sector', ''))
        html = render_to_string('metadata/sub_sectors.html', locals())
        return HttpResponse(html)
        # print("yolo")
        # for x in sector:
        #     print(x.sub_sectors)

@csrf_exempt
def currencydata(request):
    if request.is_ajax():
        sector = currency.objects.all()
        html = render_to_string('metadata/currency.html', locals())
        return HttpResponse(html)



@csrf_exempt
def session_storage(request):
    # if request.is_ajax():
    #     print(request)
    #     return HttpResponse("ajax ok")
    print("dfffdfdfdfdfd")
    print(request.session.has_key("lastname")) 
    return HttpResponse("ok")
