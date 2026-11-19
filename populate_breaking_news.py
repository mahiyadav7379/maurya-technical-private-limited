import os
import sys
import django

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maurya_technical.settings')
django.setup()

from django.utils import timezone
from core.models import BreakingNews

news_data = [
    {
        'title': 'BTEUP Odd Semester Exam 2026: पॉलिटेक्निक 1st, 3rd, 5th सेमेस्टर परीक्षा टाइम-टेबल व दिशा-निर्देश जारी',
        'category': 'polytechnic',
        'badge_text': 'BREAKING NEWS',
        'badge_color': 'danger',
        'short_description': 'प्राविधिक शिक्षा परिषद उत्तर प्रदेश (BTEUP लखनऊ) द्वारा पॉलिटेक्निक विषम सेमेस्टर (Odd Sem) बोर्ड परीक्षाओं की समय सारिणी (Exam Time Table) जारी कर दी गई है। सभी छात्र विषयवार तिथियां व दिशा-निर्देश नीचे पढ़ें।',
        'full_content': """प्राविधिक शिक्षा परिषद उत्तर प्रदेश (BTEUP, Lucknow) द्वारा शैक्षणिक सत्र 2026 के अंतर्गत पॉलिटेक्निक विषम सेमेस्टर (Odd Semester 1st, 3rd & 5th Semester) तथा विशेष बैक पेपर परीक्षाओं का आधिकारिक कार्यक्रम घोषित कर दिया गया है।

मुख्य परीक्षा विवरण:
1. परीक्षा प्रारंभ होने की तिथि: 25 दिसंबर 2026 से प्रदेश भर के राजकीय, अनुदानित एवं निजी पॉलीटेक्निक संस्थानों में बनाए गए नोडल केंद्रों पर।
2. एडमिट कार्ड (Admit Card): परीक्षा से 5 दिन पूर्व यू-राइज पोर्टल (U-Rise Portal) एवं संबंधित पॉलीटेक्निक लॉगिन पर उपलब्ध कराए जाएंगे।
3. परीक्षा का समय: प्रथम पाली प्रातः 09:00 बजे से 11:30 बजे तक तथा द्वितीय पाली दोपहर 02:00 बजे से 04:30 बजे तक।
4. प्रैक्टिकल परीक्षाएं: संस्था स्तर पर विषय विशेषज्ञों द्वारा बाह्य परीक्षकों की निगरानी में लिखित परीक्षा से पूर्व अथवा बाद में आयोजित होंगी।

सभी छात्र-छात्राओं को सख्त निर्देश दिया गया है कि परीक्षा केंद्र पर प्रवेश पत्र के साथ अपना कॉलेज पहचान-पत्र अथवा आधार कार्ड अनिवार्य रूप से साथ लेकर आएं। किसी भी प्रकार का इलेक्ट्रॉनिक उपकरण (स्मार्टवॉच, मोबाइल फोन) परीक्षा कक्ष में वर्जित रहेगा।""",
        'official_link': 'https://bteup.ac.in',
        'official_link_label': 'BTEUP आधिकारिक पोर्टल पर जाएं',
        'author_or_source': 'BTEUP प्राविधिक शिक्षा परिषद, लखनऊ',
        'is_breaking': True,
        'is_pinned': True,
        'views_count': 1240,
        'published_date': timezone.now(),
    },
    {
        'title': 'AKTU B.Tech Odd Semester Exam 2026: परीक्षा फॉर्म, कैरी ओवर (COP) व अंतिम परीक्षा केंद्र सूची जारी',
        'category': 'btech',
        'badge_text': 'URGENT NOTICE',
        'badge_color': 'danger',
        'short_description': 'डॉ. एपीजे अब्दुल कलाम प्राविधिक विश्वविद्यालय (AKTU) द्वारा बी.टेक सभी ब्रांचेस (CS, IT, ME, EC, Civil) के विषम सेमेस्टर परीक्षा फॉर्म भरने व कैरी ओवर परीक्षा केंद्रों की सूची आधिकारिक पोर्टल पर जारी।',
        'full_content': """डॉ. एपीजे अब्दुल कलाम प्राविधिक विश्वविद्यालय (AKTU लखनऊ) के परीक्षा नियंत्रक कार्यालय द्वारा सत्र 2026 हेतु बी.टेक (B.Tech), बी.फार्मा, एमसीए व एमबीए के विषम सेमेस्टर (Odd Sem Phase-1 व Phase-2) परीक्षाओं के संबंध में महत्वपूर्ण दिशा-निर्देश जारी किए गए हैं।

महत्वपूर्ण विवरण एवं दिशा-निर्देश:
• परीक्षा फॉर्म भरने की अंतिम तिथि: 30 नवंबर 2026 (बिना विलंब शुल्क के साथ)।
• कैरी ओवर (Carry Over / COP) फॉर्म: प्रति विषय ₹1,000 परीक्षा शुल्क निर्धारित किया गया है जिसे ईआरपी पोर्टल द्वारा जमा किया जा सकता है।
• परीक्षा केंद्र सूची: प्रदेश के 120+ नोडल केंद्रों पर सीसीटीवी निगरानी एवं लाइव वेबकास्टिंग के माध्यम से परीक्षाएं आयोजित की जाएंगी।
• एडमिट कार्ड जारी होने की तिथि: परीक्षा प्रारंभ होने के 3 दिन पहले छात्रों के AKTU ERP लॉगिन पर डाउनलोड के लिए उपलब्ध रहेगा।

बी.टेक के सभी विद्यार्थियों को सूचित किया जाता है कि वे अपनी 75% उपस्थिति एवं परीक्षा फॉर्म का सत्यापन अपने संबंधित संस्थान के एकेडमिक विभाग से समय रहते पूरा करवा लें।""",
        'official_link': 'https://aktu.ac.in',
        'official_link_label': 'AKTU आधिकारिक वेबसाइट पर जाएं',
        'author_or_source': 'AKTU Examination Controller, Lucknow',
        'is_breaking': True,
        'is_pinned': True,
        'views_count': 980,
        'published_date': timezone.now(),
    },
    {
        'title': 'BTEUP Scrutiny & Re-Evaluation Result 2026 Declared: पॉलिटेक्निक पुनर्मूल्यांकन का रिजल्ट घोषित, सीधा लिंक यहां देखें',
        'category': 'exam_result',
        'badge_text': 'RESULT DECLARED',
        'badge_color': 'success',
        'short_description': 'प्राविधिक शिक्षा परिषद उत्तर प्रदेश ने पॉलिटेक्निक स्क्रूटनी व री-इवैल्युएशन का रिजल्ट घोषित कर दिया है। छात्र अपने एनरोलमेंट नंबर से सीधे परिणाम देख सकते हैं।',
        'full_content': """प्राविधिक शिक्षा परिषद (BTEUP) लखनऊ द्वारा पॉलीटेक्निक सेमेस्टर परीक्षा के स्क्रूटनी एवं पुनर्मूल्यांकन (Scrutiny & Re-evaluation Result 2026) का परीक्षा परिणाम आधिकारिक वेबसाइट पर जारी कर दिया गया है। जिन छात्रों ने अपने अंकों के पुनर्मूल्यांकन के लिए आवेदन किया था, वे अब अपना संशोधित स्कोरकार्ड ऑनलाइन देख सकते हैं।

परिणाम जांचने की स्टेप-बाय-स्टेप प्रक्रिया:
1. BTEUP के आधिकारिक रिजल्ट पोर्टल result.bteup.ac.in पर जाएं।
2. 'View Result of Scrutiny / Re-Evaluation 2026' वाले लिंक पर क्लिक करें।
3. दिए गए बॉक्स में अपना एनरोलमेंट नंबर (जैसे E21...) दर्ज करें और 'Show Result' पर क्लिक करें।
4. अपने संशोधित अंक देखें और भविष्य के संदर्भ के लिए मार्कशीट का प्रिंटआउट सुरक्षित रख लें।

नोट: जिन विद्यार्थियों के अंकों में परिवर्तन हुआ है, उनकी नई संशोधित मार्कशीट परिषद द्वारा सीधे संबंधित संस्थान को प्रेषित की जाएगी।""",
        'official_link': 'https://result.bteup.ac.in',
        'official_link_label': 'BTEUP रिजल्ट पोर्टल खोलें',
        'author_or_source': 'BTEUP Exam Cell, Lucknow',
        'is_breaking': False,
        'is_pinned': False,
        'views_count': 1650,
        'published_date': timezone.now(),
    },
    {
        'title': 'Maurya Technical Mega Campus Placement Drive 2026: 50+ IT व इंजीनियरिंग कंपनियों में Polytechnic और B.Tech की सीधी भर्ती',
        'category': 'job_internship',
        'badge_text': 'JOB FAIR 2026',
        'badge_color': 'warning',
        'short_description': 'मौर्य टेक्निकल प्राइवेट लिमिटेड आलमबाग लखनऊ द्वारा पॉलिटेक्निक डिप्लोमा व बी.टेक फ्रेशर्स छात्रों के लिए विशाल रोजगार मेले का आयोजन। पैकेज ₹3.0 LPA से ₹7.5 LPA तक।',
        'full_content': """मौर्य टेक्निकल प्राइवेट लिमिटेड (पंजीकृत कॉर्पोरेट मंत्रालय, भारत सरकार) द्वारा उत्तर प्रदेश के सभी पॉलिटेक्निक एवं बी.टेक उत्तीर्ण तथा फाइनल ईयर के विद्यार्थियों के लिए एक ऐतिहासिक 'मेगा कैंपस प्लेसमेंट ड्राइव 2026' का आयोजन किया जा रहा है।

प्लेसमेंट ड्राइव की मुख्य विशेषताएं:
• प्रतिभागी कंपनियां: 50 से अधिक प्रतिष्ठित बहुराष्ट्रीय एवं भारतीय कंपनियां (सॉफ्टवेयर डेवलपमेंट, वेब टेक्नोलॉजीज, CAD/CAM, इंडस्ट्रियल ऑटोमेशन, इलेक्ट्रॉनिक्स मैन्युफैक्चरिंग आदि)।
• वेतन पैकेज (CTC): ₹3,00,000 प्रति वर्ष से ₹7,50,000 प्रति वर्ष (मेरिट व इंटरव्यू के आधार पर)।
• पात्रता: B.Tech (CS, IT, ME, EC, Civil, EE) एवं Polytechnic Diploma (All Branches) पासआउट व 2026 अपीयरिंग बैच।
• भर्ती स्थल (Venue): मौर्य टेक्निकल प्राइवेट लिमिटेड, निकट आलमबाग बस स्टैंड / मेट्रो स्टेशन, आलमबाग, लखनऊ।
• आवश्यक दस्तावेज: रेज़्यूमे की 4 प्रतियां, 4 पासपोर्ट साइज फोटो, आधार कार्ड एवं सभी शैक्षणिक प्रमाण पत्रों की छायाप्रतियां।

पंजीकरण प्रक्रिया: छात्र मौर्य टेक्निकल की वेबसाइट पर 'Job Fair' टैब से निःशुल्क रजिस्ट्रेशन कर सकते हैं।""",
        'official_link': 'https://mauryatechnical.in/job-fair/',
        'official_link_label': 'जॉब फेयर के लिए निःशुल्क रजिस्ट्रेशन करें',
        'author_or_source': 'Maurya Technical Training & Placement Cell',
        'is_breaking': True,
        'is_pinned': False,
        'views_count': 1420,
        'published_date': timezone.now(),
    },
    {
        'title': 'UP Scholarship 2026: Polytechnic व B.Tech छात्रवृत्ति स्टेटस व सस्पेक्ट डाटा सुधार की अंतिम तिथि घोषित',
        'category': 'scholarship',
        'badge_text': 'SCHOLARSHIP ALERT',
        'badge_color': 'primary',
        'short_description': 'समाज कल्याण विभाग उत्तर प्रदेश द्वारा पोस्ट मैट्रिक स्कॉलरशिप 2026 का स्टेटस लाइव। सस्पेक्टेड डाटा (Suspect Data) में संशोधन करने और कॉलेज में हार्डकॉपी जमा करने की समय-सीमा जारी।',
        'full_content': """उत्तर प्रदेश सरकार के समाज कल्याण, पिछड़ा वर्ग कल्याण एवं अल्पसंख्यक कल्याण विभाग द्वारा शैक्षणिक सत्र 2026 के लिए दशमोत्तर छात्रवृत्ति एवं शुल्क प्रतिपूर्ति योजना (UP Post Matric Scholarship 2026) का ऑनलाइन स्टेटस जारी कर दिया गया है।

सस्पेक्ट डाटा सुधार व स्टेटस जांच के महत्वपूर्ण बिंदु:
1. scholarship.up.gov.in पोर्टल पर जाकर 'Postmatric Other than Inter' लॉगिन में अपना रजिस्ट्रेशन नंबर और पासवर्ड दर्ज करें।
2. 'Check Current Status' विकल्प पर क्लिक कर अपना आवेदन स्टेटस देखें।
3. यदि स्टेटस में 'Suspect' अथवा 'Marks Mismatch / Enrollment Number Not Matched' आ रहा है, तो तत्काल संशोधन पोर्टल पर सही विवरण अपलोड करें।
4. संशोधन उपरांत आवेदन पत्र की हार्डकॉपी समस्त संलग्नकों के साथ 7 दिनों के भीतर अपने कॉलेज के स्कॉलरशिप अनुभाग में जमा कराएं।

छात्र अपने बैंक खाते को आधार कार्ड से NPCI मैपिंग अनिवार्य रूप से करवा लें ताकि छात्रवृत्ति की धनराशि सीधे डीबीटी (DBT) के माध्यम से खाते में आ सके।""",
        'official_link': 'https://scholarship.up.gov.in',
        'official_link_label': 'UP स्कॉलरशिप पोर्टल खोलें',
        'author_or_source': 'UP Social Welfare Department',
        'is_breaking': False,
        'is_pinned': False,
        'views_count': 890,
        'published_date': timezone.now(),
    },
    {
        'title': 'Free Winter Industrial Training & Live Project Internship 2026: Polytechnic व B.Tech छात्रों के लिए नए बैच शुरू',
        'category': 'all',
        'badge_text': 'INTERNSHIP 2026',
        'badge_color': 'danger',
        'short_description': 'Python Full-Stack, AI & ML, AutoCAD, SolidWorks, Revit BIM, Circuit Design व PLC Scada में 45 दिन एवं 6 माह की लाइव प्रोजेक्ट इंडस्ट्रियल ट्रेनिंग प्रारंभ।',
        'full_content': """मौर्य टेक्निकल प्राइवेट लिमिटेड (आलमबाग, लखनऊ) द्वारा उत्तर प्रदेश के सभी राजकीय एवं निजी संस्थानों के पॉलिटेक्निक डिप्लोमा एवं बी.टेक इंजीनियरिंग के विद्यार्थियों हेतु विंटर ट्रेनिंग एवं 6-महीने की इंडस्ट्रियल प्रोजेक्ट ट्रेनिंग 2026 के नए बैच प्रारंभ किए गए हैं।

प्रशिक्षण के प्रमुख तकनीकी पाठ्यक्रम:
1. कंप्यूटर साइंस व आईटी: Python Full Stack Development, Django Framework, Machine Learning, AI Applications, React.js.
2. मैकेनिकल इंजीनियरिंग: AutoCAD 2D/3D, SolidWorks 3D Modeling, CATIA, ANSYS FEA Simulation.
3. सिविल इंजीनियरिंग: Building Information Modeling (BIM), Revit Architecture, 3ds Max, STAAD.Pro Structural Analysis.
4. इलेक्ट्रिकल व इलेक्ट्रॉनिक्स: Circuit & PCB Designing, Arduino Microcontroller, IoT Projects, PLC & SCADA Automation.

प्रशिक्षण के लाभ:
• 100% प्रैक्टिकल व लाइव इंडस्ट्री प्रोजेक्ट्स पर कार्य करने का अवसर।
• अनुभवी इंडस्ट्री ट्रेनर्स द्वारा व्यक्तिगत मेंटरशिप।
• सरकारी व निजी नौकरियों में मान्य ISO 9001:2015 प्रमाणित ट्रेनिंग सर्टिफिकेट।
• मौर्य टेक्निकल जॉब फेयर व कैंपस प्लेसमेंट ड्राइव में 100% इंटरव्यू अवसर।""",
        'official_link': 'https://mauryatechnical.in/trainings/',
        'official_link_label': 'ट्रेनिंग कोर्स विवरण देखें व सीट बुक करें',
        'author_or_source': 'Maurya Technical Academic Bureau',
        'is_breaking': True,
        'is_pinned': False,
        'views_count': 1130,
        'published_date': timezone.now(),
    }
]

created_count = 0
for item in news_data:
    obj, created = BreakingNews.objects.get_or_create(
        title=item['title'],
        defaults=item
    )
    if created:
        created_count += 1
        print(f"Created news #{obj.id}: {obj.category}")
    else:
        print(f"Already exists news #{obj.id}: {obj.category}")

print(f"Done! {created_count} breaking news articles populated.")
