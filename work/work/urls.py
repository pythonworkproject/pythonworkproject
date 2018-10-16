from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('employee_app.urls')),
    url(r'^', include('users.urls')),
]

admin.site.site_header = 'Web Site Panel'
admin.site.site_title = 'Employee Site Panel '