from urllib.request import urlopen

from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

from staff.models import PhoneModel
from .formatChecker import ContentTypeRestrictedFileField
from .serializer import ChatSerializer
from django.http import FileResponse, Http404
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from django.core.exceptions import ValidationError

from django.http import JsonResponse
from seller1.models import Seller1
from profiles.models import Notification
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from user_seller.models import Invest, Advise,Sell
from investor.models import Investor, IndividualInvestor, CompanyInvestor
from profiles.models import Profile
from django.http import HttpResponse
from advisor.models import Advisor, StartupAdvisor, BusinessAdvisor

from .models import Chat, Contact, Message, Malbum, Notify, StaffChat, StaffMessage
import json
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse
import mimetypes
import requests
import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime, timedelta
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


User = get_user_model()

@login_required(login_url='profiles:index')
def index(request):
    context={}
    user = request.user
    try:
        contact = Contact.objects.get(user=user)
    except:
        return redirect('profiles:index')
    # curr_username=user.username
    # photo = user.profile.photo
    # full_name = user.profile.first_name + user.profile.last_name
    # user_dict={
    #     'curr_username':curr_username,
    #     'photo':photo.name,
    #     'full_name':full_name,
    #     'chat_id':user.profile.curr_chat.chat_id
    # }
    # context['user']=json.dumps(user_dict)
    return render(request, 'chat/index.html', context)

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username))
    })

User = get_user_model()

def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    contact = get_object_or_404(Contact, user=user)
    return contact


class ChatListView(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        queryset = Chat.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            contact = get_user_contact(username)
            queryset = contact.chats.all()
            fchats = []
            print(queryset[0])
            for chat in queryset:
                content={}
                content['chat_id'] = chat.chat_id
                array = []
                kchat = Chat.objects.get(chat_id=chat.chat_id)
                print(kchat)
                print(kchat.participants.all()[0].user.username)
                for person in kchat.participants.all():
                    dict = {}
                    dict['username'] = person.user.username
                    dict['url'] = person.user.profile.photo
                    array.append(dict)
                content['people'] = array
                content['business_name'] = chat.seller.name
                fchats.append(content)
        return fchats


class ChatDetailView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny, )


class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ChatDeleteView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )

def get_last_10_messages(chatId):
    chat = get_object_or_404(Chat, chat_id=chatId)
    return chat.messages.order_by('-timestamp').all()[:30]

def get_staff_messages(chat_id):
    staff_chat = get_object_or_404(StaffChat, chat_id=chat_id)
    return staff_chat.messages.order_by('-timestamp').all()

def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(Contact, user=user)

def get_chat(chat_id):
    return get_object_or_404(Chat, chat_id=chat_id)

def get_about_chat(request, chat_id):
    chat = Chat.objects.get(chat_id=chat_id)
    content = {}
    content['chat_id'] = chat_id
    array = []
    for person in chat.participants:
        dict = {}
        dict['username'] = person.user.username
        dict['url'] = person.user.profile.photo
        array.append(dict)
    content['people'] = array
    content['business_name'] = chat.seller.title
    return JsonResponse(content, safe=False)

def get_all_chats(request, username):


    if username is not None:
        contact = get_user_contact(username)
        queryset = contact.chats.all()
        now_chat = contact.user.profile.curr_chat
        fdata={}
        fchats = []
        fother={}
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
                else :
                    dict['status'] = 'offline'
                array.append(dict)
            content['people'] = array
            content['business_name'] = ''
            notify = Notify.objects.get(contact=contact, chat=chat)
            content['notif_number']=notify.number
            content['notif_id']=notify.notify_id
            if chat==now_chat:
                arr = list(chat.participants.all())
                arr.remove(contact)

                fother['other_profile_url'] = arr[0].user.profile.photo.name
                fother['other_name'] = '' + arr[0].user.profile.first_name + ' ' + arr[0].user.profile.last_name
                fother['other_id'] = arr[0].contact_id
                fother['blocked'] = ''
                if chat in arr[0].blocked_chats.all():
                    fother['blocked'] = 'true'

            print(content)
            fchats.append(content)

        fdata['chats'] = fchats
        fdata['curr'] = fother
        fdata = json.dumps(fdata)
        print(fdata)
        return HttpResponse(fdata)

