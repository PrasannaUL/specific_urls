from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def kohli(request):
    return render(request,'kohli.html')

def david(request):
    return HttpResponse('hi david')
