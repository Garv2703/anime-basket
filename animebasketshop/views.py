from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        referer = request.META['HTTP_REFERER'].split('/')
        if referer[-2] == 'login':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                else:
                    print('hello')
            else:
                print(form.errors)

        else:
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
            else:
                print(form.errors)

    template = loader.get_template('home.html')
    context = {
        'media_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('../')

    form = LoginForm()
    template = loader.get_template('login.html')
    context = {
        'media_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.MEDIA_URL,
        'base_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'],
        'form': form,
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
    if not request.user.is_authenticated:
        # referer = request.META['HTTP_REFERER'].split('/')
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    logout(request)
    return redirect('https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.BASE_URL)