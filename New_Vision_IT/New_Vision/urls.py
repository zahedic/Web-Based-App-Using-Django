from django.urls import path
from New_Vision import views


urlpatterns = [

    
    path('student/', views.student_list, name='student_list'),
    path('instructors/', views.instructor_list, name='instructor_list'),
  
   
]
