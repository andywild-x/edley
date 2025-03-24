from django.http import HttpResponse
from django.shortcuts import render
from .models import TelefonbuchEintrag

# Create your views here.

def hello(request):
    return HttpResponse("Hello World!")

def einträge (reguest):
    einträge = TelefonbuchEintrag.objects.all()
    return render(reguest , 'einträge.html', context = {'einträge' : einträge})

def test ():
    return "Test"