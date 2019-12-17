from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
import json
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Notification
from profiles.forms import UserLoginForm, UserRegisterForm, ProfileForm
from django.http import JsonResponse
from metadata.views import business_sector, companies,codedata,yeardata
from .serializers import UserSerializer, ProfileSerializer
from chat.models import Chat, Contact, Notify
from chat.views import get_user_contact, get_chat
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


def login_view(request):
    try:
        form = UserLoginForm(request.POST or None)
    except:
        data = {}
        data['status'] = 'invalid'
        # data['img_name'] = name
        print(data)
        # return redirect('seller1:seller')
        return JsonResponse(data, safe=False)
    try:
        if form.is_valid():

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                username = User.objects.get(email=email.lower()).username
            except:
                data={}
                data['status'] = 'invalid'
                # data['img_name'] = name
                print(data)
                # return redirect('seller1:seller')
                return JsonResponse(data, safe=False)
            try:
                user = authenticate(username=username, password=password)
            except:
                data={}
                data['status'] = 'invalid'
                # data['img_name'] = name
                print(data)
                # return redirect('seller1:seller')
                return JsonResponse(data, safe=False)
            login(request, user)
            data = {}

            name=user.profile.photo.name
            data['status'] ='success'
            data['img_name']=name
            print(data)
            # return redirect('seller1:seller')
            return JsonResponse(data, safe=False)
    except:
        data = {}
        data['status'] = 'invalid'
        # data['img_name'] = name
        print(data)
        # return redirect('seller1:seller')
        return JsonResponse(data, safe=False)

    context = {
        'form': form,
    }
    data={}
    data['status']='no post request made'
    # return render(request, "login.html", context)
    return JsonResponse(data, safe=False)



def register_view(request):
    # next = request.GET.get('next')
    try:
        form = UserRegisterForm(data=request.POST or None)
        profile_form = ProfileForm(data=request.POST, files=request.FILES or None)
    except:
        data = {}
        data['status'] = 'invalid'
        # data['img_name'] = name
        print(data)
        # return redirect('seller1:seller')
        return JsonResponse(data, safe=False)
    if form.is_valid() and profile_form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        user.profile.first_name=profile_form.cleaned_data['first_name']
        print('0')
        user.profile.last_name = profile_form.cleaned_data['last_name']
        print('1')

        try:
            user.profile.contact_number = profile_form.cleaned_data['contact_number']
            print('2')
            user.profile.photo = request.FILES['photo']
            print(request.FILES['photo'])
        except:
            pass
        # user.profile.about_me = profile_form.cleaned_data['about_me']
        print('2')
        try:
            user.profile.country = profile_form.cleaned_data['country']
            print('2')
            user.profile.region = profile_form.cleaned_data['region']
            print('2')
            user.profile.city = profile_form.cleaned_data['city']
            print('2')
            user.profile.lngt = profile_form.cleaned_data['lngt']
            print('2')
            user.profile.lat = profile_form.cleaned_data['lat']
            print('2')
            user.profile.address_line = profile_form.cleaned_data['address_line']
            print('2')
        except:
            pass


        # profile.user = user
        user.save()
        print('3')
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        data = {}
        name = user.profile.photo.name
        data['status'] = 'success'
        data['img_name'] = name
        print(data)
        # return redirect('seller1:seller')
        # return redirect('profiles:signup')
        return JsonResponse(data, safe=False)
    print(profile_form.errors)
    print(form.errors)
    context = {
        'form': form,
        'profile_form': profile_form
    }
    data = {}
    data['status'] = 'no post request made'
    # return render(request, "signup.html", context)
    return JsonResponse(data, safe=False)


def logout_view(request):
    logout(request)
    return redirect('profiles:index')




def home_view(request):
    log_form = UserLoginForm()
    reg_form = UserRegisterForm()
    profile_form = ProfileForm()
    code_data = codedata()
    sectors = business_sector()
    print(sectors)
    notifications=None
    notif_number = None
    try:
        user = request.user
        notifications = user.profile.notifs.all().order_by('-created_at')
        notif_number=0
        for notif in notifications:
            if notif.notif_seen==False:
                notif_number=notif_number+1
    except:
        print('user is not authenticated')
        pass


    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1
    
    context ={
        'log_form': log_form,
        'reg_form': reg_form,
        'profile_form': profile_form,
        'code_data': code_data,
        'sectors': sectors,
        'notifications':notifications,
        'notif_number':notif_number,
        # 'num_visits': num_visits,
    }
    return render(request, "index.html", context)


