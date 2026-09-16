from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import (
    TrainingCourse, Placement, TeamMember, Branch, 
    Certificate, Registration, ContactMessage, BlogPost,
    Faculty, FacultyAttendance, SalarySlip
)
from .forms import RegistrationForm, ContactForm, CertificateSearchForm

def home(request):
    courses = TrainingCourse.objects.filter(is_active=True)[:8]
    placements = Placement.objects.all().order_by('-placed_year', '-created_at')[:10]
    team_members = TeamMember.objects.filter(is_active=True)[:6]
    branches = Branch.objects.all()
    latest_blogs = BlogPost.objects.all().order_by('-created_at')[:3]

    context = {
        'courses': courses,
        'placements': placements,
        'team_members': team_members,
        'branches': branches,
        'latest_blogs': latest_blogs,
    }
    return render(request, 'home.html', context)


def about(request):
    team_members = TeamMember.objects.filter(is_active=True)
    return render(request, 'about.html', {'team_members': team_members})


def branches(request):
    branch_list = Branch.objects.all()
    return render(request, 'branches.html', {'branches': branch_list})


def trainings(request):
    q = request.GET.get('q', '').strip()
    if q:
        from django.db.models import Q
        courses = TrainingCourse.objects.filter(
            Q(title__icontains=q) | Q(short_description__icontains=q) | Q(category__icontains=q),
            is_active=True
        )
    else:
        courses = TrainingCourse.objects.filter(is_active=True)
    return render(request, 'trainings.html', {'courses': courses, 'search_query': q})


