from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    # url('admin/', admin.site.urls),
    url('emp', views.emp),
    url('show',views.show),
    url('main', views.main, name='main'),
    url('contact', views.contact, name='contact'),
    url('about', views.about, name='about'),

    url('edit/(?P<eid>\d+)/', views.edit, name="edit"),
    url('update/(?P<eid>\d+)/', views.update, name="update"),
    url('delete/(?P<eid>\d+)/', views.destroy, name="delete"),
    url(r'^search/$', views.search, name='search'),
]



admin.site.site_header = 'Employee Site Panel'
admin.site.site_title = 'Employee Login Panel'