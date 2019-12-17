from django.conf import settings # import the settings file

def all_media(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'MEDIA_PREFIX': 'https://bverge.s3.ap-south-1.amazonaws.com'}