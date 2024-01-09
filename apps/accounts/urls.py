from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register, profile, logout_user, logout

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', logout_user, name='login'),
    path('logout/', logout, name='logout'),

]
