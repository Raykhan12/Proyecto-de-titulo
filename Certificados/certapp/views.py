from django.shortcuts import render
from .forms import *
from .models import *
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def index (request):
    return render(request,'index.html')

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        #uploaded_file_url = fs.url(filename)
        os.system("instantiate-certificate-batch -c /home/rayman/Certificados_blockchain/cert_tools/cert-tools/conf.ini")
        os.system("cert-issuer -c /home/rayman/Certificados_blockchain/cert-issuer-master/conf.ini")  
        path="/home/rayman/Certificados_blockchain/Certificados/certapp/blockcert"  # insert the path to your directory   
        file1 =os.listdir(path)

        return render(request, 'index.html', {
            'file_list': file1
        })
    return render(request, 'index.html')


 
