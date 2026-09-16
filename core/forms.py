from django import forms
from .models import Registration, ContactMessage, TrainingCourse

class RegistrationForm(forms.ModelForm):
    YEAR_CHOICES = [
        ('', '-- Select Year of Study * --'),
        ('1st Year', '1st Year (Degree / Diploma)'),
        ('2nd Year', '2nd Year (Degree / Diploma)'),
        ('3rd Year', '3rd Year (Degree / Diploma)'),
        ('4th Year (Final Year)', '4th Year (Final Year B.Tech / BE)'),
        ('Diploma Final Year', 'Diploma / Polytechnic (Final Year)'),
        ('MCA / BCA Final Year', 'MCA / BCA (Final Year)'),
        ('Passed Out / Job Seeker', 'Passed Out / Job Seeker'),
    ]

    BRANCH_CHOICES = [
        ('', '-- Select Branch / Stream * --'),
        ('Computer Science & Engineering (CSE)', 'Computer Science & Engineering (CSE)'),
        ('Information Technology (IT)', 'Information Technology (IT)'),
        ('BCA / MCA', 'BCA / MCA'),
        ('Mechanical Engineering (ME)', 'Mechanical Engineering (ME)'),
        ('Civil Engineering (CE)', 'Civil Engineering (CE)'),
        ('Electrical / Electronics (EE/EEE/EC)', 'Electrical / Electronics (EE/EEE/EC)'),
        ('Polytechnic / Diploma (Any Stream)', 'Polytechnic / Diploma (Any Stream)'),
        ('Fashion / Interior / Textile Design', 'Fashion / Interior / Textile Design'),
        ('B.Sc / M.Sc / Other Tech Degree', 'B.Sc / M.Sc / Other Tech Degree'),
        ('Other Stream', 'Other Stream'),
    ]

    TRAINING_TYPE_CHOICES = [
        ('', '-- Select Training Batch / Program * --'),
        ('winter_2026', 'Winter Training 2026 (45 Days / 6 Weeks)'),
        ('summer_2026', 'Summer Training 2026 (45 Days / 6 Weeks)'),
        ('6_months', '06 Months Industrial Training (Live Projects)'),
        ('45_days', '45 Days Project Training & Certification'),
        ('online_batch', 'Online Live Interactive Batch'),
    ]

    year_of_study = forms.ChoiceField(
        choices=YEAR_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_year_of_study'})
    )

    branch = forms.ChoiceField(
        choices=BRANCH_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_branch'})
    )

    training_type = forms.ChoiceField(
        choices=TRAINING_TYPE_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_training_type'})
    )

    course_interested = forms.ChoiceField(
        choices=[('', '-- Select Course Interested * --')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-select select-highlight', 'id': 'id_course_interested'})
    )

    class Meta:
        model = Registration
        fields = [
            'full_name', 'email', 'phone', 'whatsapp_number', 
            'college', 'branch', 'year_of_study', 
            'course_interested', 'training_type', 'city'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name', 'id': 'id_full_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter active email address', 'id': 'id_email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10-digit mobile number', 'id': 'id_phone', 'maxlength': '15'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'WhatsApp number', 'id': 'id_whatsapp_number', 'maxlength': '15'}),
            'college': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. BBD, SRMCEM, LU, Govt Polytechnic...', 'id': 'id_college'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Lucknow, Kanpur, Gorakhpur...', 'id': 'id_city'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Build courses choices dynamically from database + catalog
        try:
            db_courses = list(TrainingCourse.objects.filter(is_active=True).values_list('title', flat=True).distinct())
        except Exception:
            db_courses = []

        canonical = [
            "Python with Django",
            "Data Analytics & Python",
            "MERN Stack Web Development",
            "Full Stack Web Development & Design",
            "Flutter & Dart App Development",
            "Java Full Stack Development",
            "Machine Design & CAD/CAM",
            "Circuit Design & VLSI Embedded",
            "Building Design & Revit Architecture",
            "Interior Design & 3D Visualization",
            "Textile Design & Fabric CAD",
            "Fashion Design & Apparel CAD",
            "PLC SCADA Industrial Automation",
            "AutoCAD (2D & 3D Drafting)",
        ]

        seen = set()
        course_list = []
        for c in db_courses + canonical:
            c_clean = c.strip()
            key = c_clean.lower()
            if key not in seen and c_clean:
                seen.add(key)
                course_list.append(c_clean)

        # If an initial course was requested via GET parameter and not in list
        initial_val = self.initial.get('course_interested') or (self.data.get('course_interested') if self.is_bound else None)
        if initial_val and initial_val.strip() and initial_val.strip().lower() not in seen:
            course_list.insert(0, initial_val.strip())

        choices = [('', '-- Select Course Interested * --')] + [(c, c) for c in course_list] + [('Other Specialized Course', 'Other Specialized Course')]
        self.fields['course_interested'].choices = choices

        # Default city to Lucknow if not provided
        if not self.is_bound and not self.initial.get('city'):
            self.initial['city'] = 'Lucknow'


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Mobile Number'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your Message'}),
        }


class CertificateSearchForm(forms.Form):
    certificate_number = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter Certificate ID (e.g. MT-2026-1001)'
        })
    )
