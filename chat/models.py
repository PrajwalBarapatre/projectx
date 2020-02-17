from django.db import models
from django.contrib.auth import get_user_model
from seller1.models import Seller1
from .formatChecker import ContentTypeRestrictedFileField

CONTENT_TYPES = ['video/x-msvideo', 'application/pdf', 'video/mp4', 'audio/mpeg', 'image/png', 'image/jpeg', 'image/jpg', 'audio/mp3']
FILE_EXTENSIONS = ['mp4', 'mp3', 'pdf', 'png', 'jpg', 'jpeg']
User = get_user_model()

class Contact(models.Model):
    contact_id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username



class Malbum(models.Model):
    malbum_id = models.UUIDField(primary_key=True)
    file = ContentTypeRestrictedFileField(upload_to='message/', content_types=CONTENT_TYPES, file_extensions=FILE_EXTENSIONS, max_upload_size=10485760, blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        self.file_name = self.file.name
        super(Malbum, self).save(*args, **kwargs)

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True)
    contact = models.ForeignKey(Contact, related_name='messages', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    malbum = models.ForeignKey(Malbum, on_delete=models.CASCADE, blank=True, null=True)
    file_exist = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.username


class Chat(models.Model):
    chat_id = models.UUIDField(primary_key=True)
    participants = models.ManyToManyField(Contact, related_name='chats')
    messages = models.ManyToManyField(Message, blank=True)
    seller = models.OneToOneField(Seller1, null=True, blank=True, on_delete=models.CASCADE)
    blocked = models.ManyToManyField(Contact, blank=True, null=True, related_name='blocked_chats')

    def last_10_messages(self):
        return self.messages.order_by('-timestamp').all()[:10]

    def __str__(self):
        return "{}".format(self.pk)

class Notify(models.Model):
    notify_id = models.UUIDField(primary_key=True)
    contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, null=True, blank=True, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)

    def clear(self):
        self.number=0
        self.save()
        print('cleared')
        pass

    def increase(self):
        number = self.number
        self.number=number+1
        self.save()
        print('increased')
        pass
