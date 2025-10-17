from django.urls import path
from New_Vision import views


urlpatterns = [

    path('',views.home_page,name='home'),
    path('student/', views.student_list, name='student_list'),
    path('instructors/', views.instructor_list, name='instructor_list'),
    path('course/', views.course_list, name='course_list'),
    path('result/', views.result_list, name='result_list'),
   
]
