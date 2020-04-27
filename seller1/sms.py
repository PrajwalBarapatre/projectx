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
from staff.models import PhoneModel, EmailModel
import re
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure


def generateSecureRandomString(stringLength=10):
    """Generate a secure random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(password_characters) for i in range(stringLength))

def email_adder(user, email):
    email_model = EmailModel()
    email_model.email = email
    email_model.user = user
    email_model.save()

def phone_adder(user, phone_number, country_code_primary):
    phone_model = PhoneModel()
    phone_model.phone_number = ''+country_code_primary+phone_number
    print(phone_model.phone_number)
    phone_model.country_code_primary = country_code_primary
    phone_model.user = user
    phone_model.save()

def email_checker(user_id, email):
    try:
        client = User.objects.get(id=user_id)
        email_model = EmailModel.objects.get(user=client, email=email)
        return True
    except:
        return False

def phone_checker(user_id, number):
    print('inside phone checker')
    try:
        client = User.objects.get(id=user_id)
        print(client.email)
        phone_model = PhoneModel.objects.get(user=client, phone_number=number)
        print(phone_model.user)
        return True
    except:
        return False


def otp_message(request):
    try:
        print(request.GET['client_id'])
        print(request.GET['number'])
        print('inside otp_message')
        if phone_checker(request.GET['client_id'],request.GET['number']):
            data = {}
            data['status'] = 'success'
            data['number'] = request.GET['number']
            data['exist'] = 'True'
            print(data)
            return JsonResponse(data=data, safe=False)
    except:
        pass
    # account_sid = 'ACd50fe123ff4c24314ca2b6ac63c3d350'
    account_sid = 'ACdd657d4ed521eff8bd750ca7de57142c'
    auth_token = '17591dd653a6f4c24965d63ddb08ccd8'
    client = Client(account_sid, auth_token)
    number = request.GET['number']
    name = request.GET['name']
    otp = randint(1000,9999)
    body=""
    # Hi, Welcome to Business Verge. Verify using the OTP: [1234]
    if name:
        body="Hi, Welcome to Business Verge. Verify using the OTP: "+ str(otp)
    else:
        body="Hi, Welcome to Business Verge. Verify using the OTP: "+ str(otp)
    try:
        message = client.messages \
            .create(
            body=body,
            from_='+18432030382',
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
    try:
        print(request.GET['client_id'])
        if email_checker(request.GET['client_id'], request.GET['email']):
            data = {}
            data['status'] = 'success'
            data['email'] = request.GET['email']
            data['exist'] = 'True'
            print(data)
            return JsonResponse(data=data, safe=False)
    except:
        pass
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

def email_consent(request):
    subject = "OTP for Listing in Business Verge"

    email = request.GET['email']
    name = request.GET['name']
    otp = randint(1000,9999)
    body=""
    hbody=""
    if name:
        body="Hii "+", please provide the following otp to list yourself "+ str(otp)
        hbody='<p>Hii '+', please provide the following otp to list yourself <strong>'+ str(otp)+'</strong></p>'
    else:
        body = "Hii " + ", please provide the following otp to list yourself " + str(otp)
        hbody = '<p>Hii ' + ', please provide the following otp to list yourself <strong>' + str(otp) + '</strong></p>'

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

        # if(user.profile.social):
        #     print('found but social')
        #     found=False
        #     data={}
        #     data['status']='invalid'
        #     return JsonResponse(data, safe=False)
        # else:
        
        found=True
        print('found')
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


def process_request(request):
    is_mobile = False
    print('inside phone detection')

    if request.META['HTTP_USER_AGENT']:
        print('has request.meta')
        user_agent = request.META['HTTP_USER_AGENT']

        # Test common mobile values.
        pattern = "(up.browser|up.link|mmp|symbian|smartphone|midp|wap|phone|windows ce|pda|mobile|mini|palm|netfront)"
        prog = re.compile(pattern, re.IGNORECASE)
        match = prog.search(user_agent)

        if match:
            is_mobile = True
        else:
            # Nokia like test for WAP browsers.
            # http://www.developershome.com/wap/xhtmlmp/xhtml_mp_tutorial.asp?page=mimeTypesFileExtension

            if request.META['HTTP_ACCEPT']:
                http_accept = request.META['HTTP_ACCEPT']

                pattern = "application/vnd\.wap\.xhtml\+xml"
                prog = re.compile(pattern, re.IGNORECASE)

                match = prog.search(http_accept)

                if match:
                    is_mobile = True
        # local_mobile = is_mobile
        print('could not decide')
        if not is_mobile:
            # Now we test the user_agent from a big list.
            user_agents_test = ("w3c ", "acs-", "alav", "alca", "amoi", "audi",
                                "avan", "benq", "bird", "blac", "blaz", "brew",
                                "cell", "cldc", "cmd-", "dang", "doco", "eric",
                                "hipt", "inno", "ipaq", "java", "jigs", "kddi",
                                "keji", "leno", "lg-c", "lg-d", "lg-g", "lge-",
                                "maui", "maxo", "midp", "mits", "mmef", "mobi",
                                "mot-", "moto", "mwbp", "nec-", "newt", "noki",
                                "xda", "palm", "pana", "pant", "phil", "play",
                                "port", "prox", "qwap", "sage", "sams", "sany",
                                "sch-", "sec-", "send", "seri", "sgh-", "shar",
                                "sie-", "siem", "smal", "smar", "sony", "sph-",
                                "symb", "t-mo", "teli", "tim-", "tosh", "tsm-",
                                "upg1", "upsi", "vk-v", "voda", "wap-", "wapa",
                                "wapi", "wapp", "wapr", "webc", "winw", "winw",
                                "xda-",)

            test = user_agent[0:4].lower()
            # local_mobile = False
            if test in user_agents_test:
                print('is_mobile')
                is_mobile = True
    data={}
    print(is_mobile)
    data['is_mobile']=is_mobile
    return is_mobile

def mobile_request(request):
    is_mobile = False
    print('inside phone detection')

    if request.META['HTTP_USER_AGENT']:
        print('has request.meta')
        user_agent = request.META['HTTP_USER_AGENT']

        # Test common mobile values.
        pattern = "(up.browser|up.link|mmp|symbian|smartphone|midp|wap|phone|windows ce|pda|mobile|mini|palm|netfront)"
        prog = re.compile(pattern, re.IGNORECASE)
        match = prog.search(user_agent)

        if match:
            is_mobile = True
        else:
            # Nokia like test for WAP browsers.
            # http://www.developershome.com/wap/xhtmlmp/xhtml_mp_tutorial.asp?page=mimeTypesFileExtension

            if request.META['HTTP_ACCEPT']:
                http_accept = request.META['HTTP_ACCEPT']

                pattern = "application/vnd\.wap\.xhtml\+xml"
                prog = re.compile(pattern, re.IGNORECASE)

                match = prog.search(http_accept)

                if match:
                    is_mobile = True
        # local_mobile = is_mobile
        print('could not decide')
        if not is_mobile:
            # Now we test the user_agent from a big list.
            user_agents_test = ("w3c ", "acs-", "alav", "alca", "amoi", "audi",
                                "avan", "benq", "bird", "blac", "blaz", "brew",
                                "cell", "cldc", "cmd-", "dang", "doco", "eric",
                                "hipt", "inno", "ipaq", "java", "jigs", "kddi",
                                "keji", "leno", "lg-c", "lg-d", "lg-g", "lge-",
                                "maui", "maxo", "midp", "mits", "mmef", "mobi",
                                "mot-", "moto", "mwbp", "nec-", "newt", "noki",
                                "xda", "palm", "pana", "pant", "phil", "play",
                                "port", "prox", "qwap", "sage", "sams", "sany",
                                "sch-", "sec-", "send", "seri", "sgh-", "shar",
                                "sie-", "siem", "smal", "smar", "sony", "sph-",
                                "symb", "t-mo", "teli", "tim-", "tosh", "tsm-",
                                "upg1", "upsi", "vk-v", "voda", "wap-", "wapa",
                                "wapi", "wapp", "wapr", "webc", "winw", "winw",
                                "xda-",)

            test = user_agent[0:4].lower()
            # local_mobile = False
            if test in user_agents_test:
                print('is_mobile')
                is_mobile = True
    data={}
    print(is_mobile)
    data['is_mobile']=is_mobile
    return JsonResponse(data=data, safe=False)




