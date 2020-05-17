from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import hashlib
import zlib
import pickle
import urllib

from django.template.context import Context
from django.template.loader import render_to_string
from twilio.rest import Client
from django.contrib.auth.models import User
from datetime import datetime, timedelta

from chat.models import StaffChat, StaffMessage
from metadata.views import codedata
from staff.models import Task, RegTask, EmailModel, PhoneModel
from staff.forms import TaskForm, RegTaskForm
import base64
from django.http import JsonResponse
from random import randint
from django.core.mail import EmailMultiAlternatives

# Create your views here.

## note mysecret should be same while encode_data and decode_data

def encode_data(data):
    """Turn `data` into a hash and an encoded string, suitable for use with `decode_data`."""
    my_secret = str(datetime.now())
    compressed_text = zlib.compress(pickle.dumps(data, 0))
    enc = base64.b64encode(compressed_text).decode().replace('\n', '')
    hash_ = hashlib.md5(str.encode('{}{}'.format(my_secret, enc))).hexdigest()[:25]
    return hash_, enc

# def decode_data(hash, enc):
#     """The inverse of `encode_data`."""
#     text = urllib.unquote(enc)
#
#     m = hashlib.md5(my_secret + text).hexdigest()[:12]
#     if m != hash:
#         raise Exception("Bad hash!")
#     data = pickle.loads(zlib.decompress(text.decode('base64')))
#     return data

url_list = {
    'Business': 'staff:business_task',
    'Asset': 'staff:asset_task',
    'Loan': 'staff:loan_task',
    'Equity': 'staff:equity_task',
    'Startup': 'staff:startup_task',
    'Ip_Codes': 'staff:ipcode_task',
    'Application': 'staff:app_task',
    'Franchise': 'staff:franchise_task',
    'Supplier': 'staff:supplier_task',
}



def create_Task(request):
    user = request.user
    if user.is_staff:

        if request.method == 'POST':
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                task_form.save(commit=False)
                task = Task()
                task.user = user
                print(task_form.cleaned_data['client_email'])
                email = task_form.cleaned_data['client_email']
                client = User.objects.get(email=email)
                task.client = client
                task.listing_type = task_form.cleaned_data['listing_type']
                task_hash, task_enc = encode_data([email, str(datetime.now())])
                task.task_hash = task_hash
                task.task_enc = task_enc
                task.expires = datetime.now() + timedelta(minutes=30)
                task.lead_type = task_form.cleaned_data['lead_type']
                task.save()

                # print('task saved')
                # print(task.expires)
                # print(datetime.now())

                return redirect(url_list[task.lead_type], task_hash=task_hash)
            print('seems task post has errors')
        print('seems task form is get')
        task_form = TaskForm()
        context = {
            'task_form': task_form
        }

        return render(request, 'staff/staff.html', context)
    else:
        print('seems user is not staff')
        return redirect('profiles:index')

def createRegTask(request):
    user = request.user
    if user.is_staff and request.method=='POST':
        reg_form = RegTaskForm(request.POST)
        print(reg_form)
        if reg_form.is_valid():
            reg_form.save(commit=False)
            reg_task = RegTask()
            reg_task.client_email = reg_form.cleaned_data['client_email']
            reg_task.client_phone = reg_form.cleaned_data['client_phone']
            otp = randint(1000, 9999)
            reg_task.otp_email = otp
            otp = randint(1000, 9999)
            reg_task.otp_phone = otp
            reg_task.user = user
            reg_task.country_code_primary = reg_form.cleaned_data['country_code_primary']
            reg_task.save()
            data = {}
            subject = "Email Verification Business Verge"

            email = reg_task.client_email
            name = reg_form.cleaned_data['first_name']
            otp = reg_task.otp_email
            body = ""
            hbody = ""
            if name != '':
                body = "Hii " + ", verify your business email address using this   " + str(otp)
                c = {'name': name, 'otp': otp}
                hbody = render_to_string('seller1/otp_verify.html', context=c)
            else:
                body = "Hii " + ", verify your business email address using this   " + str(otp)
                c = {'name': '', 'otp': otp}
                hbody = render_to_string('seller1/otp_verify.html', context=c)

            # send_mail(subject, body, 'businessmerge@gmail.com', [email], fail_silently=False)
            msg = EmailMultiAlternatives(subject, hbody, 'admin@bverge.com', [email])
            msg.attach_alternative(hbody, "text/html")
            msg.send()

            data['status'] = 'success'
            data['email'] = email
            data['otp'] = otp
            print(data)

            account_sid = 'ACdd657d4ed521eff8bd750ca7de57142c'
            auth_token = '17591dd653a6f4c24965d63ddb08ccd8'
            client = Client(account_sid, auth_token)
            number = reg_task.client_phone
            name = ''
            otp = reg_task.otp_phone
            body = ""
            # Hi, Welcome to Business Verge. Verify using the OTP: [1234]
            # if name:
            #     body = "Hi, Welcome to Business Verge. Verify using the OTP: " + str(otp)
            # else:
            #     body = "Hi, Welcome to Business Verge. Verify using the OTP: " + str(otp)
            # try:
            #     message = client.messages \
            #         .create(
            #         body=body,
            #         from_='+18432030382',
            #         to=number
            #     )
            #     print(message.sid)
            #     # data = {}
            #     data['status'] = 'success'
            #     data['number'] = number
            #     data['otp'] = otp
            #     print(data)
            # except:
            #     # data = {}
            #     data['status'] = 'invalid'
            #     return JsonResponse(data, safe=False)

            new_data={}
            new_data['status']='valid'
            new_data['reg_id']=reg_task.reg_task_id

            return JsonResponse(new_data, safe=False)
        else:
            print(reg_form.errors)

    data = {}
    data['status'] = 'invalid'
    return JsonResponse(data, safe=False)

