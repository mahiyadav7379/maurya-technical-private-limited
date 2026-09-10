import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maurya_technical.settings')
django.setup()

from core.models import Placement, Branch, TeamMember

def populate():
    print("Populating Real Placements Data...")

    # Clear previous sample placements
    Placement.objects.all().delete()

    placements_data = [
        {
            "student_name": "Annu Singh",
            "course_taken": "Python with Django & Web Development",
            "company_name": "NIVRAJ Software Solutions (P) Ltd.",
            "designation": "Software Developer",
            "package": "5.8 LPA",
            "student_image_url": "/static/images/placement_annu_singh.png",
            "placed_year": 2026
        },
        {
            "student_name": "Kanti Pal",
            "course_taken": "Full Stack Web Development",
            "company_name": "Vartax Global Technologies Pvt. Ltd.",
            "designation": "Software Engineer",
            "package": "6.2 LPA",
            "student_image_url": "/static/images/placement_kanti_pal.png",
            "placed_year": 2026
        },
        {
            "student_name": "Saloni Katara",
            "course_taken": "Python & Data Analytics",
            "company_name": "Vartax Global Technologies Pvt. Ltd.",
            "designation": "Web Developer",
            "package": "5.5 LPA",
            "student_image_url": "/static/images/placement_saloni_katara.png",
            "placed_year": 2026
        },
        {
            "student_name": "Rahul Maurya",
            "course_taken": "Python with Django",
            "company_name": "TCS (Tata Consultancy Services)",
            "designation": "Backend Engineer",
            "package": "6.0 LPA",
            "student_image_url": "/static/images/maurya_event_1.jpg",
            "placed_year": 2026
        },
        {
            "student_name": "Priya Sharma",
            "course_taken": "MERN Stack Development",
            "company_name": "Wipro Technologies",
            "designation": "Frontend Developer",
            "package": "5.2 LPA",
            "student_image_url": "/static/images/maurya_event_3.jpg",
            "placed_year": 2026
        },
        {
            "student_name": "Amit Kumar",
            "course_taken": "Full Stack Development",
            "company_name": "Infosys",
            "designation": "Software Engineer",
            "package": "5.5 LPA",
            "student_image_url": "/static/images/maurya_event_5.jpg",
            "placed_year": 2026
        }
    ]

    for p in placements_data:
        placement = Placement.objects.create(**p)
        print(f"Added Placement: {placement.student_name} at {placement.company_name}")

    print("Placements population completed successfully!")

    # Populate Team / Leadership
    print("Populating Team & Director Data...")
    TeamMember.objects.filter(name="Vivek Kushawaha").delete()
    TeamMember.objects.create(
        name="Vivek Kushawaha",
        role="Founder & Director",
        tech_stack="Academic & Industry Leadership / Electrical & IT Engineering",
        bio="Founder & Director of Maurya Technical Private Limited, Assistant Professor, Dean Student Welfare & Head of Department (Electrical Engineering) at M.G. Institute of Management & Technology, Lucknow (Affiliated to Dr. APJ Abdul Kalam Technical University Lucknow).",
        phone="+91 88878 39689",
        email="info@mauryatechnical.com",
        image_url="/static/images/director_vivek_kushawaha.png",
        is_active=True
    )
    print("Added Vivek Kushawaha (Founder & Director) successfully!")

if __name__ == '__main__':
    populate()
