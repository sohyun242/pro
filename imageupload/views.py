from django.shortcuts import render
from .models import Imageupload

def home(request):
    return render(request, 'home.html')
  



def imageupload(request):
    imageuploads = Imageupload.objects
    return render(request, 'home.html', {'imageuploads':imageuploads})

