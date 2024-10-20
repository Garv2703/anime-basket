from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('anime-details/<str:animeId>/', views.anime_details, name='anime-details'),
    path('watch/<str:animeId>/', views.anime_watch, name='anime-watch'),
    path('watch/<str:animeId>/<str:episodeId>', views.anime_watch, name='anime-watch'),
    path('search/', views.search, name='search'),
    path('addcomment', views.add_comment, name='addComment'),
]