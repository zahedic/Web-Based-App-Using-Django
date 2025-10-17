from django.db import models

# --------------------------Create Student Table --------------------------

class Instructor(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    department=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# --------------------------Create Course Table --------------------------

class Course(models.Model):
    title=models.CharField(max_length=100)
    code=models.CharField(max_length=10,unique=True)
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# --------------------------Create Student Table --------------------------
   
class Student(models.Model):
    sid=models.CharField(max_length=20,unique=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name


# --------------------------Create Result Table --------------------------
   
class Result(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.FloatField()
    grade=models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student.name}-{self.course.title}"
    


