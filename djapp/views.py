from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver,Signal
from .models import Post 


request_counter_signal = Signal(providing_args=['timestamp'])


def home(request):
    request_counter_signal.send(sender=Post ,timestamp='its now')
    return HttpResponse("You have request the home page")

@receiver(request_finished)
def home_page_requested(sender,**kwargs):
    print('The home page has been request and its fine')

@receiver(request_counter_signal)
def post_counter(sender,**kwargs):
    print(kwargs)