def make_chat_invest(request):
    if request.method == 'GET':

        user = request.user
        # business_id = request.POST['business_id']
        investor_id = request.GET['investor_id']
        investor = Investor.objects.get(investor_id=investor_id)
        invest = Invest.objects.get(investor=investor)
        invest_profile = invest.owned_by.all()[0]
        invest_user = invest_profile.user
        # seller = Seller1.objects.get(business_id=business_id)
        # seller_profile = seller.owned_by.all()[0]
        # seller_user = User.objects.get(profile=seller_profile)
        user_contact = None
        invest_contact = None
        try:
            user_contact = Contact.objects.get(user=user)
        except:
            print('creating user contact')
            user_contact = Contact()
            user_contact.user = user
            user_contact.save()
        try:
            invest_contact = Contact.objects.get(user=invest_user)
        except:
            print('creating investor contact')
            invest_contact = Contact()
            invest_contact.user = invest_user
            invest_contact.save()
        chat = None
        invest_chats = None
        user_chats = None
        try:
            invest_chats = invest_contact.chats.all()
        except:
            pass
        try:
            user_chats = user_contact.chats.all()
        except:
            pass
        found = False
        if invest_chats is not None and user_chats is not None:
            print('chats are not none')
            for ichat in invest_chats:
                for schat in user_chats:
                    if ichat == schat:
                        print('found is true')
                        found = True
                        chat = ichat
                        user.profile.curr_chat = chat
                        invest_user.profile.curr_chat = chat
                        user.save()
                        invest_user.save()
                        try:
                            user_notify=Notify.objects.get(contact=user_contact, chat=chat)
                            invest_notify = Notify.objects.get(contact=invest_contact, chat=chat)
                        except:
                            user_notify=Notify()
                            user_notify.save()
                            user_notify.chat=chat
                            user_notify.contact=user_contact
                            user_notify.save()
                            invest_notify = Notify()
                            invest_notify.save()
                            invest_notify.chat = chat
                            invest_notify.contact = invest_contact
                            invest_notify.save()
                        print('user chat changed')
                        return render(request, 'chat/index.html', {})
        if found == False and chat is None:
            print('found is false')
            chat = Chat()
            # chat.seller = seller
            chat.save()
            chat.participants.add(user_contact)
            chat.participants.add(invest_contact)
            chat.save()
            print('new chat created')
            user.profile.curr_chat = chat
            invest_user.profile.curr_chat=chat
            user.save()
            invest_user.save()
            try:
                user_notify = Notify.objects.get(contact=user_contact, chat=chat)
                invest_notify = Notify.objects.get(contact=invest_contact, chat=chat)
            except:
                user_notify = Notify()
                user_notify.save()
                user_notify.chat = chat
                user_notify.contact = user_contact
                user_notify.save()
                invest_notify = Notify()
                invest_notify.save()
                invest_notify.chat = chat
                invest_notify.contact = invest_contact
                invest_notify.save()
            print('user chat changed')

        return render(request, 'chat/index.html', {})

