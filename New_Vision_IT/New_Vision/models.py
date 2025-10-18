from django.db import models

# -------------------------- Instructor Table --------------------------
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)  # Changed IntegerField → CharField
    picture = models.ImageField(upload_to='instructors/')

    def __str__(self):
        return self.name


# -------------------------- Course Table --------------------------
class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='courses/')
    price=models.IntegerField()


    def __str__(self):
        return self.title


# -------------------------- Student Table --------------------------
class Student(models.Model):
    sid = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='students/')

    def __str__(self):
        return self.name


# -------------------------- Result Table --------------------------
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.FloatField()
    grade = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student.name} - {self.course.title}"
