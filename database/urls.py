from django.urls import path, include
from . import views
from rest_framework import routers

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('shop/database/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]