def make_chat_advisor(request):

    if request.method == 'GET':

        user = request.user
        # business_id = request.POST['business_id']
        investor_id = request.GET['advisor_id']
        investor = Advisor.objects.get(advisor_id=investor_id)
        invest = Advise.objects.get(advisor=investor)
        invest_profile = invest.owned_by.all()[0]
        invest_user = invest_profile.user

        user_contact = None
        invest_contact = None
        try:
            user_contact = Contact.objects.get(user=user)
        except:
            print('creating user contact')
            user_contact = Contact()
            user_contact.user = user
            user_contact.save()
        try:
            invest_contact = Contact.objects.get(user=invest_user)
        except:
            print('creating investor contact')
            invest_contact = Contact()
            invest_contact.user = invest_user
            invest_contact.save()
        chat = None
        invest_chats = None
        user_chats = None
        try:
            invest_chats = invest_contact.chats.all()
        except:
            pass
        try:
            user_chats = user_contact.chats.all()
        except:
            pass
        found = False
        if invest_chats is not None and user_chats is not None:
            print('chats are not none')
            for ichat in invest_chats:
                for schat in user_chats:
                    if ichat == schat:
                        print('found is true')
                        found = True
                        chat = ichat
                        user.profile.curr_chat = chat
                        invest_user.profile.curr_chat = chat
                        user.save()
                        invest_user.save()
                        try:
                            user_notify = Notify.objects.get(contact=user_contact, chat=chat)
                            invest_notify = Notify.objects.get(contact=invest_contact, chat=chat)
                        except:
                            user_notify = Notify()
                            user_notify.save()
                            user_notify.chat = chat
                            user_notify.contact = user_contact
                            user_notify.save()
                            invest_notify = Notify()
                            invest_notify.save()
                            invest_notify.chat = chat
                            invest_notify.contact = invest_contact
                            invest_notify.save()
                        print('user chat changed')
                        return render(request, 'chat/index.html', {})
        if found == False and chat is None:
            print('found is false')
            chat = Chat()
            # chat.seller = seller
            chat.save()
            chat.participants.add(user_contact)
            chat.participants.add(invest_contact)
            chat.save()
            print('new chat created')
            user.profile.curr_chat = chat
            invest_user.profile.curr_chat = chat
            user.save()
            invest_user.save()
            try:
                user_notify = Notify.objects.get(contact=user_contact, chat=chat)
                invest_notify = Notify.objects.get(contact=invest_contact, chat=chat)
            except:
                user_notify = Notify()
                user_notify.save()
                user_notify.chat = chat
                user_notify.contact = user_contact
                user_notify.save()
                invest_notify = Notify()
                invest_notify.save()
                invest_notify.chat = chat
                invest_notify.contact = invest_contact
                invest_notify.save()
            print('user chat changed')

        return render(request, 'chat/index.html', {})


def make_chat_seller(request):
    if request.method == 'GET':

        user = request.user
        # business_id = request.POST['business_id']
        investor_id = request.GET['business_id']
        investor = Seller1.objects.get(business_id=investor_id)
        invest = Sell.objects.get(seller=investor)
        invest_profile = invest.owned_by.all()[0]
        invest_user = invest_profile.user

        user_contact = None
        invest_contact = None
        try:
            user_contact = Contact.objects.get(user=user)
        except:
            print('creating user contact')
            user_contact = Contact()
            user_contact.user = user
            user_contact.save()
        try:
            invest_contact = Contact.objects.get(user=invest_user)
        except:
            print('creating investor contact')
            invest_contact = Contact()
            invest_contact.user = invest_user
            invest_contact.save()
        chat = None
        invest_chats = None
        user_chats = None
        try:
            invest_chats = invest_contact.chats.all()
        except:
            pass
        try:
            user_chats = user_contact.chats.all()
        except:
            pass
        found = False
        if invest_chats is not None and user_chats is not None:
            print('chats are not none')
            for ichat in invest_chats:
                for schat in user_chats:
                    if ichat == schat:
                        print('found is true')
                        found = True
                        chat = ichat
                        user.profile.curr_chat = chat
                        invest_user.profile.curr_chat = chat
                        user.save()
                        invest_user.save()
                        try:
                            user_notify = Notify.objects.get(contact=user_contact, chat=chat)
                            invest_notify = Notify.objects.get(contact=invest_contact, chat=chat)
                        except:
                            user_notify = Notify()
                            user_notify.save()
                            user_notify.chat = chat
                            user_notify.contact = user_contact
                            user_notify.save()
                            invest_notify = Notify()
                            invest_notify.save()
                            invest_notify.chat = chat
                            invest_notify.contact = invest_contact
                            invest_notify.save()
                        print('user chat changed')
                        return render(request, 'chat/index.html', {})
        if found == False and chat is None:
            print('found is false')
            chat = Chat()
            # chat.seller = seller
            chat.save()
            chat.participants.add(user_contact)
            chat.participants.add(invest_contact)
            chat.save()
            print('new chat created')
            user.profile.curr_chat = chat
            invest_user.profile.curr_chat = chat
            user.save()
            invest_user.save()
            try:
                user_notify = Notify.objects.get(contact=user_contact, chat=chat)
                invest_notify = Notify.objects.get(contact=invest_contact, chat=chat)
            except:
                user_notify = Notify()
                user_notify.save()
                user_notify.chat = chat
                user_notify.contact = user_contact
                user_notify.save()
                invest_notify = Notify()
                invest_notify.save()
                invest_notify.chat = chat
                invest_notify.contact = invest_contact
                invest_notify.save()
            print('user chat changed')

        return render(request, 'chat/index.html', {})


