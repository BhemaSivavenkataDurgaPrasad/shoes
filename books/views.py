from django.shortcuts import render
from django.http import HttpResponse,request
from . import models

# Create your views here.
def Home_page(request):
    return render(request ,'index.html')

def Shop_page(request):
    return render(request ,'shoes.html')


def collection_page(request):
    return render(request ,'collection.html')


def racing_page(request):
    return render(request,'racing boots.html')


def contact_page(request):
    return render(request,'contact.html')
 