def course_detail(request, slug):
    course = TrainingCourse.objects.filter(slug=slug).first()
    if not course:
        course = TrainingCourse.objects.filter(slug__startswith=slug).first()
    if not course:
        course = get_object_or_404(TrainingCourse, slug=slug)

    related_courses = TrainingCourse.objects.filter(is_active=True).exclude(id=course.id)[:4]

    # Dynamic syllabus and tools tailored for each design domain
    curriculum_data = {
        "machine-design": {
            "modules": [
                {"num": "01", "title": "Engineering Drawing Fundamentals", "desc": "Standard projections, orthographic views, sectioning, dimensioning, and GD&T conventions."},
                {"num": "02", "title": "AutoCAD 2D Drafting & Detailing", "desc": "Commands, layers, isometric drawings, component layouts, and production drawing sheets."},
                {"num": "03", "title": "SolidWorks 3D Parametric Modeling", "desc": "Part modeling, sketch constraints, extrude, revolve, sweep, loft, and feature tree management."},
                {"num": "04", "title": "CATIA Surface & Sheet Metal Design", "desc": "Wireframe and surface workbench, generative shape design, sheet metal bends, and stamping features."},
                {"num": "05", "title": "3D Modeling & Freeform Surfacing", "desc": "Advanced hybrid modeling, complex curvature, fillets, blends, and product aesthetics."},
                {"num": "06", "title": "2D Drafting & Production Blueprints", "desc": "Bill of Materials (BOM), exploded views, tolerance stacking, and manufacturing blueprints."},
                {"num": "07", "title": "Machine Components & Assembly Modeling", "desc": "Mates, fasteners, gear trains, shafts, bearings, interference checks, and motion study."},
                {"num": "08", "title": "Mechanical Design Basics & Prototyping", "desc": "Material selection, stress concentration basics, 3D printing preparation, and capstone project."}
            ],
            "tools": ["AutoCAD Mechanical", "SolidWorks", "CATIA", "ANSYS FEA", "GD&T", "Keyshot 3D"],
            "projects": [
                {"name": "Automotive Gearbox Assembly", "desc": "Complete CAD assembly with gear ratios, shaft sizing, and casing blueprints."},
                {"name": "Hydraulic Pump & Valve Design", "desc": "Internal flow casing, impeller modeling, and sectioned fabrication drawings."}
            ]
        },
        "circuit-design": {
            "modules": [
                {"num": "01", "title": "Basic Electronics & Components", "desc": "Resistors, capacitors, diodes, transistors, op-amps, and active/passive circuit behavior."},
                {"num": "02", "title": "Electrical Circuit Basics & Laws", "desc": "Ohm's law, Kirchhoff's laws, AC/DC analysis, power calculations, and filter circuits."},
                {"num": "03", "title": "PCB Design Fundamentals", "desc": "Schematic capture, footprint assignment, track routing, ground planes, and design rule checks (DRC)."},
                {"num": "04", "title": "Circuit Simulation & SPICE Analysis", "desc": "Transient analysis, frequency response, waveform verification, and tolerance testing."},
                {"num": "05", "title": "Arduino Basics & Interfacing", "desc": "Microcontroller architecture, digital/analog I/O, PWM, sensor interfacing, and serial communication."},
                {"num": "06", "title": "Embedded System Basics & Firmware", "desc": "Embedded C programming, interrupt handling, timers, ADC, and hardware abstraction."},
                {"num": "07", "title": "Proteus Virtual Lab Simulation", "desc": "Interactive circuit simulation, MCU code debugging, virtual instruments, and oscilloscope testing."},
                {"num": "08", "title": "KiCad / EasyEDA Multilayer PCB Routing", "desc": "Double-sided and multilayer routing, Gerber file generation, BOM export, and SMD assembly prep."}
            ],
            "tools": ["KiCad", "EasyEDA", "Proteus", "Arduino IDE", "Multisim", "Altium Basics"],
            "projects": [
                {"name": "Smart IoT Sensor Node PCB", "desc": "Double-sided board with power regulation, ESP32 MCU, and analog sensor conditioning."},
                {"name": "Digital Battery Management Circuit", "desc": "Overvoltage protection, thermal cut-off, and LED status indicators."}
            ]
        },
        "building-design": {
            "modules": [
                {"num": "01", "title": "Architectural Drawing & Symbols", "desc": "Standard building symbols, scales, line weights, elevation tags, and site orientation."},
                {"num": "02", "title": "AutoCAD Civil 2D Drafting", "desc": "Walls, doors, windows, hatching, dimensioning, layers, blocks, and plot sheet setup."},
                {"num": "03", "title": "2D Floor Plan & Residential Layouts", "desc": "Vastu/functional room layout planning, circulation spaces, staircase design, and toilet layouts."},
                {"num": "04", "title": "3D Building Modeling & Masses", "desc": "Converting 2D floor plans into 3D massing models, parapets, roof terraces, and balconies."},
                {"num": "05", "title": "Revit Architecture & BIM Modeling", "desc": "Parametric walls, curtain walls, floors, roofs, schedules, materials, and family creation."},
                {"num": "06", "title": "SketchUp 3D Architectural Exterior", "desc": "Push-pull modeling, component libraries, 3D terrain modeling, and daylight study."},
                {"num": "07", "title": "Building Planning & Municipal Norms", "desc": "FAR, set-backs, ground coverage, parking norms, fire safety, and municipal approval layouts."},
                {"num": "08", "title": "Structural Drawing Basics & Blueprints", "desc": "Column grid layouts, footing details, beam-slab reinforcement schedules, and capstone project."}
            ],
            "tools": ["AutoCAD Civil", "Revit Architecture", "SketchUp", "STAAD.Pro Basics", "Lumion", "Photoshop"],
            "projects": [
                {"name": "Multi-Storey Residential Apartment Plan", "desc": "Complete municipal approval drawing set with 2D plans, sections, and 3D elevation."},
                {"name": "Commercial Office Complex BIM", "desc": "3D Revit model with doors/windows schedules and realistic walkthrough animation."}
            ]
        },
        "interior-design": {
            "modules": [
                {"num": "01", "title": "Space Planning & Anthropometrics", "desc": "Ergonomics, spatial zoning, traffic clearance, human dimension standards, and bubble diagrams."},
                {"num": "02", "title": "Furniture Layout & Detailing", "desc": "Custom modular furniture planning, wardrobe internals, TV units, modular kitchens, and beds."},
                {"num": "03", "title": "AutoCAD Interior Working Drawings", "desc": "Reflected ceiling plans (RCP), electrical layout, flooring pattern drawings, and wall elevations."},
                {"num": "04", "title": "SketchUp 3D Interior Modeling", "desc": "Creating interior volumes, precision furniture modeling, custom moldings, and 3D Warehouse assets."},
                {"num": "05", "title": "3D Interior Modeling & Styling", "desc": "Soft furnishings, curtains, rugs, decorative accents, wall panels, and indoor landscaping."},
                {"num": "06", "title": "V-Ray / Rendering & Material Creation", "desc": "PBR materials, wood veneers, marble, fabrics, camera field-of-view, and photorealistic rendering."},
                {"num": "07", "title": "Material & Color Selection", "desc": "Color psychology, finishes, laminate swatches, wallpaper selection, tile patterns, and mood boards."},
                {"num": "08", "title": "Lighting Design & Walkthroughs", "desc": "Ambient, task, and accent lighting, false ceiling light coves, Lumion walkthrough animation, and portfolio."}
            ],
            "tools": ["SketchUp", "AutoCAD", "V-Ray", "Lumion", "Adobe Photoshop", "Enscape"],
            "projects": [
                {"name": "Luxury 3BHK Residence Interior", "desc": "Complete modular kitchen design, master bedroom suite, and 4K photorealistic V-Ray renders."},
                {"name": "Modern Co-Working Office Interior", "desc": "Reception lobby, open workstations, executive cabin, and acoustic ceiling plan."}
            ]
        },
        "textile-design": {
            "modules": [
                {"num": "01", "title": "Textile Designing Basics", "desc": "Fiber to fabric journey, yarn classifications, plain/twill/satin weave structures, and count systems."},
                {"num": "02", "title": "Fabric Design & Weave Structures", "desc": "Drafting, lifting plans, cross-sections, motif placement, and handloom/powerloom understanding."},
                {"num": "03", "title": "Pattern Making & Repeat Systems", "desc": "Straight repeats, half-drop, brick, diamond repeats, toss patterns, and border layouts."},
                {"num": "04", "title": "Surface Design & Ornamentation", "desc": "Tie-dye, batik, block printing, screen printing fundamentals, embroidery motifs, and texture effects."},
                {"num": "05", "title": "Digital Textile Printing (DTP)", "desc": "Color profiles, raster vs vector, sublimation, reactive digital printing, and RIP software setup."},
                {"num": "06", "title": "Photoshop for Textile Design", "desc": "Color separation, cleaning artwork, indexing, tonal prints, and floral artwork development."},
                {"num": "07", "title": "CorelDRAW Vector Fabric Patterns", "desc": "Geometric patterns, vector motifs, seamless tile generation, scale adjustment, and production colorways."},
                {"num": "08", "title": "Color & Pattern Development", "desc": "Color forecasting, seasonal palette boards, fabric swatch sampling, and commercial textile portfolio."}
            ],
            "tools": ["Adobe Photoshop", "CorelDRAW", "NedGraphics Basics", "Textile CAD", "Pantone Guides"],
            "projects": [
                {"name": "Home Furnishing Fabric Collection", "desc": "Curtain and upholstery coordinates with 4 seamless colorways and digital print specifications."},
                {"name": "Ethnic Apparel Print Capsule", "desc": "Block-print inspired floral coordinates for sarees and ethnic tunics with production repeats."}
            ]
        },
        "fashion-design": {
            "modules": [
                {"num": "01", "title": "Fashion Illustration & Croquis", "desc": "8-head and 10-head figure proportions, posture posing, facial features, and fashion rendering."},
                {"num": "02", "title": "Garment Designing & Silhouettes", "desc": "Necklines, collars, sleeves, skirts, trousers, bodice styles, and design balance principles."},
                {"num": "03", "title": "Pattern Making & Block Drafting", "desc": "Standard measurement taking, basic bodice block, skirt block, sleeve block, and dart manipulation."},
                {"num": "04", "title": "Draping Techniques on Dress Form", "desc": "Muslin preparation, basic bodice draping, cowl necks, princess seams, gathers, and pleating."},
                {"num": "05", "title": "Textile & Fabric Knowledge", "desc": "Fabric grainline, drape characteristics, knits vs wovens, lining, interfacings, and trim selection."},
                {"num": "06", "title": "CorelDRAW / Photoshop for Fashion", "desc": "Digital flat sketches (tech packs), mood board creation, fabric rendering, and spec sheets."},
                {"num": "07", "title": "Fashion CAD & Pattern Grading", "desc": "Computer-aided pattern drafting, grading across size charts (S, M, L, XL), and marker planning."},
                {"num": "08", "title": "Apparel Design & Collection Portfolio", "desc": "Theme-based 5-look capsule collection, stitching tech packs, cost calculation, and runway portfolio."}
            ],
            "tools": ["CorelDRAW", "Adobe Illustrator", "Adobe Photoshop", "Fashion CAD", "Pattern Drafting Tools"],
            "projects": [
                {"name": "Seasonal Capsule Collection", "desc": "5-look digital illustration line-up with tech packs, fabric swatches, and flat sketches."},
                {"name": "Boutique Evening Gown Construction", "desc": "Draped pattern, corset detailing, fabric estimation, and production spec sheet."}
            ]
        }
    }

    # Match slug to curriculum key
    curriculum_key = None
    for key in curriculum_data.keys():
        if key in slug:
            curriculum_key = key
            break

    if curriculum_key:
        active_data = curriculum_data[curriculum_key]
        syllabus_modules = active_data["modules"]
        tools_list = active_data["tools"]
        projects_list = active_data["projects"]
    else:
        # Default Web Design modules
        syllabus_modules = [
            {"num": "01", "title": "Web Architecture & Semantic HTML5", "desc": "Internet structure, client-server lifecycle, semantic HTML5 tags, accessible web forms, tables, modern media embedding, and SEO metadata."},
            {"num": "02", "title": "Modern Styling with CSS3, Flexbox & CSS Grid", "desc": "CSS box model, responsive layouts with Flexbox and CSS Grid, responsive typography, media queries, CSS transitions, and smooth animations."},
            {"num": "03", "title": "Responsive UI Frameworks & Bootstrap 5", "desc": "Mobile-first responsive design, Bootstrap 5 components, navbar, modals, cards, carousels, forms, and custom utility classes."},
            {"num": "04", "title": "Interactive Client-Side JavaScript & DOM", "desc": "JavaScript ES6+ fundamentals, DOM manipulation, event listeners, form validation, Fetch API / AJAX for dynamic asynchronous web experiences."},
            {"num": "05", "title": "Python Programming Essentials for Web", "desc": "Python syntax, control flow, functions, modular architecture, Object-Oriented Programming (OOP) classes, inheritance, and exception handling."},
            {"num": "06", "title": "Django Web Framework & MVT Architecture", "desc": "Django project & app architecture, Model-View-Template (MVT) pattern, URL dispatcher, Jinja-style template tags, filters, and inheritance."},
            {"num": "07", "title": "Database Modeling, ORM & User Authentication", "desc": "Django ORM models, migrations, PostgreSQL/SQLite integration, admin customization, user signup/login, sessions, and role permissions."},
            {"num": "08", "title": "REST APIs, Live Capstone Project & Deployment", "desc": "Building RESTful APIs with Django REST Framework, real-world live project development, Git & GitHub version control, and production cloud hosting."}
        ]
        tools_list = ["HTML5", "CSS3", "JavaScript", "Bootstrap 5", "Python 3", "Django 5", "PostgreSQL", "SQLite", "Git & GitHub", "VS Code", "Postman", "Figma"]
        projects_list = [
            {"name": "Dynamic E-Commerce Marketplace", "desc": "Product catalog, shopping cart, checkout, and admin order tracking."},
            {"name": "Corporate Business & Agency Portal", "desc": "Interactive services showcase, lead capture forms, and blog publishing."},
            {"name": "Student Assessment & Exam Portal", "desc": "Timed quizzes, automated grading, user dashboards, and certificate generation."},
            {"name": "Interactive Personal Portfolio Website", "desc": "Showcasing live projects, contact inquiries, and responsive resume sections."}
        ]

    context = {
        'course': course,
        'related_courses': related_courses,
        'syllabus_modules': syllabus_modules,
        'tools_list': tools_list,
        'projects_list': projects_list,
    }
    return render(request, 'course_detail.html', context)


