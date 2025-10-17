from django.contrib import admin
from .models import  Instructor, Course, Student, Result

# Register your models here.
@admin.register(Student)
class Student_Model_Admin(admin.ModelAdmin):
    list_display=['sid','name','email']


@admin.register(Instructor)
class Instructor_Model_Admin(admin.ModelAdmin):
    list_display=['name','email','department']


@admin.register(Course)
class Course_Model_Admin(admin.ModelAdmin):
    list_display=['title','code','instructor']


@admin.register(Result)
class Result_Model_Admin(admin.ModelAdmin):
    list_display=['student','course','marks','grade']
