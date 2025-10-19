from django.urls import path
from New_Vision import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',views.home_page,name='home'),
    path('student/', views.student_list, name='student_list'),
    path('instructor/', views.instructor_list, name='instructor_list'),
    path('course/', views.course_list, name='course_list'),
    path('result/', views.result_list, name='result_list'),


    path('about/', views.about_page, name='about_page'),
    path('success/', views.success_page, name='success_page'),
    path('contact/', views.contact_page, name='contact_page'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
