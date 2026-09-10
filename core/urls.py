from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('branches/', views.branches, name='branches'),
    path('trainings/', views.trainings, name='trainings'),
    path('trainings/<slug:slug>/', views.course_detail, name='course_detail'),
    path('web-design/', views.web_design_hub, name='web_design'),
    path('web-design/python/', views.python_web_design_redirect, name='python_web_design_alias'),
    path('registration/', views.registration, name='registration'),
    path('gallery/', views.gallery, name='gallery'),
    path('placements/', views.placements, name='placements'),
    path('job-fair/', views.job_fair, name='job_fair'),
    path('verify-certificate/', views.job_fair, name='verify_certificate'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.blogs, name='blogs'),
    path('projects/', views.blogs, name='projects'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('services/', views.services, name='services'),
    path('student-login/', views.student_login, name='student_login'),
]
