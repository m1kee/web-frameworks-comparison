from django.urls import path
from .views import hello_world, get_users

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('users/', get_users, name='get_users'),
]