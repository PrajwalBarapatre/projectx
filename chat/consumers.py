from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Message, Contact, Chat, Malbum, Notify, StaffMessage, StaffChat
from .serializer import MessageSerializer
from django.contrib.auth import get_user_model
from .views import get_last_10_messages, get_user_contact, get_chat, gen_notif, get_staff_messages, get_staff_chat
from channels.exceptions import StopConsumer
from datetime import datetime, timedelta

# from channels.auth import channel_session_user, channel_session_user_from_http
from profiles.models import Profile
User = get_user_model()

class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        print(data)
        messages = get_last_10_messages(data['chatId'])
        print(messages)
        # serializer = MessageSerializer(messages, many=True)
        content = {
            'command' : 'messages',
            # 'messages': serializer.data
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def messages_to_json(self, messages):
        result=[]
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        file_name = 'None'
        if message.malbum is not None:
            file_name = message.malbum.file_name
        return {
            'author': message.contact.user.username,
            'content': message.content,
            'timestamp': str(message.timestamp),
            'id':message.message_id,
            'chat_id':message.chat_set.all()[0].chat_id,
            'file':file_name,
            'file_exist':message.file_exist
        }

    def new_message(self, data):
        print('new message')
        user_contact = get_user_contact(data['from'])
        curr_chat = get_chat(data['chatId'])
        if user_contact in curr_chat.blocked.all():
            content = {
                'command': 'blocked',
                'status': 'online',

            }
            return self.send_message(content)
        message = Message()
        message.contact = user_contact
        message.content = data['message']
        message.save()

        curr_chat.messages.add(message)
        curr_chat.save()
        serializer = MessageSerializer(message)
        content = {
            'command': 'new_message',
            # 'message': serializer.data
            'message': self.message_to_json(message)
        }
        gen_notif(user_contact, curr_chat)
        return self.send_chat_message(content)

    def change_chat(self, data):
        print('inside change_chat')
        print(data['chat_id'])
        self.user = self.scope["user"]
        username = self.user.username
        user = self.user
        print(user.profile.curr_chat)
        nuser = User.objects.get(username=username)
        nuser.profile.curr_chat=get_chat(data['chat_id'])
        nuser.save()
        notify = Notify.objects.get(notify_id=data['notif_id'])
        Notify.clear(notify)
        print(user.profile.curr_chat)
        content = {
            'command': 'status',
            'status': 'online',

        }
        return self.send_chat_message(content)




    def file_message(self, data):
        print(data)
        malbum_id = data['malbum_id']
        malbum = Malbum.objects.get(malbum_id=malbum_id)
        user_contact = get_user_contact(data['from'])
        curr_chat = get_chat(data['chatId'])
        if user_contact in curr_chat.blocked.all():
            content = {
                'command': 'status',
                'status': 'online',

            }
            return self.send_chat_message(content)
        message = Message()
        message.contact = user_contact
        message.malbum = malbum
        message.file_exist=True
        message.content = malbum.file_name
        message.save()

        curr_chat.messages.add(message)
        curr_chat.save()
        content = {
            'command': 'new_message',
            # 'message': serializer.data
            'message': self.message_to_json(message)
        }
        gen_notif(user_contact, curr_chat)
        return self.send_chat_message(content)

    def block_user(self, data):
        curr_chat = get_chat(data['chatId'])
        contact = Contact.objects.get(contact_id=data['contact_id'])
        if data['block']==1:
            curr_chat.blocked.add(contact)
        else:
            curr_chat.blocked.remove(contact)
        curr_chat.save()
        content = {
            'command': 'status',
            'status': 'online',

        }
        return self.send_chat_message(content)



    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
        'change_chat': change_chat,
        'new_file': file_message,
        'block':block_user,
    }




    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.user = self.scope["user"]
        username = self.user.username
        user = self.user
        print(user.profile.status)
        user.profile.status=True
        user.save()
        print(user.profile.status)
        content ={
            'command':'status',
            'status':'online',

        }
        self.send_chat_message(content)


    def disconnect(self, close_code):
        # Leave room group
        print('disconnect')
        # self.user = self.scope["user"]
        # user = self.user
        # user.profile.status = False
        # user.save()
        # print(user.profile.status)
        # # self.disconnect(message["code"])
        #
        # content = {
        #     'command': 'status',
        #     'status': 'offline'
        # }
        #

        # self.send_chat_message(content)
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print('disconnected')
        self.close()
        raise StopConsumer()

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)


    def send_chat_message(self, message):
        print('inside send_chat_message')
        # Send message to room group

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )


    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group
    def chat_message(self, event):
        user = self.scope['user']

        print('sending')
        message = event['message']
        print(message)






        self.send(text_data=json.dumps(message))




class StaffChatConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        print(data)
        messages = get_staff_messages(data['chatId'])
        print(messages)
        # serializer = MessageSerializer(messages, many=True)
        content = {
            'command' : 'messages',
            # 'messages': serializer.data
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def messages_to_json(self, messages):
        result=[]
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
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

    def new_message(self, data):
        print('new message')
        self.user = self.scope["user"]
        user = self.user
        curr_chat = get_staff_chat(data['chatId'])
        # curr_chat.bverge_open = True
        # curr_chat.save()

        if curr_chat.expiry_time.time() < datetime.now().time() and \
                curr_chat.expiry_time.date() < datetime.now().date():
            content = {
                'command': 'blocked',
                # 'status': 'online',

            }
            return self.send_message(content)
        message = data['message']
        # message = StaffMessage()
        # message.user = user
        # message.chat = curr_chat
        # message.client = curr_chat.client
        # message.content = data['message']
        # message.from_bverge = True
        # message.save()

        # curr_chat.messages.add(message)
        # curr_chat.save()
        # serializer = MessageSerializer(message)
        content = {
            'command': 'new_message',
            # 'message': serializer.data
            'message': message
        }
        # gen_notif(user_contact, curr_chat)
        return self.send_chat_message(content)

    # def change_chat(self, data):
    #     print('inside change_chat')
    #     print(data['chat_id'])
    #     self.user = self.scope["user"]
    #     username = self.user.username
    #     user = self.user
    #     print(user.profile.curr_chat)
    #     nuser = User.objects.get(username=username)
    #     nuser.profile.curr_chat=get_chat(data['chat_id'])
    #     nuser.save()
    #     notify = Notify.objects.get(notify_id=data['notif_id'])
    #     Notify.clear(notify)
    #     print(user.profile.curr_chat)
    #     content = {
    #         'command': 'status',
    #         'status': 'online',
    #
    #     }
    #     return self.send_chat_message(content)




    def file_message(self, data):
        print(data)
        malbum_id = data['malbum_id']
        malbum = Malbum.objects.get(malbum_id=malbum_id)
        self.user = self.scope["user"]
        user = self.user
        curr_chat = get_staff_chat(data['chatId'])
        if curr_chat.expiry_time.time() < datetime.now().time() and \
                curr_chat.expiry_time.date() < datetime.now().date():
            content = {
                'command': 'blocked',
                # 'status': 'online',

            }
            return self.send_chat_message(content)
        message = StaffMessage()
        message.user = user
        message.chat = curr_chat
        message.client = curr_chat.client
        message.malbum = malbum
        message.from_bverge = True
        message.file_exist=True
        message.content = malbum.file_name
        message.save()

        # curr_chat.messages.add(message)
        # curr_chat.save()
        content = {
            'command': 'new_message',
            # 'message': serializer.data
            'message': self.message_to_json(message)
        }
        # gen_notif(user_contact, curr_chat)
        return self.send_chat_message(content)

    # def block_user(self, data):
    #     curr_chat = get_chat(data['chatId'])
    #     contact = Contact.objects.get(contact_id=data['contact_id'])
    #     if data['block']==1:
    #         curr_chat.blocked.add(contact)
    #     else:
    #         curr_chat.blocked.remove(contact)
    #     curr_chat.save()
    #     content = {
    #         'command': 'status',
    #         'status': 'online',
    #
    #     }
    #     return self.send_chat_message(content)



    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
        # 'change_chat': change_chat,
        'new_file': file_message,
        # 'block':block_user,
    }




    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.user = self.scope["user"]
        # username = self.user.username
        # user = self.user
        # curr_chat = StaffChat.objects.get(chat_id=self.room_name)
        # curr_chat.bverge_open = True
        # curr_chat.save()
        # print(user.profile.status)
        # user.profile.status=True
        # user.save()
        # print(user.profile.status)
        content ={
            'command':'status',
            'status':'online',

        }
        self.send_chat_message(content)


    def disconnect(self, close_code):
        # Leave room group
        print('disconnect')
        # self.user = self.scope["user"]
        # user = self.user
        # user.profile.status = False
        # user.save()
        # print(user.profile.status)
        # # self.disconnect(message["code"])
        #
        # content = {
        #     'command': 'status',
        #     'status': 'offline'
        # }
        #

        # self.send_chat_message(content)
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print('disconnected')
        self.close()
        raise StopConsumer()

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)


    def send_chat_message(self, message):
        print('inside send_chat_message')
        # Send message to room group

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message_whatsapp',
                'message': message
            }
        )


    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group
    def chat_message_whatsapp(self, event):
        user = self.scope['user']

        print('sending')
        message = event['message']
        print(message)






        self.send(text_data=json.dumps(message))