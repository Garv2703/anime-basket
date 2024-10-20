from django.forms import ValidationError
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm
from .functions import Functions
from .models import Reviews
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    anime = Functions.get_anime()
    recent_anime = Functions.get_recent_anime()
    popular_anime = Functions.get_popular_anime()
    heroAnime = Functions.get_hero_content()

    template = loader.get_template('home.html')
    context = {
        'static_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.STATIC_URL,
        'login_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.LOGIN_URL,
        'anime_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.ANIME_URL,
        'base_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'],
        'anime_watch_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.ANIME_WATCH_URL,
        'anime': anime['results'],
        'recent_anime': recent_anime['results'],
        'popular_anime': popular_anime['results'],
        'hero_anime': heroAnime,
    }
    return HttpResponse(template.render(context, request))

def login_view(request):
    if request.user.is_authenticated:
        return redirect('https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.BASE_URL)
    
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.BASE_URL)
            else:
                error = 'Invalid Email or Password!'        
    else:
        form = LoginForm()

    form = LoginForm()
    template = loader.get_template('login.html')
    context = {
        'static_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.STATIC_URL,
        'login_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.LOGIN_URL,
        'base_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'],
        'form': form,
        'error': error,
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    if request.user.is_authenticated:
        return redirect('https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.BASE_URL)
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                raise ValidationError(("Email already exists!"), code="invalid")
            
            username = email.split('@')
            username = username[0]
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # name = first_name + ' ' + last_name
            password = form.cleaned_data['password']
            new_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            if new_user is not None:
                login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.BASE_URL)
        else:
            print(form.errors)
    else:
        form = SignupForm()

    template = loader.get_template('signup.html')
    context = {
        'static_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.STATIC_URL,
        'login_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.LOGIN_URL,
        'base_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'],
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def anime_details(request, animeId):
    template = loader.get_template('anime-details.html')

    anime_details = Functions.get_anime_details(animeId)

    context = {
        'static_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.STATIC_URL,
        'login_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.LOGIN_URL,
        'base_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'],
        'anime_watch_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.ANIME_WATCH_URL,
        'anime': anime_details,
        'animeId': animeId,
    }
    return HttpResponse(template.render(context, request))

def anime_watch(request, animeId, episodeId=None):
    template = loader.get_template('anime-watching.html')

    if episodeId == None:
        episodeId = animeId + '-episode-1'

    anime_details = Functions.get_anime_details(animeId)
    episode = Functions.get_anime_episode(episodeId)
    servers = Functions.get_available_servers(episodeId)
    reviews = Functions.get_episode_comments(episodeId)

    epNum = episodeId.split('-')

    context = {
        'static_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.STATIC_URL,
        'login_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.LOGIN_URL,
        'base_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'],
        'anime_watch_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.ANIME_WATCH_URL,
        'anime': anime_details,
        'animeId': animeId,
        'episodeId': episodeId,
        'episode': episode,
        'episodeNum': epNum[-1],
        'servers': servers,
        'reviews': reviews,
    }
    return HttpResponse(template.render(context, request))

def search(request):
    query = request.GET.get('title', '')
    if not query:
        return redirect(request.META['HTTP_REFERER'])

    search_results = Functions.get_search_results(query)

    template = loader.get_template('search.html')
    context = {
        'static_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.STATIC_URL,
        'login_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.LOGIN_URL,
        'base_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'],
        'anime_url': 'https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.ANIME_URL,
        'search_results': search_results['results'],
        'search_item': query,
    }
    return HttpResponse(template.render(context, request))

def add_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        name = request.user.get_full_name()
        episodeId = request.POST.get('episode_id')
        review = Reviews(uid=request.user.id, name=name,comment=comment, episode_id=episodeId)
        review.save()

    return JsonResponse({'name': name})

@login_required
def logout_view(request):
    logout(request)
    return redirect('https://' if request.is_secure() else 'http://' + request.META['HTTP_HOST'] + settings.BASE_URL)