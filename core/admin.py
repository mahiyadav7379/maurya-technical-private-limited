from django.contrib import admin
from .models import (
    TrainingCourse, Placement, TeamMember, Branch, 
    Certificate, Registration, ContactMessage, BlogPost,
    Faculty, FacultyAttendance, SalarySlip
)

@admin.register(TrainingCourse)
class TrainingCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'duration', 'is_featured', 'is_active', 'created_at')
    list_filter = ('category', 'duration', 'is_featured', 'is_active')
    search_fields = ('title', 'category', 'features')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Placement)
class PlacementAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'company_name', 'designation', 'package', 'placed_year')
    list_filter = ('company_name', 'placed_year')
    search_fields = ('student_name', 'company_name', 'designation')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'tech_stack', 'phone', 'is_active')
    search_fields = ('name', 'role', 'tech_stack')


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('city', 'branch_name', 'phone', 'is_head_office')
    list_filter = ('is_head_office',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_number', 'student_name', 'course_name', 'issue_date', 'is_valid')
    search_fields = ('certificate_number', 'student_name', 'course_name')
    list_filter = ('is_valid', 'issue_date')


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'college', 'course_interested', 'training_type', 'created_at')
    list_filter = ('training_type', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'college', 'course_interested')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at')
    search_fields = ('name', 'email', 'phone', 'subject')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'name', 'designation', 'department', 'phone', 'joining_date', 'monthly_salary', 'is_active')
    search_fields = ('faculty_id', 'name', 'phone', 'email', 'department')
    list_filter = ('department', 'is_active', 'joining_date')


@admin.register(FacultyAttendance)
class FacultyAttendanceAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'date', 'status', 'check_in', 'check_out')
    list_filter = ('status', 'date')
    search_fields = ('faculty__name', 'faculty__faculty_id')


@admin.register(SalarySlip)
class SalarySlipAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'month_year', 'net_salary', 'pay_date', 'payment_mode', 'status')
    list_filter = ('status', 'month_year')
    search_fields = ('faculty__name', 'faculty__faculty_id', 'transaction_id')

