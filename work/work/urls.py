from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('employee_app.urls')),
    url(r'^', include('api.urls')),

    # url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_views.login),
    url(r'^logout/', auth_views.logout),
    url(r'^', include('login_app.urls'))

]


admin.site.site_header = 'Web Site Panel'
admin.site.site_title = 'Employee Site Panel '