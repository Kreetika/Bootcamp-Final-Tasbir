
from django.contrib import admin
from django.urls import path
from .views import login, logout,edit_profile

urlpatterns = [
    path('login/', login, name = 'login' ),
    path('logout/', logout, name = 'logout'),
    path('edit-profile', edit_profile, name='edit-profile')
]
