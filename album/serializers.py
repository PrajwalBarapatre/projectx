from rest_framework import serializers
from album.models import KAlbumForFile, File

class KAblumSerializer(serializers.ModelSerializer):
    class Meta:
        model = KAlbumForFile
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
