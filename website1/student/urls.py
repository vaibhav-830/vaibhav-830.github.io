app_name ='student'
from django.conf.urls import url
from . import views

urlpatterns =[

     url(r'^$',views.index, name='index'),
     url(r'^staffregistration/', views.staffregistration , name='staffregistration'),
     url(r'^studentregistration/',views.studentregistration, name='studentregistration'),
     url(r'^complain/', views.complain, name='complain'),
     url(r'^staffquery/', views.staffquery, name='staffquery'),
     url(r'^stafftoken/(?P<staffid>[0-9]+)', views.stafftoken, name='stafftoken'),
     url(r'^studenttoken/(?P<studentid>[0-9]+)', views.studenttoken, name='studenttoken'),
     url(r'^query2/', views.query2, name='query2'),
     url(r'^backindex/',views.backindex, name='backindex'),
     url(r'^querylogin/', views.querylogin, name='querylogin'),
     url(r'^querylogin2/', views.querylogin2, name='querylogin2'),
     url(r'^signupstaff/', views.signupstaff, name='signupstaff'),
     url(r'^sstudent/', views.sstudent, name='sstudent'),
     url(r'^stafflogin/', views.stafflogin, name='stafflogin'),
     url(r'^stafflogin1/', views.stafflogin1, name='stafflogin1'),
     url(r'^studentlogin/', views.studentlogin, name='studentlogin'),
     url(r'^studentprofile/', views.studentprofile, name='studentprofile'),
     url(r'^staffprofile/', views.staffprofile, name='staffprofile'),
]