def upload_file(request):
    if request.method=='POST':
        try:
            malbum = Malbum()
            file = request.FILES['file']
            malbum.file = file
            name = file.name
            malbum.save()
            malbum.file_name=name
            malbum.save()
            print(malbum.file_name)
            malbum_id = malbum.malbum_id
            data_send = {}
            data_send['status']='success'
            data_send['malbum_id']=malbum_id
            # data = json.dumps(data_send)
            print(data_send)
            return JsonResponse(data_send, safe=False)
        except ValidationError as e:
            print(e)



def pdf_view(request, file_name):
    print(file_name)
    name = 'media/message/'+file_name
    try:
        return FileResponse(open(name, 'rb'))
    except FileNotFoundError:
        raise Http404()

def chat_close(request):
    print('function called')
    try:
        user = request.user
        user.profile.status=False
        user.save()
        return JsonResponse({}, safe=False)
    except:
        return JsonResponse({}, safe=False)

def gen_notif(user_contact, curr_chat):
    participants=[]
    participants = curr_chat.participants.all()
    arr = list(participants)
    # arr.copy(participants)
    arr.remove(user_contact)
    for contact in arr:
        if contact.user.profile.status==False:
            notify = Notify.objects.get(contact=contact, chat=curr_chat)
            Notify.increase(notify)
            if notify.number==1:
                notif = Notification()
                notif.notif_type='Chat'
                notif.notif_statement='You have a new message from' + user_contact.user.profile.first_name + ' ' + user_contact.user.profile.last_name
                notif.save()
                contact.user.profile.notifs.add(notif)
                contact.user.save()
            if notify.number == 1:
                subject = "Business Verge New Message"
                email = notify.contact.user.email

                name = "" + user_contact.user.profile.first_name + ' ' + user_contact.user.profile.last_name
                body = "Hii " + ", you have a new message from " + name
                hbody = '<p>Hii ' + ', you have a new message from <strong>' + name + '</strong></p>'
                msg = EmailMultiAlternatives(subject, body, 'businessmerge@gmail.com', [email])
                msg.attach_alternative(hbody, "text/html")
                msg.send()
                print('mail sent')
            print(contact.user.username + 'has been notified')
        if contact.user.profile.status==True and contact.user.profile.curr_chat!=curr_chat:
            notify = Notify.objects.get(contact=contact, chat=curr_chat)
            Notify.increase(notify)
            print(contact.user.username + 'has been notified')


def fetch_sell_id(request,business_id):
    if request.method == 'GET':
        user = request.user
        # business_id = request.POST['business_id']
        investor_id = business_id
        investor = Seller1.objects.get(business_id=investor_id)
        invest = Sell.objects.get(seller=investor)
        invest_profile = invest.owned_by.all()[0]
        invest_user = invest_profile.user
        print(investor)

    return


def get_staff_chat(chat_id):
    return get_object_or_404(StaffChat, chat_id=chat_id)

def message_to_json(message):
    file_name = 'None'
    if message.malbum is not None:
        file_name = message.malbum.file_name
    author = 'Bverge'
    if not message.from_bverge:
        author = message.client.email
    return {
        'author': author,
        'content': message.content,
        'timestamp': str(message.timestamp),
        'id':message.message_id,
        'chat_id':message.chat.chat_id,
        'file':file_name,
        'file_exist':message.file_exist
    }



