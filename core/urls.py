from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('branches/', views.branches, name='branches'),
    path('trainings/', views.trainings, name='trainings'),
    path('trainings/<slug:slug>/', views.course_detail, name='course_detail'),
    path('fees/', views.fees_structure, name='fees'),
    path('fees/python/', views.python_web_design_redirect, name='python_web_design_alias'),
    path('web-design/', views.fees_structure, name='web_design'),
    path('registration/', views.registration, name='registration'),
    path('gallery/', views.gallery, name='gallery'),
    path('placements/', views.placements, name='placements'),
    path('job-fair/', views.job_fair, name='job_fair'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.blogs, name='blogs'),
    path('projects/', views.blogs, name='projects'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('services/', views.services, name='services'),
    path('student-login/', views.student_login, name='student_login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/logout/', views.student_logout, name='student_logout'),
    path('faculty-login/', views.faculty_login, name='faculty_login'),
    path('faculty/dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('faculty/salary-slip/<int:slip_id>/', views.salary_slip_view, name='salary_slip_view'),
    path('faculty/logout/', views.faculty_logout, name='faculty_logout'),
]
