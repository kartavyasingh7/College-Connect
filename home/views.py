from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from home.models import Student
from django.contrib.auth import authenticate, login, logout
from .models import FilesAdmin
from django.conf import settings
from django.http.response import Http404
import os

# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginUser(request):
    if request.user.is_anonymous:
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['pass']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                return redirect('/login')
        else:
            return render(request, 'login.html')
    else:
        return redirect('/home')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def signup(request):
    return render(request, 'signup.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['enroll']
        password = request.POST['pass1']
        batch = request.POST['batch']
        year = request.POST['year']
        print(batch,year)
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,password=password)
        user.save()
        student = Student.objects.create(enroll_no=username, batch=batch, year=year)
        student.save()
        return redirect('/login')

def home(request):
    if request.user.is_anonymous == False:
        return render(request, 'welcome.html')
    else:
        return redirect('/login')

def timetable(request):
    return render(request, 'timetable.html')

def menu(request):
    return render(request, 'menu.html')

def paper(request):
    context={'file':FilesAdmin.objects.all()}
    return render(request,'paper.html',context)

def download(request,path):
	file_path=os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path,'rb')as fh:
			response=HttpResponse(fh.read(),content_type="application/adminupload")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return response

	raise Http404	