def fees_structure(request):
    all_courses = TrainingCourse.objects.filter(is_active=True).order_by('id')
    python_course = TrainingCourse.objects.filter(slug='python-web-design').first()
    if not python_course:
        python_course = all_courses.first()

    software_web_courses = all_courses.filter(category__in=[
        'Web Design', 'Software Development', 'Full Stack Development', 
        'Data Science & AI', 'Mobile App Development'
    ])
    machine_courses = all_courses.filter(category='Machine Design')
    circuit_courses = all_courses.filter(category='Circuit Design')
    building_interior_courses = all_courses.filter(category__in=['Building Design', 'Interior Design'])
    textile_fashion_courses = all_courses.filter(category__in=['Textile Design', 'Fashion Design'])

    context = {
        'all_courses': all_courses,
        'python_course': python_course,
        'software_web_courses': software_web_courses,
        'machine_courses': machine_courses,
        'circuit_courses': circuit_courses,
        'building_interior_courses': building_interior_courses,
        'textile_fashion_courses': textile_fashion_courses,
    }
    return render(request, 'fees.html', context)


web_design_hub = fees_structure


def python_web_design_redirect(request):
    return redirect('course_detail', slug='python-web-design')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            reg = form.save()
            messages.success(request, f"Congratulations {reg.full_name}! Your registration for {reg.course_interested} ({reg.get_training_type_display() if hasattr(reg, 'get_training_type_display') else reg.training_type}) has been received successfully. Our admission counselor will contact you shortly!")
            return redirect('registration')
        else:
            messages.error(request, "Please check the form below and correct the highlighted fields.")
    else:
        initial_data = {}
        course_param = request.GET.get('course', '').strip()
        training_param = request.GET.get('training_type', '').strip()
        
        if course_param:
            initial_data['course_interested'] = course_param
        if training_param:
            initial_data['training_type'] = training_param

        form = RegistrationForm(initial=initial_data)

    courses = TrainingCourse.objects.filter(is_active=True)
    return render(request, 'registration.html', {'form': form, 'courses': courses})