def notif_data(request):
    notifications=None
    notif_number = None
    try:
        user = request.user
        notifications = user.profile.notifs.all().order_by('-created_at')
        notif_number=0
        for notif in notifications:
            if notif.notif_seen==False:
                notif_number=notif_number+1
    except:
        print('user is not authenticated')
        pass

    fdata = {}
    fdata['notif_number'] = notif_number
    print(notifications)
    fdata['notifications'] = []
    for a in notifications:
        k={'notif_statement':a.notif_statement,
        'notif_type':a.notif_type,
        'notif_on':a.notif_on,
        'created_at':a.created_at,
        'notif_seen':a.notif_seen,
        'notif_id':a.notif_id,
        'notif_on_id':a.notif_on_id
        }
        fdata['notifications'].append(k)

    return JsonResponse(fdata, safe=False)



class getUser(APIView):

    def get(self, request, format=None):
        user = request.user
        serializer =UserSerializer(user)
        serializer2 = ProfileSerializer(user.profile)
        x=serializer.data
        y=serializer2.data
        z=x.copy()
        z.update(y)
        user_contact = get_user_contact(user.username)
        curr_chat = user.profile.curr_chat
        participants = curr_chat.participants.all()
        arr = list(participants)
        arr.remove(user_contact)
        w={}
        w['other_profile_url']=arr[0].user.profile.photo.name
        w['other_name']=''+arr[0].user.profile.first_name + ' ' +arr[0].user.profile.last_name
        w['other_id']=arr[0].contact_id
        w['blocked']=''
        w['photo_name']=user.profile.photo.name
        if curr_chat in arr[0].blocked_chats.all():
            w['blocked']='true'
        contact = get_user_contact(user.username)
        queryset = contact.chats.all()
        now_chat = contact.user.profile.curr_chat
        fdata = {}
        fchats = []
        fother = {}
        print(queryset[0])
        for chat in queryset:
            content = {}
            content['chat_id'] = chat.chat_id
            array = []
            print(chat)
            print(chat.participants.all()[0].user.username)
            for person in chat.participants.all():
                dict = {}
                dict['username'] = person.user.username
                dict['url'] = person.user.profile.photo.name
                if person.user.profile.status:
                    dict['status'] = 'online'
                else:
                    dict['status'] = 'offline'
                array.append(dict)
            content['people'] = array
            content['business_name'] = ''
            notify = Notify.objects.get(contact=contact, chat=chat)
            content['notif_number'] = notify.number
            content['notif_id'] = notify.notify_id

            arr = list(chat.participants.all())
            arr.remove(contact)

            content['other_profile_url'] = arr[0].user.profile.photo.name
            content['other_name'] = '' + arr[0].user.profile.first_name + ' ' + arr[0].user.profile.last_name
            content['other_id'] = arr[0].contact_id
            content['blocked'] = ''
            if chat in arr[0].blocked_chats.all():
                content['blocked'] = 'true'

            print(content)
            fchats.append(content)

        fdata['chats'] = fchats
        fdata['curr'] = fother
        # fdata = json.dumps(fdata)
        print(fdata)
        z.update(w)
        z.update(fdata)
        return Response(z)

def password_confirm(request):
    user = request.user
    username = user.username
    password=request.GET['password']
    if user.check_password(password):
        # authenticate(username=username, password=password)

        data={}
        data['status']='valid'
        return JsonResponse(data, safe=False)
    else:
        data = {}
        data['status']='invalid'
        return JsonResponse(data, safe=False)

def password_change(request):
    if request.method == 'POST':
        password = request.POST['password']
        new_password = request.POST['new_password']
        con_password = request.POST['con_password']
        if con_password != new_password:
            data={}
            data['status'] = 'invalid'
            return JsonResponse(data, safe=False)
        user = request.user
        username = user.username
        try:
            if user.check_password(password):
                user.set_password(new_password)
                user.save()
                data={}
                data['status']='valid'

                return JsonResponse(data, safe=False)
            else:
                data = {}
                data['status'] = 'invalid'
                return JsonResponse(data, safe=False)
        except:
            data = {}
            data['status']='invalid'
            return JsonResponse(data, safe=False)


def check_email(request):
    email = request.GET['email']
    try:
        User.objects.get(email=email)
        data={}
        data['status']='invalid'
        return JsonResponse(data, safe=False)
    except:
        data = {}
        data['status'] = 'success'
        return JsonResponse(data, safe=False)


