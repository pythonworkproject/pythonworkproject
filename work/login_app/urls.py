from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register
from . import views
urlpatterns = [
    # url(r'^$', home),
    url('home', views.home, name='home'),
    # url(r'^$', home, name='home'),
    url(r'^register/', register),
    url('logout',views.logoutView.as_view(), name="logout"),
]