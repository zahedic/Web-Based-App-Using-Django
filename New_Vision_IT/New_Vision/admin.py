from django.contrib import admin
from .models import  Instructor, Course, Student, Result

# Register your models here.
@admin.register(Student)
class Student_Model_Admin(admin.ModelAdmin):
    list_display=['sid','name','email','phone','course','picture']


@admin.register(Instructor)
class Instructor_Model_Admin(admin.ModelAdmin):
    list_display=['name','email','department','phone','picture']


@admin.register(Course)
class Course_Model_Admin(admin.ModelAdmin):
    list_display=['code','title','description','instructor','picture']


@admin.register(Result)
class Result_Model_Admin(admin.ModelAdmin):
    list_display=['student','course','marks','grade']