def check_username(request):
    username = request.GET['username']
    try:
        User.objects.get(username=username)
        data={}
        data['status']='invalid'
        return JsonResponse(data, safe=False)
    except:
        data = {}
        data['status'] = 'success'
        return JsonResponse(data, safe=False)


def edit_profile(request):
    profile_form = ProfileForm(data=request.POST, files=request.FILES or None)
    user = request.user
    if True:
        user.profile.first_name = request.POST['first_name']
        user.profile.last_name = request.POST['last_name']
        try:
            user.profile.contact_number = request.POST['contact_number']
            print(request.POST['contact_number'])
            user.profile.photo = request.FILES['photo']
            print(request.FILES['photo'])
        except:
            print('except from one')
            pass
        # user.profile.about_me = profile_form.cleaned_data['about_me']
        print('2')
        try:
            user.profile.country = request.POST['country']
            print(request.POST['country'])
            user.profile.region = request.POST['region']
            print(request.POST['region'])
            user.profile.city = request.POST['city']
            print(request.POST['city'])

            user.profile.address_line = request.POST['address_line']
            print(request.POST['address_line'])
        except:
            pass

        # profile.user = user
        user.save()
        print('3')

        data = {}

        data['status'] = 'success'

        print(data)
        # return redirect('seller1:seller')
        # return redirect('profiles:signup')
        return JsonResponse(data, safe=False)

def clear_notif(request):
    notifs = Notification.objects.filter(notif_seen=False)
    for notif in notifs:
        notif.notif_seen=True
        notif.save()
    return JsonResponse(data={}, safe=False)


def subscription(request):
    if request.method == 'POST':
        f = SubscriptionForm(request.POST)
        if f.is_valid():
            request.session['subscription_plan'] = request.POST.get('plans')
            return redirect('profiles:process_subscription')
        else:
            print(f.errors)
    else:
        f = SubscriptionForm()
    context = {
        'f': f
    }
    return render(request, 'subscription_form.html', context)


@csrf_exempt
def payment_done(request):
    return render(request, 'payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment_cancelled.html')

def process_subscription(request):
    subscription_plan = request.session.get('subscription_plan')
    host = request.get_host()
    user = request.user
    if subscription_plan == 'trial':
        if user.profile.trial:
            paypal_dict = {
                "cmd": "_xclick-subscriptions",
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                "a1": "0",  # monthly price
                "p1": "1",  # duration of each unit (depends on unit)
                # "t3": billing_cycle_unit,  # duration unit ("M for Month")
                "src": "1",  # make payments recur
                "sra": "1",  # reattempt payment on payment error
                "no_note": "1",  # remove extra notes (optional)
                'item_name': 'Bverge Subscription',
                'custom': {
                    'trial':True,
                    'username': user.username
                },  # custom data, pass something meaningful here
                'currency_code': 'INR',
                'notify_url': 'http://{}{}'.format(host,
                                                   reverse('paypal-ipn')),
                'return_url': 'http://{}{}'.format(host,
                                                   reverse('profiles:payment_done')),
                'cancel_return': 'http://{}{}'.format(host,
                                                      reverse('profiles:payment_canceled')),
            }

            form = PayPalPaymentsForm(initial=paypal_dict, button_type="subscribe")
            context = {
                'form': form
            }
            return render(request, 'process_subscription.html', context)
    price = ""
    billing_cycle = None
    billing_cycle_unit = ""
    if subscription_plan == '1-month':
        price = "10"
        billing_cycle = 1
        billing_cycle_unit = "M"
    elif subscription_plan == '6-month':
        price = "50"
        billing_cycle = 6
        billing_cycle_unit = "M"
    else:
        price = "90"
        billing_cycle = 1
        billing_cycle_unit = "Y"

    paypal_dict = {
        "cmd": "_xclick-subscriptions",
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        "a3": price,  # monthly price
        "p3": billing_cycle,  # duration of each unit (depends on unit)
        "t3": billing_cycle_unit,  # duration unit ("M for Month")
        "src": "1",  # make payments recur
        "sra": "1",  # reattempt payment on payment error
        "no_note": "1",  # remove extra notes (optional)
        'item_name': 'Bverge Subscription',
        'custom': user.username,  # custom data, pass something meaningful here
        'currency_code': 'INR',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('profiles:payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('profiles:payment_canceled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict, button_type="subscribe")
    context={
        'form': form
    }
    return render(request, 'process_subscription.html', context)




