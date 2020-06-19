from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from .models import Post, Counter
from .forms import numbersinc

request_counter_signal = Signal(providing_args=['timestamp'])


def home(request):
    request_counter_signal.send(sender=Post, timestamp='its now')
    context = {}
    return HttpResponse('Welcome to the home page ')


@receiver(request_finished)
def home_page_requested(sender, **kwargs):
    counts = Counter.objects.get(id=1)
    counts.number += 1
    counts.save()
    print('I have Had a new request ')


@receiver(request_counter_signal)
def post_counter(sender, **kwargs):
    print(kwargs)
