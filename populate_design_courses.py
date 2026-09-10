import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maurya_technical.settings')
django.setup()

from core.models import TrainingCourse

def populate_courses():
    print("Populating Design Courses with Exact Subjects & Fees...")

    design_courses = [
        {
            "title": "WEB DESIGN & DEVELOPMENT",
            "slug": "web-design",
            "category": "Web Design",
            "duration": "both",
            "badge_text": "GOVT. REGISTERED DESIGN COURSE 2026",
            "fee_45_days": "₹4,000",
            "fee_6_months": "₹18,000",
            "short_description": "Complete Web Design solutions covering Python Web Design, HTML5, CSS3, JavaScript, Bootstrap 5, Django framework, and live website hosting.",
            "full_description": "Comprehensive Web Design program at Maurya Technical Private Limited (Alambagh Lucknow). Learn end-to-end website architecture, modern UI layout design, interactive frontend engineering, and powerful Python Django backend development.",
            "features": "Python Web Design, HTML5 & CSS3 Web Architecture, JavaScript & Dynamic Interactivity, Bootstrap 5 Responsive Design, Django Web Framework & MVT, Database Modeling (SQLite / PostgreSQL), RESTful APIs & Cloud Deployment, 100% Placement Support",
            "image_url": "/static/images/project_2_ecommerce_platform.jpg",
            "is_featured": True,
            "is_active": True
        },
        {
            "title": "PYTHON WEB DESIGN & DEVELOPMENT",
            "slug": "python-web-design",
            "category": "Web Design",
            "duration": "both",
            "badge_text": "FEATURED WEB DESIGN PROGRAM",
            "fee_45_days": "₹4,000",
            "fee_6_months": "₹18,000",
            "short_description": "Master responsive web design, HTML5, CSS3, JavaScript, Python programming, and Django Web Framework to build modern dynamic web applications.",
            "full_description": "Our Python Web Design & Development program at Maurya Technical Private Limited (Alambagh Lucknow) is structured for engineering and diploma students. You will master modern UI wireframing, semantic HTML5, advanced CSS3 (Flexbox & Grid), Bootstrap 5 responsiveness, interactive JavaScript, and backend web architecture with Python and Django.",
            "features": "Python Web Design Basics, Semantic HTML5 & CSS3 Flexbox, JavaScript DOM & AJAX, Bootstrap 5 Responsive Prototyping, Python Object-Oriented Programming, Django MVT Architecture, Database Modeling (SQLite/PostgreSQL), Live Capstone Project & Cloud Deployment",
            "image_url": "/static/images/project_2_ecommerce_platform.jpg",
            "is_featured": True,
            "is_active": True
        },
        {
            "title": "MACHINE DESIGN",
            "slug": "machine-design",
            "category": "Machine Design",
            "duration": "both",
            "badge_text": "MECHANICAL CAD & DESIGN",
            "fee_45_days": "₹4,000",
            "fee_6_months": "₹18,000",
            "short_description": "Comprehensive Mechanical & Machine Design covering Engineering Drawing, AutoCAD, SolidWorks, CATIA, 3D Modeling, and Machine Assembly.",
            "full_description": "Professional Machine Design training program at Maurya Technical Private Limited. Master engineering drawings, parametric 3D modeling, component drafting, assembly simulation, and industrial manufacturing standards.",
            "features": "Engineering Drawing, AutoCAD, SolidWorks, CATIA, 3D Modeling, 2D Drafting, Machine Components & Assembly, Mechanical Design Basics",
            "image_url": "/static/images/project_4_hrms_payroll.jpg",
            "is_featured": True,
            "is_active": True
        },
        {
            "title": "CIRCUIT DESIGN",
            "slug": "circuit-design",
            "category": "Circuit Design",
            "duration": "both",
            "badge_text": "ELECTRONICS & EMBEDDED DESIGN",
            "fee_45_days": "₹4,000",
            "fee_6_months": "₹18,000",
            "short_description": "Electronic circuit design covering Basic Electronics, Electrical Circuit Basics, PCB Design, Circuit Simulation, Arduino, Proteus, and KiCad.",
            "full_description": "Practical Circuit Design program at Maurya Technical Private Limited. Designed for Electrical & Electronics engineering trainees to gain hands-on expertise in PCB schematic design, simulation, Arduino interfacing, and embedded hardware prototyping.",
            "features": "Basic Electronics, Electrical Circuit Basics, PCB Design, Circuit Simulation, Arduino Basics, Embedded System Basics, Proteus, KiCad / EasyEDA",
            "image_url": "/static/images/project_3_ai_exam_portal.jpg",
            "is_featured": True,
            "is_active": True
        },
        {
            "title": "BUILDING DESIGN",
            "slug": "building-design",
            "category": "Building Design",
            "duration": "both",
            "badge_text": "CIVIL & ARCHITECTURAL DESIGN",
            "fee_45_days": "₹4,000",
            "fee_6_months": "₹18,000",
            "short_description": "Civil and architectural building design covering Architectural Drawing, AutoCAD, 2D Floor Plan, 3D Building Modeling, Revit, and SketchUp.",
            "full_description": "Industry-grade Building Design training at Maurya Technical Private Limited. Learn architectural drafting, 2D residential/commercial floor planning, 3D BIM modeling with Revit, and structural drawing fundamentals.",
            "features": "Architectural Drawing, AutoCAD, 2D Floor Plan, 3D Building Modeling, Revit, SketchUp, Building Planning, Structural Drawing Basics",
            "image_url": "/static/images/maurya_building_office.png",
            "is_featured": True,
            "is_active": True
        },
        {
            "title": "INTERIOR DESIGN",
            "slug": "interior-design",
            "category": "Interior Design",
            "duration": "both",
            "badge_text": "INTERIOR ARCHITECTURE & 3D",
            "fee_45_days": "₹4,000",
            "fee_6_months": "₹18,000",
            "short_description": "Professional interior design covering Space Planning, Furniture Layout, AutoCAD, SketchUp, 3D Interior Modeling, V-Ray, and Lighting Design.",
            "full_description": "Creative and technical Interior Design training program at Maurya Technical Private Limited. Master spatial ergonomics, modular furniture drafting, 3D photorealistic V-Ray rendering, material palettes, and architectural lighting design.",
            "features": "Space Planning, Furniture Layout, AutoCAD, SketchUp, 3D Interior Modeling, V-Ray / Rendering, Material & Color Selection, Lighting Design",
            "image_url": "/static/images/maurya_event_2.jpg",
            "is_featured": True,
            "is_active": True
        },
        {
            "title": "TEXTILE DESIGN",
            "slug": "textile-design",
            "category": "Textile Design",
            "duration": "both",
            "badge_text": "TEXTILE TECHNOLOGY & CAD",
            "fee_45_days": "₹4,000",
            "fee_6_months": "₹18,000",
            "short_description": "Modern textile design covering Textile Designing Basics, Fabric Design, Pattern Making, Surface Design, Digital Textile Printing, and CorelDRAW.",
            "full_description": "Industry-oriented Textile Design course at Maurya Technical Private Limited. Gain practical mastery over fabric structures, repeating patterns, digital textile printing workflows, Photoshop/CorelDRAW styling, and textile surface ornamentation.",
            "features": "Textile Designing Basics, Fabric Design, Pattern Making, Surface Design, Digital Textile Printing, Photoshop, CorelDRAW, Color & Pattern Development",
            "image_url": "/static/images/maurya_event_3.jpg",
            "is_featured": True,
            "is_active": True
        },
        {
            "title": "FASHION DESIGN",
            "slug": "fashion-design",
            "category": "Fashion Design",
            "duration": "both",
            "badge_text": "FASHION TECHNOLOGY & APPAREL",
            "fee_45_days": "₹4,000",
            "fee_6_months": "₹18,000",
            "short_description": "Comprehensive Fashion Design covering Fashion Illustration, Garment Designing, Pattern Making, Draping, CorelDRAW/Photoshop, and Fashion CAD.",
            "full_description": "Professional Fashion Design training at Maurya Technical Private Limited. Master apparel sketching, digital garment pattern making CAD, fabric draping techniques, garment construction, and runway collection portfolio development.",
            "features": "Fashion Illustration, Garment Designing, Pattern Making, Draping, Textile & Fabric Knowledge, CorelDRAW / Photoshop, Fashion CAD, Apparel Design",
            "image_url": "/static/images/maurya_event_1.jpg",
            "is_featured": True,
            "is_active": True
        }
    ]

    for item in design_courses:
        slug = item.pop("slug")
        obj, created = TrainingCourse.objects.update_or_create(
            slug=slug,
            defaults=item
        )
        action = "Created" if created else "Updated"
        print(f"{action} course: {obj.title} (slug: {slug})")

    print("All design courses with exact subjects and fees updated successfully!")

if __name__ == '__main__':
    populate_courses()