@csrf_exempt
def handle_incoming_messages(request):
    if request.method=='POST':
        print('inside webhook')
        message_sid = request.POST.get('MessageSid', '')
        from_number = request.POST.get('From', '')
        body = request.POST.get('Body', '')
        print(from_number)
        num_media = int(request.POST.get('NumMedia', 0))

        media_files = [(request.POST.get("MediaUrl{}".format(i), ''),
                        request.POST.get("MediaContentType{}".format(i), ''))
                       for i in range(0, num_media)]

        if not from_number or not message_sid:
            raise Exception('Please provide a From Number and a Message Sid')
        response = MessagingResponse()
        phonemodel = None
        client = None
        try:
            phonemodel = PhoneModel.objects.get(phone_number=from_number)
            client = phonemodel.user
        except:
            return str(response)
        chat = None
        try:
            chat = StaffChat.objects.get(client=client)
        except:
            chat = StaffChat()
            chat.client = client
            phone_model = PhoneModel.objects.get(user=client)
            chat.phone_model = phone_model
            chat.expiry_time = datetime.utcnow() + timedelta(days=1)
            chat.bverge_open = False
            chat.pending = True
            chat.save()

        if num_media > 0:
            for (media_url, mime_type) in media_files:
                file_extension = mimetypes.guess_extension(mime_type)
                media_sid = os.path.basename(urlparse(media_url).path)
                # content = requests.get(media_url).text
                filename = '{sid}{ext}'.format(sid=media_sid, ext=file_extension)

                # mms_media = MMSMedia(
                #     filename=filename,
                #     mime_type=mime_type,
                #     media_sid=media_sid,
                #     message_sid=message_sid,
                #     media_url=media_url,
                #     content=content)
                # mms_media.save()
                malbum = Malbum()
                # malbum.save()
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(urlopen(media_url).read())
                img_temp.flush()
                malbum.file.save(filename, ContentTypeRestrictedFileField(img_temp), save=True)
                malbum.save()
                message = StaffMessage()
                message.client = client
                message.chat = chat
                message.malbum = malbum
                message.file_exist = True
                message.from_bverge = False
                message.content = malbum.file_name
                message.save()
                if chat.bverge_open:
                    channel_layer = get_channel_layer()
                    room_name = chat.chat_id
                    content = {
                        'command': 'new_message',
                        # 'message': serializer.data
                        'message': message_to_json(message)
                    }
                    async_to_sync(channel_layer.group_send)(room_name,
                                                            {"type": "chat_message_whatsapp", 'message': message})

                else:
                    chat.pending = True
                    chat.save()
            if body:
                message = StaffMessage()
                message.client = client
                message.chat = chat
                # message.malbum = malbum
                message.file_exist = False
                message.from_bverge = False
                message.content = body
                message.save()
                if chat.bverge_open:
                    channel_layer = get_channel_layer()
                    room_name = chat.chat_id
                    content = {
                        'command': 'new_message',
                        # 'message': serializer.data
                        'message': message_to_json(message)
                    }
                    async_to_sync(channel_layer.group_send)(room_name,
                                                            {"type": "chat_message_whatsapp", 'message': message})

                else:
                    chat.pending = True
                    chat.save()
        else:
            message = StaffMessage()
            message.client = client
            message.chat = chat
            # message.malbum = malbum
            message.file_exist = False
            message.from_bverge = False
            message.content = body
            message.save()
            if chat.bverge_open:
                channel_layer = get_channel_layer()
                room_name = chat.chat_id
                content = {
                    'command': 'new_message',
                    # 'message': serializer.data
                    'message': message_to_json(message)
                }
                async_to_sync(channel_layer.group_send)(room_name,
                                                        {"type": "chat_message_whatsapp", 'message': message})

            else:
                chat.pending = True
                chat.save()

        response = MessagingResponse()
        return str(response)


