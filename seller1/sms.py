# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from random import randint
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import string
import secrets
from django.contrib.auth.models import User
from profiles.models import Profile
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure


def generateSecureRandomString(stringLength=10):
    """Generate a secure random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(password_characters) for i in range(stringLength))

def otp_message(request):
    account_sid = 'ACd50fe123ff4c24314ca2b6ac63c3d350'
    auth_token = '858bf3236bc7b1d97b4a9290b6da524d'
    client = Client(account_sid, auth_token)
    number = request.GET['number']
    name = request.GET['name']
    otp = randint(1000,9999)
    body=""
    if name:
        body="Hii "+ name +", verify your business contact number using this "+ str(otp)
    else:
        body="Hii, "+", verify your business contact number using this "+ str(otp)
    try:
        message = client.messages \
            .create(
            body=body,
            from_='+14806463893',
            to=number
        )
    except:
        data = {}
        data['status'] = 'invalid'
        return JsonResponse(data=data, safe=False)
    print(message.sid)
    data={}
    data['status']='success'
    data['number']=number
    data['otp']=otp
    print(data)
    return JsonResponse(data=data, safe=False)


def email_message(request):
    subject = "Email Verification Business Verge"

    email = request.GET['email']
    name = request.GET['name']
    otp = randint(1000,9999)
    body=""
    hbody=""
    if name:
        body="Hii "+", verify your business email address using this   "+ str(otp)
        hbody='<p>Hii '+', verify your business email address using this <strong>'+ str(otp)+'</strong></p>'
    else:
        body = "Hii " + ", verify your business email address using this   " + str(otp)
        hbody = '<p>Hii ' + ', verify your business email address using this <strong>' + str(otp) + '</strong></p>'

    # send_mail(subject, body, 'businessmerge@gmail.com', [email], fail_silently=False)
    msg = EmailMultiAlternatives(subject, body, 'admin@bverge.com', [email])
    msg.attach_alternative(hbody, "text/html")
    msg.send()
    # print(message.sid)
    data={}
    data['status']='success'
    data['email']=email
    data['otp']=otp
    print(data)
    return JsonResponse(data=data, safe=False)

def email_forgot(request):
    subject = "Business Verge OTP for New Password"
    user=None
    email = request.GET['email']
    found=False
    try:
        user=User.objects.get(email=email)

        if(user.profile.social):
            print('found but social')
            found=False
            data={}
            data['status']='invalid'
            return JsonResponse(data, safe=False)
        else:
            print('found')
            found=True
    except:
        print('not found')
        data = {}
        data['status'] = 'invalid'
        return JsonResponse(data, safe=False)
    if(found):
        try:
            otp = generateSecureRandomString()
            body=""
            hbody=""
            body = "Hii " + ", use this otp to make a new password" + str(otp)
            hbody = '<p>Hii ' + ', use this otp to make a new password <strong>' + str(otp) + '</strong></p>'


            # send_mail(subject, body, 'businessmerge@gmail.com', [email], fail_silently=False)
            msg = EmailMultiAlternatives(subject, body, 'admin@bverge.com', [email])
            msg.attach_alternative(hbody, "text/html")
            msg.send()
            user.profile.otp=otp
            user.save()
            # print(message.sid)
            data={}
            data['status']='success'
            print(data)
            return JsonResponse(data=data, safe=False)
        except:
            print('found but failed to send message')
            data = {}
            data['status'] = 'invalid'
            return JsonResponse(data, safe=False)
    else:
        print('dunno how this came')
        data = {}
        data['status'] = 'invalid'
        return JsonResponse(data, safe=False)

def forgot_password(request):
    if request.method=='POST':
        otp = request.POST['otp']
        password = request.POST['password']
        con_password = request.POST['con_password']
        email = request.POST['email']

        if(password==con_password and otp!='' and email!=''):
            found = False
            user = None
            try:
                user=User.objects.get(email=email)
                if(user.profile.social):
                    print('found but social')
                    data = {}
                    data['status'] = 'invalid'
                    return JsonResponse(data, safe=False)
                else:
                    print('found')
                    found=True
            except:
                print('not found')
                data = {}
                data['status'] = 'invalid'
                return JsonResponse(data, safe=False)
            if(found):
                if(otp==user.profile.otp):
                    print('found and otp is right')
                    user.set_password(password)
                    user.save()
                    data = {}
                    data['status'] = 'success'
                    print(data)
                    return JsonResponse(data=data, safe=False)
                else:
                    print('found but wrong otp')
                    data = {}
                    data['status'] = 'invalid'
                    return JsonResponse(data, safe=False)
            else:
                print('how did this come')
                data = {}
                data['status'] = 'invalid'
                return JsonResponse(data, safe=False)
        else:
            print('parameters are wrong')
            data = {}
            data['status'] = 'invalid'
            return JsonResponse(data, safe=False)


def check_email_otp(request):
    subject = "Email Verification Business Verge"

    email = request.GET['email']
    name = ''
    try:
        if request.GET['first_name']:
            name = ''+ request.GET['first_name'] +' '+ request.GET['last_name']
    except:
        pass
    otp = randint(1000, 9999)
    body = ""
    hbody = ""
    if name:
        body = "Hii " +name+ ", verify your email address using this   " + str(otp)
        hbody = '<p>Hii ' +name+ ', verify your email address using this <strong>' + str(otp) + '</strong></p>'
    else:
        body = "Hii " + ", verify your email address using this   " + str(otp)
        hbody = '<p>Hii ' + ', verify your email address using this <strong>' + str(otp) + '</strong></p>'

    # send_mail(subject, body, 'businessmerge@gmail.com', [email], fail_silently=False)

    msg = EmailMultiAlternatives(subject, body, 'admin@bverge.com', [email])
    msg.attach_alternative(hbody, "text/html")
    msg.send()
    # print(message.sid)
    data = {}
    data['status'] = 'success'
    data['email'] = email
    data['otp'] = otp
    print(data)
    return JsonResponse(data=data, safe=False)