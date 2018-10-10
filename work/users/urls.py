from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
       url(r'^login/', views.user_login, name='login_url'),
       url(r'^signup/', views.users_signup, name='signup_url'),

       # This is for display the pagination
       # url(r'^login/', views.index, name='pagination'),

       # This is for display the Err msgs
       url(r'^err/', views.err, name='pagination'),
]