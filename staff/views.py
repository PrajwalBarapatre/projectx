from django.shortcuts import render, redirect
import hashlib
import zlib
import pickle
import urllib
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from staff.models import Task
from staff.forms import TaskForm
import base64
# Create your views here.

## note mysecret should be same while encode_data and decode_data

def encode_data(data):
    """Turn `data` into a hash and an encoded string, suitable for use with `decode_data`."""
    my_secret = str(datetime.now())
    compressed_text = zlib.compress(pickle.dumps(data, 0))
    enc = base64.b64encode(compressed_text).decode().replace('\n', '')
    hash_ = hashlib.md5(str.encode('{}{}'.format(my_secret, enc))).hexdigest()[:25]
    return hash_, enc

# def decode_data(hash, enc):
#     """The inverse of `encode_data`."""
#     text = urllib.unquote(enc)
#
#     m = hashlib.md5(my_secret + text).hexdigest()[:12]
#     if m != hash:
#         raise Exception("Bad hash!")
#     data = pickle.loads(zlib.decompress(text.decode('base64')))
#     return data

url_list = {
    'Business': 'staff:business_task',
    'Asset': 'staff:asset_task',
    'Loan': 'staff:loan_task',
    'Equity': 'staff:equity_task',
    'Startup': 'staff:startup_task',
    'Ip_Codes': 'staff:ipcode_task',
    'Application': 'staff:app_task',
    'Franchise': 'staff:franchise_task',
    'Supplier': 'staff:supplier_task',
}



def create_Task(request):
    user = request.user
    if user.is_staff:

        if request.method == 'POST':
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                task_form.save(commit=False)
                task = Task()
                task.user = user
                print(task_form.cleaned_data['client_email'])
                email = task_form.cleaned_data['client_email']
                client = User.objects.get(email=email)
                task.client = client
                task.listing_type = task_form.cleaned_data['listing_type']
                task_hash, task_enc = encode_data([email, str(datetime.now())])
                task.task_hash = task_hash
                task.task_enc = task_enc
                task.expires = datetime.now() + timedelta(minutes=30)
                task.lead_type = task_form.cleaned_data['lead_type']
                task.save()

                # print('task saved')
                # print(task.expires)
                # print(datetime.now())

                return redirect(url_list[task.lead_type], task_hash=task_hash)
            print('seems task post has errors')
        print('seems task form is get')
        task_form = TaskForm()
        context = {
            'task_form': task_form
        }

        return render(request, 'staff/staff.html', context)
    else:
        print('seems user is not staff')
        return redirect('profiles:index')