@login_required(login_url='profiles:index')
def createRegUser(request):
    user = request.user

    if user.is_staff:
        print('user is staff')
        if request.method=='POST':
            reg_form = RegTaskForm(request.POST)
            if reg_form.is_valid():
                reg_form.save(commit=False)
                reg_task_id = reg_form.cleaned_data['reg_task_id']
                reg_task = RegTask.objects.get(reg_task_id=reg_task_id)
                if reg_form.cleaned_data['otp_email'] == reg_task.otp_email: #and \
                        # reg_form.cleaned_data['otp_phone'] == reg_task.otp_phone:

                    print('inside create RegUser')
                    print(reg_task)
                    client = User()
                    client.email = reg_task.client_email
                    client.first_name = reg_form.cleaned_data['first_name']
                    client.last_name = reg_form.cleaned_data['last_name']
                    task_hash, task_enc = encode_data([reg_task.client_email, reg_task_id])
                    client.username = task_hash
                    client.set_password(task_enc)
                    client.save()
                    email_model = EmailModel()
                    email_model.email = client.email
                    email_model.user = client
                    email_model.save()
                    phone_model = PhoneModel()
                    phone_model.phone_number = reg_task.client_phone
                    phone_model.country_code_primary = reg_task.country_code_primary
                    phone_model.user = client
                    phone_model.save()
                    client.profile.first_name = client.first_name
                    client.profile.last_name = client.last_name
                    # client.profile.contact_number = reg_task.client_phone
                    client.save()
                    reg_task.client = client
                    reg_task.save()
                    chat = StaffChat()
                    chat.client = client
                    chat.expiry_time = datetime.utcnow()
                    chat.bverge_open = False
                    chat.pending = False
                    phone_model = phone_model
                    chat.phone_model = phone_model
                    chat.save()
                    # message = StaffMessage()
                    # message.client = client
                    # message.chat = chat
                    # # message.malbum = malbum
                    # message.file_exist = False
                    # message.from_bverge = True
                    # body = 'Hi ' + client.first_name + ' ' + client.last_name + \
                    #        ', Welcome to Business Verge! \n' \
                    #        'We are a business networking platform and help' \
                    #        ' Businesses and Startups to connect to beneficial Business, Investor and Advisors. \n' \
                    #        'Please, reply with your details to help BVerge to list your need.'
                    # message.content = body
                    # message.save()
                    #
                    #
                    # account_sid = 'ACdd657d4ed521eff8bd750ca7de57142c'
                    # auth_token = '17591dd653a6f4c24965d63ddb08ccd8'
                    # tw_client = Client(account_sid, auth_token)
                    # phone_number = chat.phone_model.phone_number
                    # to_ = 'whatsapp:' + phone_number
                    # send_message = tw_client.messages \
                    #     .create(
                    #     from_='whatsapp:+14155238886',
                    #     body=body,
                    #     to=to_
                    # )
                    # print(send_message.sid)

                    subject = "Welcome to Business Verge"
                    name = ''
                    email = client.email
                    name = client.first_name + ' ' + client.last_name
                    otp = randint(1000, 9999)
                    body = ""
                    hbody = ""
                    if name != '':
                        body = "Hii " + ", verify your business email address using this   " + str(otp)
                        c = {'name': name}
                        hbody = render_to_string('seller1/welcome.html', context=c)
                    else:
                        body = "Hii " + ", verify your business email address using this   " + str(otp)
                        c = {'name': ''}
                        hbody = render_to_string('seller1/welcome.html', context=c)

                    # send_mail(subject, body, 'businessmerge@gmail.com', [email], fail_silently=False)
                    msg = EmailMultiAlternatives(subject, body, 'admin@bverge.com', [email])
                    msg.attach_alternative(hbody, "text/html")
                    msg.send()

                    return redirect('staff:staff-home')
                return redirect('staff:client-reg')
            return redirect('staff:client-reg')
        print('request is get')
        reg_form = RegTaskForm()
        code_data = codedata()
        context = {

            'code_data': code_data,
            'task_form': reg_form,

        }
        return render(request, 'staff/client_reg.html', context)
    return redirect('profiles:index')







