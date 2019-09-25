from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .forms import FileForm
from .models import File, KAlbumForFile
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie



@csrf_exempt
def post2(request):
    a=True
    if a:
        if request.method == 'POST':
            page_1 = PhotoForm(request.POST, request.FILES)
            files = request.FILES.getlist('file')
            print(request.FILES['file'].name)
            if page_1.is_valid():
                page_1.title=request.FILES['file'].name
                photo = page_1.save()
            else:
                print(page_1.errors)

        return render(request, 'album/upload.html')

    else:
        return redirect('album/upload.html')

@csrf_exempt
def post(request):

    if request.method=='POST':
        files = request.FILES.getlist('file')
        print(files)
        print(files[0].name)
        ac_name=files[0].name
        form = FileForm(request.POST, request.FILES)
        file = form.save()
        file.name=ac_name
        file.save()

        file_id = file.file_id
        print(file.name)
        data_send = {}
        data_send['file_id'] = file_id
        data_send['name']=file.name
        return JsonResponse(data_send, safe=False)
    return render(request, 'album/upload.html')


@csrf_exempt
def removeFile(request):
    if request.method == 'POST':
        print(request.POST['reque'])
        file_id="files/"+request.POST['name']
        print(file_id)
        filer = File.objects.get(name=file_id)

        filer.delete()
        data_send = {}
        return JsonResponse(data_send, safe=False)


@csrf_exempt
def removeFile2(request):
    if request.method == 'POST':
        album_id = request.POST['album_id']
        file_id = request.POST['file_id']
        album = Album.objects.get(album_id=album_id)
        filer = File.objects.get(file_id=file_id)
        for document in filer:
             document.delete()
        data_send = {}
        data_send['error'] = False
        data_send['message'] = 'fine'
        data_send['album_id'] = album_id
        return JsonResponse(data_send, safe=False)

@csrf_exempt
def Albumcreate(request):
    if request.method == 'POST':
        name = "files/" + request.POST['name']
        print(name)
        filer = File.objects.get(name=name)
        initialize = request.POST['initialize']
        print(initialize)
        if initialize=='true':
            print('true')
            album = KAlbumForFile()
            album.save()
            album.files.add(filer)
            album.save()
            data_send = {}
            data_send['error'] = False
            data_send['message'] = 'fine'
            data_send['album_id'] = album.album_id
        else :
            print('false')
            album_id = request.POST['album_id']
            album = KAlbumForFile.objects.get(album_id=album_id)
            album.files.add(filer)
            album.save()
            data_send = {}
            data_send['error'] = False
            data_send['message'] = 'fine'
            data_send['album_id'] = album.album_id
        return JsonResponse(data_send, safe=False)
















