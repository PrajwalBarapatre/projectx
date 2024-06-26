"""projectx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    re_path(r'^', include(('profiles.urls', 'profiles'), namespace='profiles')),
    re_path(r'^seller/', include(('seller1.urls', 'seller1'), namespace='seller1')),
    re_path(r'^metadata/', include(('metadata.urls', 'metadata'), namespace='metadata')),
    re_path(r'^album/', include(('album.urls', 'album'), namespace='album')),
    re_path(r'^chat/', include(('chat.urls', 'chat'), namespace='chat')),
    re_path(r'^investor/', include(('investor.urls', 'investor'), namespace='investor')),
    re_path(r'^advisor/', include(('advisor.urls', 'advisor'), namespace='advisor')),
    re_path(r'^staff/authorize/login/', include(('staff.urls', 'staff'), namespace='staff   ')),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)