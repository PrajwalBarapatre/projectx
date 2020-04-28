from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from rest_framework.views import APIView
from rest_framework.response import Response
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

