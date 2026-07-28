from django.shortcuts import render , redirect
from StudentManage.models import *

def student(request):
    queryset = Student.objects.all()
    
    return render(request, 'student.html', context= {'student' : queryset})

def addstudent(request):
     if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        course = data.get('course')
        age = data.get('age')
        status = data.get('status')
        # age = data.get('age')

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

def delete(request, id):
    queryset = Student.objects.get(id=id)
    queryset.delete()
    return redirect('/student/')
