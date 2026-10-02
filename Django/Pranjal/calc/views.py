from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    params = {'Name':'Pranjal'}
    return render(request,'index.html', params)
