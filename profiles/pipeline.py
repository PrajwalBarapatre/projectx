from django.shortcuts import redirect
from social_django.models import UserSocialAuth
from django.contrib.auth.models import User

def get_avatar(backend,user, strategy, details, response, *args, **kwargs):
    url = None
    print(backend.name)
    print(response)
    print(details)
    print(user)
    id = None
    vuser = None
    if backend.name == 'linkedin-oauth2':
        url = '/media/files/advisor-img2.png'
        vuser = user
        pass
        # url = response.get('profile_image_url', '').replace('_normal','')
    if backend.name == 'google-oauth2':
        url = response['picture']
        # ext = url.split('.')[-1]
        # id = response['email']
        # socialuser = UserSocialAuth.objects.get(uid=id)
        vuser = user
    if backend.name == 'github':
        url = response['avatar_url']
        # id = response['id']
        # socialuser = UserSocialAuth.objects.get(uid=id)
        vuser = user
    if url:
        vuser.avatar = url
        vuser.profile.first_name = vuser.first_name
        vuser.profile.last_name = vuser.last_name
        vuser.profile.photo_url = url
        vuser.profile.social=True
        vuser.save()


def check_email_exists(backend,user, strategy, details, response, *args, **kwargs):
    email = details.get('email', '')
    exists = False
    users = User.objects.filter(email=email)
    if len(users) > 1:
        exists = True

    if exists:
        return redirect('profiles:auth_error')

    pass
