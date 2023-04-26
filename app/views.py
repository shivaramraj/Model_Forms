from django.shortcuts import render
from django.http import HttpResponse
from app.views import *
from app.models import *
from app.forms import *
# Create your views here.
def Insert_topic(request):
    # TO=Topic.objects.all()
    TF=WebPageForm()
    d={'TF':TF}
    return render(request,'WebpageForm.html',d)

def insert_webpage(request):
    WFO=WebPageForm()
    d={'WFO':WFO}

    if request.method=='POST':
        WPFO=WebPageForm(request.POST)
        if WPFO.is_valid():
            WPFO.save()
            return HttpResponse('Webpage is inserted')
    return render(request,'WebpageForm.html',d)
