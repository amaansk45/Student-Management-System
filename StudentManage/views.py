from django.shortcuts import render , redirect
from StudentManage.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return redirect('/student/')
    return render(request, "home.html")

@login_required(login_url='login_page')
def student(request):
    queryset = Student.objects.all()
    
    return render(request, 'student.html', context= {'student' : queryset})

@login_required(login_url='login_page')
def addstudent(request):
     if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        course = data.get('course')
        age = data.get('age')
        status = data.get('status')

        print(name)
        print(email)
        print(phone)
        print(course)
        print(age)
        print(status)

        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            course=course,
            age=age,
            status=status
        )
        return render(request, 'success.html')
     queryset = Student.objects.all()

     return render(request, 'addStudent.html', context= {'student' : queryset})

@login_required(login_url='login_page')
def delete(request, id):
    queryset = Student.objects.get(id=id)
    queryset.delete()
    return redirect('/student/')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid User.")
            return redirect('/login_page/')
    
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Passsword.")
            return redirect('/login_page/')
        else:
            login(request,user)
            return redirect('/student/')

    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Already have an account.")
            return redirect('/register_page/')

        user = User.objects.create(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully.")
        return redirect('/register_page/')
        
    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    return redirect('/login_page/')
