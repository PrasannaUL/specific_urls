from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def rohit(request):
    return render(request,'rohit.html')

def chris(request):
    return HttpResponse('hi chris')

