from django.contrib import admin
from .models import (
    TrainingCourse, Placement, TeamMember, Branch, 
    Certificate, Registration, ContactMessage, BlogPost
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
