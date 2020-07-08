from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from random import random
import random
import string

def index(request):
    return render(request,'student/index.html')
def backindex(request):
    return render(request,'student/index.html')
def staffregistration(request):
    return render(request,'student/staffregistration.html')
def studentregistration(request):
    return render(request,'student/studentregistration.html')
def signupstaff(request):
    try:
        name = request.POST['name']
        staffid = request.POST['staffid']
        password = request.POST['password']
        faculty = request.POST['faculty']
        college=request.POST['college']
        department = request.POST['department']
        emailid = request.POST['emailid']
        dob = request.POST['dob']
        mobileno = request.POST['mobileno']
        image = request.POST['image']
        s = Staffregistration()
        s.name = name
        s.staffid = staffid
        s.password =password
        s.faculty=faculty
        s.college=college
        s.department = department
        s.emailid = emailid
        s.dob = dob
        s.mobileno = mobileno
        s.image = image
        s.save()

        msg = "Registered Sucessfully"
    except:
        return render(request,'student/staffregistration.html')
    else:
        return render(request,'student/staffregistration.html',{'msg': msg,})



def sstudent(request):
    try:
        name = request.POST['name']
        studentid = request.POST['studentid']
        password = request.POST['password']
        faculty = request.POST['faculty']
        college = request.POST['college']
        department = request.POST['department']
        course = request.POST['course']
        semester = request.POST['semester']
        emailid = request.POST['emailid']
        dob = request.POST['dob']
        mobileno = request.POST['mobileno']
        image = request.POST['image']
        s = Studentregistration()
        s.name = name
        s.studentid = studentid
        s.password = password
        s.faculty = faculty
        s.college = college
        s.department = department
        s.course = course
        s.semester = semester
        s.emailid = emailid
        s.dob = dob
        s.mobileno = mobileno
        s.image = image
        s.save()
    except:
        msg = "invalid registration"
        return render(request, 'student/studentregistration.html',{'msg':msg, })
    else:
        msg = "Registered Complaint Sucessfully"
        return render(request, 'student/studentregistration.html', {'msg': msg, })






def stafflogin(request):
    try:
        loginid=request.POST['loginid']
        password=request.POST['pass']
        s=Staffregistration.objects.get(staffid=loginid,password=password)
    except:
        error = 'Something went wrong'
        return render(request, 'student/stafflogin.html', {'errormessage': error, })
    else:
        error='You are successfully Login'
        return render(request, 'student/staffprofile.html', {'errormessage':error,})

def studentlogin(request):
    try:
        loginid=request.POST['loginid']
        password=request.POST['pass']
        s=Staffregistration.objects.get(studentid=loginid,password=password)
    except:
        error = 'Something went wrong'
        return render(request, 'student/studentlogin.html', {'errormessage': error, })
    else:
        error='You are successfully Login'
        return render(request, 'student/studentprofile.html', {'errormessage':error,})


def complain(request):
    msg='You are successfully Registered'
    return render(request,'student/index.html',{'msg':msg,})


def querylogin(request):
    msg='You are successfully Registered'
    return render(request,'student/querylogin.html',{'msg':msg,})

def querylogin2(request):
    msg='You are successfully Registered'
    return render(request,'student/querylogin2.html',{'msg':msg,})

def stafflogin1(request):
    return render(request,'student/stafflogin.html')

def staffquery(request):
    try:
        loginid = request.POST['loginid']
        password = request.POST['pass']
        staff = Staffregistration.objects.get(staffid=loginid,password=password )
    except:
        msg = "Something wents wrong"
        return render(request,'student/querylogin.html',{'msg': msg})
    else:
        msg = "You are successfully Registered"
        return render(request,'student/staffquery.html',{'msg': msg, 'staff': staff},)

def query2(request):
    try:
        loginid = request.POST['loginid']
        password = request.POST['pass']
        student = Studentregistration.objects.get(studentid=loginid,password=password )
    except:
        msg = "Something wents wrong"
        return render(request,'student/querylogin2.html',{'msg': msg})
    else:
        msg = "You are successfully login."
        return render(request,'student/query2.html',{'msg': msg, 'student': student})


def stafftoken(request,staffid):
     try:
         s= Staffregistration.objects.get(id=staffid)
         name = request.POST['name']
         email =  request.POST['email']
         category =  request.POST['category']
         description =  request.POST['description']
         stafftoken = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(0, 6)])
         q = Query()
         q.name = name
         q.email = email
         q.category = category
         q.description = description
         q.token = stafftoken
         q.staffregistration = s
         q.save()

     except:
         msg = "Something wents wrong"
         return render(request, 'student/staffquery.html', {'msg': msg})
     else:
         msg = "You are successfully login."
         return render(request, 'student/staffprofile.html',{'msg': msg,'q': q,})


def studenttoken(request, studentid):
    try:
        s = Studentregistration.objects.get(id=studentid)
        name = request.POST['name']
        email = request.POST['email']
        category = request.POST['category']
        description = request.POST['description']
        studenttoken = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(0, 6)])
        q = Query2()
        q.name = name
        q.email = email
        q.category = category
        q.description = description
        q.token = studenttoken
        q.studentregistration = s
        q.save()

    except:
        msg = "Something wents wrong"
        return render(request, 'student/query2.html', {'msg': msg})
    else:
        msg = "You are successfully login."
        return render(request, 'student/studentprofile.html', {'msg': msg,'q': q,})


def studentprofile(request):
    try:
        loginid = request.POST['loginid']
        password = request.POST['pass']
        student = Studentregistration.objects.get(studentid=loginid, password=password)
    except:
        msg = "Something wents wrong"
        return render(request, 'student/querylogin2.html', {'msg': msg})
    else:
        msg = "You are successfully login."
        return render(request, 'student/studentprofile.html', {'msg': msg,})


def staffprofile(request):
    try:
        loginid = request.POST['loginid']
        password = request.POST['pass']
        staff = Staffregistration.objects.get(staffid=loginid,password=password )
    except:
        msg = "Something wents wrong"
        return render(request,'student/querylogin.html',{'msg': msg})
    else:
        msg = "You are successfully Login"
        return render(request,'student/staffprofile.html',{'msg': msg,})