def send_whatsapp_message(request):
    user = request.user
    if request.method=='POST' and user.is_staff:
        if request.POST['type']=='text':
            chat_id = request.POST['chat_id']
            staff_chat = StaffChat.objects.get(chat_id=chat_id)
            client = staff_chat.client
            if staff_chat.bverge_open and\
                    staff_chat.expiry_time - datetime.utcnow() < timedelta(days=1):
                message = StaffMessage()
                message.client = client
                message.chat = staff_chat
                # message.malbum = malbum
                message.file_exist = False
                message.from_bverge = True
                message.user = user
                message.content = request.POST['message']
                message.save()
                data = {}
                account_sid = 'ACdd657d4ed521eff8bd750ca7de57142c'
                auth_token = '17591dd653a6f4c24965d63ddb08ccd8'
                client = Client(account_sid, auth_token)
                phone_number = staff_chat.phone_model.phone_number
                to_= 'whatsapp:'+phone_number
                send_message = client.messages \
                    .create(
                    from_='whatsapp:+14155238886',
                    body=message.content,
                    to= to_
                )
                print(send_message.sid)
                data['self_blocked']=False
                data['message']=message_to_json(message)
                return JsonResponse(data, safe=False)
            else :
                data = {}
                data['self_blocked'] = True
                # data['message'] = message_to_json(message)
                return JsonResponse(data, safe=False)
        if request.POST['type'] == 'file':
            chat_id = request.POST['chat_id']
            staff_chat = StaffChat.objects.get(chat_id=chat_id)
            client = staff_chat.client
            if staff_chat.bverge_open and \
                    staff_chat.expiry_time - datetime.utcnow() < timedelta(days=1):
                malbum_id = request.POST['malbum_id']
                malbum = Malbum.objects.get(malbum_id=malbum_id)
                message = StaffMessage()
                message.client = client
                message.user = user
                message.chat = malbum
                message.malbum = malbum
                message.file_exist = True
                message.from_bverge = True
                message.content = malbum.file_name
                message.save()
                account_sid = 'ACdd657d4ed521eff8bd750ca7de57142c'
                auth_token = '17591dd653a6f4c24965d63ddb08ccd8'
                client = Client(account_sid, auth_token)
                phone_number = staff_chat.phone_model.phone_number
                to_ = 'whatsapp:' + phone_number
                url = 'https://bverge.s3.ap-south-1.amazonaws.com/'+message.content
                send_message = client.messages \
                    .create(
                    media_url=url,
                    from_='whatsapp:+14155238886',
                    body=message.content,
                    to=to_
                )
                print(send_message.sid)
                data = {}
                data['self_blocked'] = False
                data['message'] = message_to_json(message)
                return JsonResponse(data, safe=False)
            else :
                data = {}
                data['self_blocked'] = True
                # data['message'] = message_to_json(message)
                return JsonResponse(data, safe=False)
        data = {}
        data['status'] = False
        # data['message'] = message_to_json(message)
        return JsonResponse(data, safe=False)
    else:
        data = {}
        data['self_blocked'] = True
        # data['message'] = message_to_json(message)
        return JsonResponse(data, safe=False)


def staff_close_connection(request):
    user = request.user
    if request.method=='POST' and user.is_staff:
        chat_id = request.POST['chat_id']
        chat = StaffChat.objects.get(chat_id=chat_id)
        chat.bverge_open = False
        chat.pending = False
        chat.save()
        data = {}
        data['status'] = True
        return JsonResponse(data, safe=False)

def staff_check_connection(request):
    user=request.user
    if request.method=='POST' and user.is_staff:
        email = request.POST['email']

        chat = None
        self_blocked = True
        client = User.objects.get(email=email)
        try:
            chat = StaffChat.objects.get(client=client)
            if chat.expiry_time - datetime.utcnow() < timedelta(days=1):
                self_blocked = False
        except:
            chat = StaffChat()
            chat.client = client
            chat.expiry_time = datetime.utcnow()
            chat.bverge_open = False
            chat.pending = False
            phone_model = PhoneModel.objects.get(user=client)
            chat.phone_model=phone_model
            chat.save()




        photo_name = ''
        use_prefix = True
        if client.profile.social and not client.profile.photo_updated:
            photo_name = client.profile.photo_url
            use_prefix = False
        else:
            photo_name = client.profile.photo
            use_prefix = True

        data = {
            'status': 'success',
            'first_name': client.profile.first_name,
            'last_name': client.profile.last_name,
            'photo_name': photo_name,
            'use_prefix': use_prefix,
            'self_blocked': self_blocked,
        }

        return JsonResponse(data, safe=False)


def staff_whatsapp(request):
    context={}
    user = request.user
    if user.is_staff:
        return render(request, 'chat/staff_portal.html', context)
    else:
        redirect('profiles:index')

















