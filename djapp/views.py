from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver

def home(request):
    return HttpResponse("You have request the home page")

@receiver(request_finished)
def home_page_requested(sender,**kwargs):
    print('The home page has been request and its fine')