from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register, profile, logout_user, login_user

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

]
