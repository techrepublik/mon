from django.shortcuts import render
from django.http import HttpResponse

def collections(request):
    return HttpResponse('Collection it is!')
