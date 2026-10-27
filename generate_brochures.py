import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable, KeepTogether
)

def create_training_brochure(output_path, logo_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    primary_color = colors.HexColor('#0b192c')
    accent_red = colors.HexColor('#a81b1b')
    gold_color = colors.HexColor('#d97706')
    light_bg = colors.HexColor('#f8fafc')
    dark_gray = colors.HexColor('#334155')

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=primary_color,
        alignment=0
    )
    
    sub_title_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=accent_red,
        alignment=0
    )

    h1_style = ParagraphStyle(
        'Heading1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=primary_color,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=dark_gray
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    badge_style = ParagraphStyle(
        'Badge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    story = []

    # Header with Logo & Institute Details
    logo_img = None
    if os.path.exists(logo_path):
        try:
            logo_img = Image(logo_path, width=1.1*inch, height=1.1*inch)
        except Exception:
            logo_img = Paragraph("<b>MTPL</b>", title_style)
    else:
        logo_img = Paragraph("<b>MTPL</b>", title_style)

    header_text = [
        Paragraph("<b>MAURYA TECHNICAL PRIVATE LIMITED</b>", title_style),
        Paragraph("REGISTERED UNDER MINISTRY OF CORPORATE AFFAIRS (GOVT. OF INDIA) & ISO 9001:2015 CERTIFIED", sub_title_style),
        Spacer(1, 3),
        Paragraph("<b>Campus:</b> Alambagh, Lucknow, Uttar Pradesh - 226005 | <b>Helpline:</b> +91 88582 98247 | +91 88878 39689", body_style),
        Paragraph("<b>Web:</b> www.mauryatechnical.in | <b>Email:</b> info@mauryatechnical.in / director@mauryatechnical.in", body_style)
    ]

    header_table = Table([[logo_img, header_text]], colWidths=[1.3*inch, 6.0*inch])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=2, color=accent_red, spaceAfter=10))

    # Title Banner
    banner_p = Paragraph(
        "<font size='13'><b>OFFICIAL INDUSTRIAL TRAINING & INTERNSHIP BROCHURE 2026</b></font><br/>"
        "<font size='9'>06 WEEKS (45 DAYS) PROJECT TRAINING &amp; 06 MONTHS COMPREHENSIVE INDUSTRIAL INTERNSHIPS</font>",
        ParagraphStyle('Banner', parent=title_style, textColor=colors.white, alignment=1)
    )
    banner_table = Table([[banner_p]], colWidths=[7.3*inch])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 10))

    # About Section
    story.append(Paragraph("1. ABOUT MAURYA TECHNICAL", h1_style))
    story.append(Paragraph(
        "Maurya Technical Private Limited is a premier technical skill development and industrial training organization located in Alambagh, Lucknow. "
        "We are dedicated to preparing undergraduate and diploma engineers (B.Tech, Diploma, BCA, MCA, B.Sc-IT, M.Tech) for high-growth technical careers. "
        "With state-of-the-art computer labs, corporate project leads, and an outcome-driven syllabus aligned directly with corporate hiring demands, "
        "over 15,000+ students have been trained and placed in leading software product and IT service enterprises across India.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # Core Features (4 highlights in grid)
    f1 = Paragraph("<b>100% Practical & Live Coding</b><br/>No rote learning; build real production applications from day one.", body_style)
    f2 = Paragraph("<b>Govt. Valid & ISO Certification</b><br/>Globally verifiable online certificate ID for job interviews.", body_style)
    f3 = Paragraph("<b>Dedicated Placement Support</b><br/>Campus hiring drives, resume polishing, and mock technical rounds.", body_style)
    f4 = Paragraph("<b>Industry Mentors</b><br/>Direct training by working software architects & design leads.", body_style)
    
    feat_table = Table([[f1, f2], [f3, f4]], colWidths=[3.6*inch, 3.6*inch])
    feat_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), light_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(feat_table)
    story.append(Spacer(1, 12))

    # Course Table
    story.append(Paragraph("2. POPULAR TRAINING & INTERNSHIP PROGRAMS", h1_style))
    
    courses_data = [
        [
            Paragraph("<b>Program Title</b>", body_bold),
            Paragraph("<b>Domain / Category</b>", body_bold),
            Paragraph("<b>45 Days / 6 Wks</b>", body_bold),
            Paragraph("<b>6 Months Internship</b>", body_bold)
        ],
        [
            Paragraph("Python Full Stack with Django", body_style),
            Paragraph("Software Development", body_style),
            Paragraph("Rs. 4,000", body_style),
            Paragraph("Rs. 18,000", body_style)
        ],
        [
            Paragraph("Data Analytics & AI with Python", body_style),
            Paragraph("Data Science & Machine Learning", body_style),
            Paragraph("Rs. 4,000", body_style),
            Paragraph("Rs. 18,000", body_style)
        ],
        [
            Paragraph("MERN Stack Web Development", body_style),
            Paragraph("Full Stack Web Engineering", body_style),
            Paragraph("Rs. 4,000", body_style),
            Paragraph("Rs. 18,000", body_style)
        ],
        [
            Paragraph("Flutter & Dart Cross-Platform App", body_style),
            Paragraph("Mobile App Development", body_style),
            Paragraph("Rs. 4,000", body_style),
            Paragraph("Rs. 18,000", body_style)
        ],
        [
            Paragraph("Machine Design & Mechanical CAD (SolidWorks/AutoCAD)", body_style),
            Paragraph("Mechanical & Production CAD", body_style),
            Paragraph("Rs. 4,000", body_style),
            Paragraph("Rs. 18,000", body_style)
        ],
        [
            Paragraph("Building Design & Architectural BIM (Revit/STAAD)", body_style),
            Paragraph("Civil & Structural CAD", body_style),
            Paragraph("Rs. 4,000", body_style),
            Paragraph("Rs. 18,000", body_style)
        ],
        [
            Paragraph("Circuit & PCB Design with Embedded IoT", body_style),
            Paragraph("Electronics & Electrical CAD", body_style),
            Paragraph("Rs. 4,000", body_style),
            Paragraph("Rs. 18,000", body_style)
        ],
        [
            Paragraph("Textile CAD & Fashion Design Suite", body_style),
            Paragraph("Design & Apparel CAD", body_style),
            Paragraph("Rs. 4,000", body_style),
            Paragraph("Rs. 18,000", body_style)
        ]
    ]

    c_table = Table(courses_data, colWidths=[2.8*inch, 2.3*inch, 1.1*inch, 1.1*inch])
    c_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0b192c')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
    ]))
    story.append(c_table)
    story.append(Spacer(1, 12))

    # Multi-branch Presence & Admission Procedure
    story.append(Paragraph("3. OUR BRANCHES & LEARNING CENTERS", h1_style))
    branches_p = Paragraph(
        "<b>Lucknow (Head Office):</b> Alambagh, Lucknow - 226005 | <b>Phone:</b> +91 88582 98247<br/>"
        "<b>Gorakhpur Center:</b> Civil Lines / Golghar, Near Railway Station | <b>Varanasi Center:</b> Sigra / Rathyatra<br/>"
        "<b>Ghaziabad Center:</b> RDC Raj Nagar | <b>Noida Center:</b> Sector 62, Electronic City",
        body_style
    )
    story.append(branches_p)
    story.append(Spacer(1, 10))

    # Admission Instructions Callout
    enroll_p = Paragraph(
        "<b>HOW TO REGISTER & ENROLL:</b><br/>"
        "1. Visit <b>www.mauryatechnical.in/registration/</b> to fill out the online admission form.<br/>"
        "2. Choose your preferred batch mode (Classroom / Online Live Batch).<br/>"
        "3. Instant student portal credentials and batch schedule will be issued upon registration.",
        ParagraphStyle('Enroll', parent=body_style, textColor=colors.HexColor('#1e293b'))
    )
    enroll_table = Table([[enroll_p]], colWidths=[7.3*inch])
    enroll_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#fef3c7')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#f59e0b')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(enroll_table)
    story.append(Spacer(1, 8))

    # Footer note
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e1'), spaceAfter=5))
    footer_p = Paragraph(
        "<font size='7' color='#64748b'>Maurya Technical Private Limited | CIN Registered with MCA | Official Training Brochure 2026. "
        "Verify online at https://mauryatechnical.in/verify-certificate/</font>",
        ParagraphStyle('Footer', parent=styles['Normal'], alignment=1)
    )
    story.append(footer_p)

    doc.build(story)
    print("Training brochure built successfully at:", output_path)


