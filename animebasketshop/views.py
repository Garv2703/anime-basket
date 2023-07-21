from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import SignupForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = email.split('@')
            username = username[0]
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            name = first_name + ' ' + last_name
            password = form.cleaned_data['password']
            new_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

    template = loader.get_template('home.html')
    context = {
        'media_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    if request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    template = loader.get_template('login.html')
    context = {
        'media_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('../')

    form = SignupForm()
    template = loader.get_template('signup.html')
    context = {
        'media_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.MEDIA_URL,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def logout_view(request):
    logout(request)
    return redirect('https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.BASE_URL)