def gallery(request):
    return render(request, 'gallery.html')


def placements(request):
    placement_list = Placement.objects.all().order_by('-placed_year', '-created_at')
    return render(request, 'placements.html', {'placements': placement_list})


def job_fair(request):
    return render(request, 'job_fair.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting Maurya Technical! We have received your query and will reply soon.")
            return redirect('contact')
        else:
            messages.error(request, "There was an error submitting your query.")
    else:
        form = ContactForm()

    branches_list = Branch.objects.all()
    return render(request, 'contact.html', {'form': form, 'branches': branches_list})


def blogs(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blogs.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    recent_posts = BlogPost.objects.exclude(id=post.id).order_by('-created_at')[:5]
    return render(request, 'blog_detail.html', {'post': post, 'recent_posts': recent_posts})


def services(request):
    return render(request, 'services.html')


def student_login(request):
    # If already logged in as student, redirect directly to student dashboard
    if request.session.get('student_id'):
        return redirect('student_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        # Check if faculty ID was entered here by mistake
        if username.upper().startswith('MT') and ('FAC' in username.upper() or username.upper() in ['MT2345', 'MT101']):
            faculty = Faculty.objects.filter(is_active=True).filter(
                Q(faculty_id__iexact=username) | Q(phone=username) | Q(email__iexact=username)
            ).first()
            if faculty and faculty.check_password(password):
                request.session['faculty_id'] = faculty.faculty_id
                request.session['faculty_name'] = faculty.name
                messages.success(request, f"Welcome to Faculty Portal, {faculty.name}!")
                return redirect('faculty_dashboard')
            else:
                messages.warning(request, "Aap Faculty account login kar rahe hain. Kripya 'Faculty Login' tab par click karein.")
                return redirect('faculty_login')

        # Check Registered Students in DB
        student = Registration.objects.filter(
            Q(email__iexact=username) | Q(phone=username)
        ).order_by('-created_at').first()

        if student:
            request.session['student_id'] = student.id
            request.session['student_name'] = student.full_name
            messages.success(request, f"Welcome {student.full_name}! Successfully logged into Maurya Student Portal.")
            return redirect('student_dashboard')

        # Demo Student Login fallback
        if (username.lower() in ['student@mauryatechnical.in', 'student@gmail.com', 'demo@student.com'] and password in ['123456', 'student123', 'password']) or (username and password == '123456'):
            # Fetch any recent registration or create dummy context
            dummy_student = Registration.objects.last()
            if dummy_student:
                request.session['student_id'] = dummy_student.id
            else:
                dummy_student = Registration.objects.create(
                    full_name=username.split('@')[0].capitalize(),
                    email=username,
                    phone='9876543210',
                    college='BBD University Lucknow',
                    branch='Computer Science & Engineering',
                    course_interested='Python Full-Stack & Django',
                    training_type='winter_2026',
                    city='Lucknow'
                )
                request.session['student_id'] = dummy_student.id

            messages.success(request, f"Welcome, {dummy_student.full_name}! Logged into Maurya Technical Student Portal.")
            return redirect('student_dashboard')
        else:
            messages.error(request, "Aapka registration nahi mila. Kripya pehle 'Online Registration' form bharein ya apna registered Email / Phone Number dalein.")

    return render(request, 'student_login.html')


def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        messages.info(request, "Student Portal mein pravesh karne ke liye kripya apna registered Email ya Mobile number dalkar login karein.")
        return redirect('student_login')

    student = Registration.objects.filter(id=student_id).first()
    if not student:
        student = Registration.objects.order_by('-created_at').first()

    return render(request, 'student_dashboard.html', {'student': student})


def student_logout(request):
    request.session.pop('student_id', None)
    request.session.pop('student_name', None)
    messages.success(request, "Aap Student Portal se successfully logout ho gaye hain.")
    return redirect('student_login')



def faculty_login(request):
    # If already authenticated in session, go to dashboard
    if request.session.get('faculty_id'):
        return redirect('faculty_dashboard')

    if request.method == 'POST':
        faculty_id_input = request.POST.get('faculty_id', '').strip()
        password_input = request.POST.get('password', '').strip()

        faculty = Faculty.objects.filter(
            faculty_id__iexact=faculty_id_input,
            is_active=True
        ).first()

        # Also support login by registered phone number
        if not faculty:
            faculty = Faculty.objects.filter(
                phone=faculty_id_input,
                is_active=True
            ).first()

        if faculty and faculty.check_password(password_input):
            request.session['faculty_id'] = faculty.faculty_id
            request.session['faculty_name'] = faculty.name
            messages.success(request, f"Welcome to Maurya Faculty Portal, {faculty.name}!")
            return redirect('faculty_dashboard')
        else:
            messages.error(request, "Invalid Faculty ID / Mobile Number or Password. Please try again or contact IT Admin.")

    return render(request, 'faculty_login.html')


def faculty_dashboard(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        messages.info(request, "Please log in with your Faculty ID to access the dashboard.")
        return redirect('faculty_login')

    faculty = get_object_or_404(Faculty, faculty_id=faculty_id, is_active=True)

    today = timezone.now().date()
    now_time = timezone.now().time()

    # Handle Today's Punch-In / Attendance
    if request.method == 'POST' and request.POST.get('action') == 'punch_in':
        att, created = FacultyAttendance.objects.get_or_create(
            faculty=faculty,
            date=today,
            defaults={'status': 'present', 'check_in': now_time}
        )
        if not created and not att.check_in:
            att.check_in = now_time
            att.status = 'present'
            att.save()
        messages.success(request, f"Attendance marked successfully! Punch-in time: {now_time.strftime('%I:%M %p')}")
        return redirect('faculty_dashboard')

    today_attendance = FacultyAttendance.objects.filter(faculty=faculty, date=today).first()

    # Monthly Attendance Calculation (Last 30 days / Current Month)
    first_day_of_month = today.replace(day=1)
    attendances_month = FacultyAttendance.objects.filter(faculty=faculty, date__gte=first_day_of_month)
    total_logged_days = attendances_month.count() or 1
    present_days = attendances_month.filter(status='present').count()
    leave_days = attendances_month.filter(status='leave').count()
    half_days = attendances_month.filter(status='half_day').count()
    absent_days = attendances_month.filter(status='absent').count()

    attendance_percentage = round((present_days / total_logged_days) * 100) if total_logged_days else 100

    # Recent Attendance History (Last 15 records)
    recent_attendances = FacultyAttendance.objects.filter(faculty=faculty).order_by('-date')[:15]

    # Salary Slips
    salary_slips = SalarySlip.objects.filter(faculty=faculty).order_by('-pay_date')
    if not salary_slips.exists():
        from decimal import Decimal
        import datetime
        sal = faculty.monthly_salary or Decimal('45000.00')
        SalarySlip.objects.create(
            faculty=faculty,
            month_year='August 2026',
            pay_date=datetime.date(2026, 9, 1),
            basic_salary=sal * Decimal('0.65'),
            hra=sal * Decimal('0.20'),
            special_allowance=sal * Decimal('0.15'),
            bonus=Decimal('2000.00'),
            pf_deduction=Decimal('1800.00'),
            tds_deduction=Decimal('1000.00'),
            other_deduction=Decimal('0.00'),
            net_salary=(sal + Decimal('2000.00') - Decimal('2800.00')),
            payment_mode='Bank Transfer (NEFT)',
            transaction_id='TXN-MT-202608-8858',
            status='paid'
        )
        SalarySlip.objects.create(
            faculty=faculty,
            month_year='July 2026',
            pay_date=datetime.date(2026, 8, 1),
            basic_salary=sal * Decimal('0.65'),
            hra=sal * Decimal('0.20'),
            special_allowance=sal * Decimal('0.15'),
            bonus=Decimal('0.00'),
            pf_deduction=Decimal('1800.00'),
            tds_deduction=Decimal('1000.00'),
            other_deduction=Decimal('0.00'),
            net_salary=(sal - Decimal('2800.00')),
            payment_mode='Bank Transfer (NEFT)',
            transaction_id='TXN-MT-202607-7412',
            status='paid'
        )
        salary_slips = SalarySlip.objects.filter(faculty=faculty).order_by('-pay_date')

    latest_salary = salary_slips.first()

    context = {
        'faculty': faculty,
        'today': today,
        'today_attendance': today_attendance,
        'present_days': present_days,
        'leave_days': leave_days,
        'half_days': half_days,
        'absent_days': absent_days,
        'attendance_percentage': attendance_percentage,
        'recent_attendances': recent_attendances,
        'salary_slips': salary_slips,
        'latest_salary': latest_salary,
    }
    return render(request, 'faculty_dashboard.html', context)


def salary_slip_view(request, slip_id):
    faculty_id = request.session.get('faculty_id')
    slip = get_object_or_404(SalarySlip, id=slip_id)

    # Security: If faculty is logged in, only allow viewing their own slip
    if faculty_id and slip.faculty.faculty_id != faculty_id:
        messages.error(request, "Unauthorized access to salary slip.")
        return redirect('faculty_dashboard')

    return render(request, 'salary_slip.html', {'slip': slip, 'faculty': slip.faculty})


def faculty_logout(request):
    request.session.pop('faculty_id', None)
    request.session.pop('faculty_name', None)
    messages.success(request, "You have been logged out of the Faculty Portal.")
    return redirect('faculty_login')


