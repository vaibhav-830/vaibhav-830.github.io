from django.conf.urls import url,include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^student/', include('student.urls')),
    url(r'^staffregistration/', include('student.urls')),
    url(r'^studentregistration/', include('student.urls')),
    url(r'^complain/', include('student.urls')),
    url(r'^staffquery/', include('student.urls')),
    url(r'^stafftoken/(?P<staffid>[0-9]+)', include('student.urls')),
    url(r'^studenttoken/(?P<studentid>[0-9]+)', include('student.urls')),
    url(r'^query2/', include('student.urls')),
    url(r'^querylogin/', include('student.urls')),
    url(r'^querylogin2/', include('student.urls')),
    url(r'^signupstaff/', include('student.urls')),
    url(r'^sstudent/', include('student.urls')),
    url(r'^stafflogin/', include('student.urls')),
    url(r'^stafflogin1/', include('student.urls')),
    url(r'^studentlogin/', include('student.urls')),
    url(r'^studentprofile/', include('student.urls')),
    url(r'^staffprofile/', include('student.urls')),
    url(r'^', include('student.urls')),
]

