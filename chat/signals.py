from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from chat.models import Chat, Contact, Notify

def send_update(sender, instance, created, **kwargs):
    pass

post_save.connect(send_update, sender=Notify)