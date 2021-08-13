from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View as django_views
from .models import *
# from .form import *
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('index')

class LoginView(django_views):
    """ This Class has functionality of LogIn API of User"""

    def get(self,request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request,'index.html')

    def post(self,request):
        params = request.POST
        email = params['email']
        password = params['password']


        try:
            user = authenticate(request, email=email,password=password)
            if user is not None:
                """ User session is started here."""
                login(request, user)
                return redirect('dashboard')

            else:
                message = "Wrong Email Id or Password.!!!" # A message
                return render(request,'index.html',{"message":message})

        except Exception as e:
            print("Exception",e)
            pass



class RegisterView(django_views):

    def get(self,request):
        return render(request,'register.html')

    def post(self, request):
        data=request.POST
        first_name=data['first_name']
        last_name=data['last_name']
        email=data['email']
        contact_number=data['contact_number']
        date_of_birth=data['date_of_birth']
        password=data['password']
        password1=data['password1']
        if password1 != password:
            message="Password is not match"
            return render(request,'register.html',{'message':message})
        check=MyUser.objects.filter(email=email).first()
        if check:
            message="e-mail id is already exist"
            return render(request, 'register.html', {'message':message})
        obj=MyUser.objects.create(email=email,first_name=first_name, last_name=last_name,contact_number=contact_number,date_of_birth=date_of_birth)
        obj.set_password(password)
        obj.save()
        message="user is created"
        return redirect('/')





