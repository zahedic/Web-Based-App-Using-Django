#from django.http import HttpResponse
from django.shortcuts import render,redirect,get_list_or_404
from .models import  Student,Instructor

# Create your views here.

# --------------------------Home Page --------------------------

def home_page(request):
    return render(request,'home.html')



# --------------------------Instructor CRUD --------------------------

def instructor_list(request):
    instructors=Instructor.objects.all()
    return render(request,'instructor_list.html',{'instructors':instructors})


# --------------------------Student CRUD --------------------------

def student_list(request):
    students=Student.objects.all()
    return render(request,'student_list.html',{'students':students})



'''

def add_student(request):
    if request.method=='POST':
        sid=request.POST['id']
        name=request.POST['name']
        email=request.POST['email']
        Student.objects.create(sid=sid,name=name,email=email)
        return redirect('Student_list')
    return render(request,'add_student.html')

def edit_student(request,id):
    student=get_object_or_404(Student,id=id)
    if request.method=='POST':
        student.sid=request.POST['sid']
        student.name=request.POST['name']
        student.email=request.POST['email']
        student.save()
        return redirect('student_list')
    return render(request,'edit_student.html',{'student':student})

def delete_student(request,id):
    student=get_object_or_404(Student,id=id)
    student.delete()
    return redirect('student_list')

'''

