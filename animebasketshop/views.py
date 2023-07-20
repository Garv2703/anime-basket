from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    context = {
        'media_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    context = {
        'media_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template('signup.html')
    context = {
        'media_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))