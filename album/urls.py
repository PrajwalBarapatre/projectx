from django.conf.urls import url
from . import views

urlpatterns = [
    url('add/',views.Albumcreate, name='album-create'),
    url('basic-upload/', views.post, name='basic_upload'),
    url('remove/', views.removeFile, name='remove'),
]