def create_placement_brochure(output_path, logo_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    primary_color = colors.HexColor('#0b192c')
    accent_red = colors.HexColor('#a81b1b')
    emerald_color = colors.HexColor('#059669')
    light_bg = colors.HexColor('#f8fafc')
    dark_gray = colors.HexColor('#334155')

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=primary_color,
        alignment=0
    )
    
    sub_title_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=accent_red,
        alignment=0
    )

    h1_style = ParagraphStyle(
        'Heading1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=primary_color,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=dark_gray
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    story = []

    # Header with Logo & Institute Details
    logo_img = None
    if os.path.exists(logo_path):
        try:
            logo_img = Image(logo_path, width=1.1*inch, height=1.1*inch)
        except Exception:
            logo_img = Paragraph("<b>MTPL</b>", title_style)
    else:
        logo_img = Paragraph("<b>MTPL</b>", title_style)

    header_text = [
        Paragraph("<b>MAURYA TECHNICAL PRIVATE LIMITED</b>", title_style),
        Paragraph("TRAINING &amp; CORPORATE PLACEMENT DIVISION | ALAMBAGH, LUCKNOW", sub_title_style),
        Spacer(1, 3),
        Paragraph("<b>Corporate Relations &amp; Placement Cell:</b> +91 88582 98247 | +91 88878 39689", body_style),
        Paragraph("<b>Email:</b> director@mauryatechnical.in / info@mauryatechnical.in | <b>Web:</b> www.mauryatechnical.in", body_style)
    ]

    header_table = Table([[logo_img, header_text]], colWidths=[1.3*inch, 6.0*inch])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=2, color=emerald_color, spaceAfter=10))

    # Banner
    banner_p = Paragraph(
        "<font size='13'><b>ANNUAL PLACEMENT &amp; CORPORATE RECRUITMENT BROCHURE 2026</b></font><br/>"
        "<font size='9'>BUILDING INDUSTRY-READY TECH PROFESSIONALS | 94%+ PLACEMENT TRACK RECORD</font>",
        ParagraphStyle('BannerPlacement', parent=title_style, textColor=colors.white, alignment=1)
    )
    banner_table = Table([[banner_p]], colWidths=[7.3*inch])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#064e3b')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 10))

    # Placement Metrics KPI Row (3 stat cards)
    kpi1 = Paragraph("<font size='15' color='#059669'><b>94.6%</b></font><br/><font size='8'>Placement Success Rate</font>", ParagraphStyle('KPI', alignment=1))
    kpi2 = Paragraph("<font size='15' color='#0b192c'><b>Rs. 8.5 LPA</b></font><br/><font size='8'>Highest Package Offered</font>", ParagraphStyle('KPI', alignment=1))
    kpi3 = Paragraph("<font size='15' color='#a81b1b'><b>250+</b></font><br/><font size='8'>Active Hiring Partners</font>", ParagraphStyle('KPI', alignment=1))
    kpi4 = Paragraph("<font size='15' color='#d97706'><b>Rs. 5.8 LPA</b></font><br/><font size='8'>Average CTC Package</font>", ParagraphStyle('KPI', alignment=1))

    kpi_table = Table([[kpi1, kpi2, kpi3, kpi4]], colWidths=[1.82*inch, 1.82*inch, 1.82*inch, 1.82*inch])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), light_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(kpi_table)
    story.append(Spacer(1, 10))

    # About Placement Cell
    story.append(Paragraph("1. MESSAGE FROM TRAINING &amp; PLACEMENT HEAD", h1_style))
    story.append(Paragraph(
        "At Maurya Technical Private Limited, our Training &amp; Placement Cell bridges the gap between academic theory and real enterprise standards. "
        "Through rigorous hands-on curriculum, agile project management simulations, daily coding sprints, and personality enhancement sessions, "
        "our trainees graduate equipped with the technical depth and professional acumen that leading tech recruiters actively seek. "
        "We host on-campus job fairs, corporate pool drives, and bilateral hiring partnerships with established MNCs and high-growth technology startups.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # Real Student Placements Table
    story.append(Paragraph("2. RECENT STUDENT PLACEMENTS (BATCH 2025 - 2026)", h1_style))
    
    placements_data = [
        [
            Paragraph("<b>Candidate Name</b>", body_bold),
            Paragraph("<b>Training Specialization</b>", body_bold),
            Paragraph("<b>Selected Recruiter</b>", body_bold),
            Paragraph("<b>Role / Designation</b>", body_bold),
            Paragraph("<b>CTC Package</b>", body_bold)
        ],
        [
            Paragraph("Annu Singh", body_style),
            Paragraph("Python with Django", body_style),
            Paragraph("NIVRAJ Software Solutions", body_style),
            Paragraph("Software Developer", body_style),
            Paragraph("5.8 LPA", body_style)
        ],
        [
            Paragraph("Kanti Pal", body_style),
            Paragraph("Full Stack Web Dev", body_style),
            Paragraph("Vartax Global Tech Pvt. Ltd.", body_style),
            Paragraph("Software Engineer", body_style),
            Paragraph("6.2 LPA", body_style)
        ],
        [
            Paragraph("Saloni Katara", body_style),
            Paragraph("Python &amp; Data Analytics", body_style),
            Paragraph("Vartax Global Tech Pvt. Ltd.", body_style),
            Paragraph("Web Developer", body_style),
            Paragraph("5.5 LPA", body_style)
        ],
        [
            Paragraph("Neha Maurya", body_style),
            Paragraph("Python with Django", body_style),
            Paragraph("TCS (Tata Consultancy Services)", body_style),
            Paragraph("Backend Engineer", body_style),
            Paragraph("6.0 LPA", body_style)
        ],
        [
            Paragraph("Priya Sharma", body_style),
            Paragraph("MERN Stack Web Dev", body_style),
            Paragraph("Wipro Technologies", body_style),
            Paragraph("Frontend Developer", body_style),
            Paragraph("5.2 LPA", body_style)
        ],
        [
            Paragraph("Amit Kumar", body_style),
            Paragraph("Full Stack Development", body_style),
            Paragraph("Infosys Limited", body_style),
            Paragraph("Software Engineer", body_style),
            Paragraph("5.5 LPA", body_style)
        ],
    ]

    p_table = Table(placements_data, colWidths=[1.5*inch, 1.8*inch, 1.8*inch, 1.3*inch, 0.9*inch])
    p_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#064e3b')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, light_bg]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
    ]))
    story.append(p_table)
    story.append(Spacer(1, 10))

    # Corporate Recruitment Process & Recruiters
    story.append(Paragraph("3. OUR PROMINENT RECRUITING PARTNERS", h1_style))
    story.append(Paragraph(
        "<b>Prominent Recruiters:</b> Tata Consultancy Services (TCS), Infosys, Wipro Technologies, Vartax Global Technologies, "
        "Nivraj Software Solutions, Tech Mahindra, HCL Technologies, Cognizant, L&amp;T Infotech, and 200+ partner tech firms.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # Recruiter Invitation Card
    recruiter_p = Paragraph(
        "<b>INVITATION TO CORPORATE RECRUITERS &amp; HR TEAMS:</b><br/>"
        "Maurya Technical invites corporate HR managers, technical heads, and talent acquisition teams to organize on-campus and virtual hiring drives. "
        "We offer pre-screened, technically vetted, and project-ready candidates across Python, Full Stack, Data Science, Flutter, and Engineering CAD.<br/>"
        "<b>Email:</b> placements@mauryatechnical.in / director@mauryatechnical.in | <b>Direct Cell:</b> +91 88582 98247",
        ParagraphStyle('Recruiter', parent=body_style, textColor=colors.HexColor('#064e3b'))
    )
    recruiter_table = Table([[recruiter_p]], colWidths=[7.3*inch])
    recruiter_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ecfdf5')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#10b981')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(recruiter_table)
    story.append(Spacer(1, 8))

    # Footer
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e1'), spaceAfter=5))
    footer_p = Paragraph(
        "<font size='7' color='#64748b'>Maurya Technical Private Limited | Placement Brochure 2026. "
        "Explore student profiles and placement records at https://mauryatechnical.in/placements/</font>",
        ParagraphStyle('Footer', parent=styles['Normal'], alignment=1)
    )
    story.append(footer_p)

    doc.build(story)
    print("Placement brochure built successfully at:", output_path)

if __name__ == '__main__':
    logo = r'c:\Users\simiy_otrc7ib\Desktop\mauraya\static\images\maurya_official_logo.png'
    out_dir = r'c:\Users\simiy_otrc7ib\Desktop\mauraya\static\brochures'
    os.makedirs(out_dir, exist_ok=True)
    
    t_pdf = os.path.join(out_dir, 'Maurya_Technical_Training_Brochure_2026.pdf')
    p_pdf = os.path.join(out_dir, 'Maurya_Technical_Placement_Brochure_2026.pdf')
    
    create_training_brochure(t_pdf, logo)
    create_placement_brochure(p_pdf, logo)
