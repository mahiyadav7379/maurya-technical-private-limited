from django.db import models
from django.utils.text import slugify

class TrainingCourse(models.Model):
    DURATION_CHOICES = (
        ('6_weeks', '06 Weeks / 45 Days'),
        ('6_months', '06 Months Industrial Training'),
        ('both', '45 Days & 06 Months'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=100, default='Software Development')
    duration = models.CharField(max_length=50, choices=DURATION_CHOICES, default='both')
    badge_text = models.CharField(max_length=100, default='WINTER TRAINING 2026')
    short_description = models.TextField()
    full_description = models.TextField(blank=True)
    features = models.TextField(help_text="Comma separated key features", default="100% Job Oriented, Live Project, Industry Experts")
    fee_45_days = models.CharField(max_length=50, default='₹4,000', help_text="Fee for 45 Days / 6 Weeks")
    fee_6_months = models.CharField(max_length=50, default='₹18,000', help_text="Fee for 06 Months Industrial Training")
    image_url = models.CharField(max_length=500, blank=True, null=True, help_text="Image URL or static path")
    is_featured = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_features_list(self):
        if not self.features:
            return []
        return [f.strip() for f in self.features.split(',') if f.strip()]

    def __str__(self):
        return self.title


class Placement(models.Model):
    student_name = models.CharField(max_length=150)
    course_taken = models.CharField(max_length=150, default='Python with Django')
    company_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150, default='Software Engineer')
    package = models.CharField(max_length=50, default='4.5 LPA')
    student_image_url = models.CharField(max_length=500, blank=True, null=True)
    placed_year = models.IntegerField(default=2026)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.company_name}"


class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    tech_stack = models.CharField(max_length=200, help_text="e.g. Full Stack Developer / Python Trainer")
    bio = models.TextField()
    phone = models.CharField(max_length=20, default='9198483820')
    email = models.EmailField(default='info@mauryatechnical.com')
    image_url = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.role})"


class Branch(models.Model):
    city = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=50)
    email = models.EmailField(default='info@mauryatechnical.com')
    is_head_office = models.BooleanField(default=False)
    map_embed_url = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.city} - {self.branch_name}"


class Certificate(models.Model):
    certificate_number = models.CharField(max_length=100, unique=True)
    student_name = models.CharField(max_length=150)
    course_name = models.CharField(max_length=200)
    training_duration = models.CharField(max_length=100, default='6 Months')
    issue_date = models.DateField()
    grade = models.CharField(max_length=20, default='A+')
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.certificate_number} - {self.student_name}"


class Registration(models.Model):
    TRAINING_TYPE_CHOICES = (
        ('winter_2026', 'Winter Training 2026'),
        ('summer_2026', 'Summer Training 2026'),
        ('6_months', '6 Months Industrial Training'),
        ('45_days', '45 Days Project Training'),
        ('online_batch', 'Online Live Batch'),
    )

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    college = models.CharField(max_length=200)
    branch = models.CharField(max_length=100, help_text="e.g. CS, IT, BCA, MCA, Diploma")
    year_of_study = models.CharField(max_length=50, default='3rd Year')
    course_interested = models.CharField(max_length=150)
    training_type = models.CharField(max_length=50, choices=TRAINING_TYPE_CHOICES, default='winter_2026')
    city = models.CharField(max_length=100, default='Lucknow')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.course_interested} ({self.phone})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100, default='Maurya Technical Team')
    summary = models.TextField()
    content = models.TextField()
    image_url = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
