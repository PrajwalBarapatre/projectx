from django.conf import settings # import the settings file

def all_media(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    notifications = None
    notif_number = None
    notif_true = False
    try:
        user = request.user
        notifications = user.profile.notifs.all().order_by('-created_at')
        notif_number = 0
        for notif in notifications:
            if notif.notif_seen == False:
                notif_number = notif_number + 1
        notif_true = True
    except:
        print('user is not authenticated')
        pass
    return {'MEDIA_PREFIX': 'https://bverge.s3.ap-south-1.amazonaws.com',
            'notifications': notifications,
            'notif_number': notif_number,
            'notif_true': notif_true,
            }