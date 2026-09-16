/* Maurya Technical JavaScript & Framer Motion Animations with Gallery Lightbox Slideshow */
document.addEventListener('DOMContentLoaded', function() {
    console.log("Maurya Technical Framer Motion Animations & Gallery Lightbox Initialized.");

    // Initialize AOS (Animate On Scroll) with spring physics easing
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            once: true,
            easing: 'ease-out-back',
            offset: 80
        });
    } else {
        // Fallback: If AOS library fails to load, ensure elements are visible
        document.querySelectorAll('[data-aos]').forEach(function(el) {
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
    }

    // Safety timeout: ensure no element remains invisible
    setTimeout(function() {
        document.querySelectorAll('[data-aos]').forEach(function(el) {
            if (window.getComputedStyle(el).opacity === '0') {
                el.classList.add('aos-animate');
                el.style.opacity = '1';
            }
        });
    }, 1000);

    // Back to top smooth scroll
    const backToTopBtn = document.getElementById('backToTopBtn');
    if (backToTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTopBtn.style.display = 'flex';
            } else {
                backToTopBtn.style.display = 'none';
            }
        });

        backToTopBtn.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // --- DEDICATED GALLERY LIGHTBOX SLIDESHOW ---
    const lightboxModal = document.getElementById('galleryLightboxModal');
    const lightboxImage = document.getElementById('lightboxImage');
    const lightboxTitle = document.getElementById('lightboxTitle');
    const lightboxCounter = document.getElementById('lightboxCounter');
    const prevBtn = document.getElementById('lightboxPrevBtn');
    const nextBtn = document.getElementById('lightboxNextBtn');

    let currentGalleryIndex = 0;
    let galleryList = [];

    function updateLightbox(index) {
        if (galleryList.length === 0) return;
        if (index < 0) index = galleryList.length - 1;
        if (index >= galleryList.length) index = 0;

        currentGalleryIndex = index;
        const item = galleryList[currentGalleryIndex];

        lightboxImage.style.opacity = '0';
        setTimeout(function() {
            lightboxImage.setAttribute('src', item.src);
            if (lightboxTitle) lightboxTitle.innerHTML = `<i class="fas fa-images me-2"></i> ${item.title}`;
            if (lightboxCounter) lightboxCounter.textContent = `Photo ${currentGalleryIndex + 1} of ${galleryList.length}`;
            lightboxImage.style.opacity = '1';
        }, 150);
    }

    function initGalleryLightbox() {
        const galleryItems = document.querySelectorAll('.gallery-lightbox-item, .batch-card img, .card-img-top');
        galleryList = [];

        galleryItems.forEach(function(img, idx) {
            img.style.cursor = 'pointer';
            const src = img.getAttribute('src');
            const title = img.getAttribute('alt') || img.getAttribute('data-caption') || 'Maurya Technical Event Photo';
            galleryList.push({ src: src, title: title });

            img.addEventListener('click', function() {
                if (lightboxModal && lightboxImage) {
                    const modalInstance = bootstrap.Modal.getOrCreateInstance(lightboxModal);
                    updateLightbox(idx);
                    modalInstance.show();
                }
            });
        });

        if (prevBtn) {
            prevBtn.addEventListener('click', function() {
                updateLightbox(currentGalleryIndex - 1);
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', function() {
                updateLightbox(currentGalleryIndex + 1);
            });
        }

        // Keyboard Arrow Key Navigation
        document.addEventListener('keydown', function(e) {
            if (lightboxModal && lightboxModal.classList.contains('show')) {
                if (e.key === 'ArrowLeft') {
                    updateLightbox(currentGalleryIndex - 1);
                } else if (e.key === 'ArrowRight') {
                    updateLightbox(currentGalleryIndex + 1);
                }
            }
        });
    }

    initGalleryLightbox();

    // Navbar Scroll Shadow effect
    const navbar = document.querySelector('.main-navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('shadow-md');
                navbar.style.padding = '8px 0';
            } else {
                navbar.classList.remove('shadow-md');
                navbar.style.padding = '12px 0';
            }
        });
    }

    // Design Solutions Accordion Expanded State Sync
    const designAccordion = document.getElementById('designSolutionsAccordion');
    if (designAccordion) {
        designAccordion.addEventListener('show.bs.collapse', function(e) {
            const item = e.target.closest('.accordion-item');
            if (item) item.classList.add('is-expanded');
        });

        designAccordion.addEventListener('hide.bs.collapse', function(e) {
            const item = e.target.closest('.accordion-item');
            if (item) item.classList.remove('is-expanded');
        });
    }

    // --- MAURYA TECHNICAL OFFICIAL LIVE CHATBOT CONTROLLER ---
    const chatLauncher = document.getElementById('mauryaChatLauncher');
    const chatWindow = document.getElementById('mauryaChatWindow');
    const chatCloseBtn = document.getElementById('chatCloseBtn');
    const chatMinimizeBtn = document.getElementById('chatMinimizeBtn');
    const chatMessagesArea = document.getElementById('chatMessagesArea');
    const chatInputForm = document.getElementById('chatInputForm');
    const chatInputField = document.getElementById('chatInputField');
    const chatUnreadBadge = document.querySelector('.chat-unread-badge');
    const externalLiveChatBtn = document.getElementById('liveChatBtn');

    function toggleChatbot(forceOpen) {
        if (!chatWindow) return;
        const isHidden = chatWindow.classList.contains('d-none');
        const shouldOpen = forceOpen !== undefined ? forceOpen : isHidden;

        if (shouldOpen) {
            chatWindow.classList.remove('d-none');
            chatWindow.classList.add('chat-window-open');
            if (chatUnreadBadge) chatUnreadBadge.style.display = 'none';
            if (chatLauncher) {
                chatLauncher.querySelector('.chat-icon-open')?.classList.add('d-none');
                chatLauncher.querySelector('.chat-icon-close')?.classList.remove('d-none');
            }
            setTimeout(() => {
                chatInputField?.focus();
                scrollChatToBottom();
            }, 200);
        } else {
            chatWindow.classList.add('d-none');
            chatWindow.classList.remove('chat-window-open');
            if (chatLauncher) {
                chatLauncher.querySelector('.chat-icon-open')?.classList.remove('d-none');
                chatLauncher.querySelector('.chat-icon-close')?.classList.add('d-none');
            }
        }
    }

    if (chatLauncher) chatLauncher.addEventListener('click', () => toggleChatbot());
    if (chatCloseBtn) chatCloseBtn.addEventListener('click', () => toggleChatbot(false));
    if (chatMinimizeBtn) chatMinimizeBtn.addEventListener('click', () => toggleChatbot(false));
    if (externalLiveChatBtn) {
        externalLiveChatBtn.addEventListener('click', function(e) {
            e.preventDefault();
            toggleChatbot(true);
        });
    }

    function scrollChatToBottom() {
        if (chatMessagesArea) {
            chatMessagesArea.scrollTop = chatMessagesArea.scrollHeight;
        }
    }

    function appendUserMessage(text) {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'chat-msg user-msg';
        msgDiv.innerHTML = `
            <div class="chat-msg-bubble">
                <p class="mb-0">${escapeHtml(text)}</p>
            </div>
            <span class="chat-timestamp">Just now</span>
        `;
        chatMessagesArea.appendChild(msgDiv);
        scrollChatToBottom();
    }

    function appendBotMessage(htmlContent) {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'chat-msg bot-msg';
        msgDiv.innerHTML = `
            <div class="chat-msg-bubble">
                ${htmlContent}
            </div>
            <span class="chat-timestamp">Just now</span>
        `;
        chatMessagesArea.appendChild(msgDiv);
        scrollChatToBottom();
    }

    function escapeHtml(string) {
        const div = document.createElement('div');
        div.innerText = string;
        return div.innerHTML;
    }

    // Knowledge base automated responses
    const botAnswers = {
        fees: `
            <p class="fw-bold mb-1 text-danger"><i class="fas fa-tags me-1"></i> Industrial Training Fees 2026:</p>
            <ul class="list-unstyled small mb-2">
                <li>• <strong>45 Days / 6 Weeks:</strong> ₹4,000 (Vocational)</li>
                <li>• <strong>06 Months:</strong> ₹18,000 (Internship + Job Track)</li>
            </ul>
            <p class="small mb-2 text-muted">Includes Major Live Projects & MSME Government Registered Certificate with QR Verification.</p>
            <div class="d-flex gap-2 flex-wrap">
                <a href="/fees/" class="btn btn-sm btn-danger fw-bold"><i class="fas fa-external-link-alt me-1"></i> View Full Fee Table</a>
                <a href="/registration/" class="btn btn-sm btn-warning fw-bold text-dark"><i class="fas fa-edit me-1"></i> Register</a>
            </div>
        `,
        courses: `
            <p class="fw-bold mb-1 text-danger"><i class="fas fa-graduation-cap me-1"></i> 7 Major Training Solutions:</p>
            <ol class="small ps-3 mb-2 text-dark">
                <li><strong>Web Design:</strong> Python, Django, HTML/CSS/JS, Bootstrap</li>
                <li><strong>Machine Design:</strong> SolidWorks, AutoCAD, CATIA</li>
                <li><strong>Circuit Design:</strong> PCB, Arduino, Proteus, Embedded</li>
                <li><strong>Building Design:</strong> Revit, SketchUp, 2D/3D BIM</li>
                <li><strong>Interior & Fashion Design:</strong> 3ds Max, CAD</li>
            </ol>
            <a href="/trainings/" class="btn btn-sm btn-danger fw-bold"><i class="fas fa-book-open me-1"></i> Explore All 19 Courses</a>
        `,
        register: `
            <p class="fw-bold mb-1 text-danger"><i class="fas fa-edit me-1"></i> Admission & Registration Process:</p>
            <p class="small mb-2 text-muted">Seat booking open for AKTU / BTEUP Summer & Winter Vocational batches 2026. Online registration requires just 2 minutes:</p>
            <div class="d-flex gap-2 flex-wrap">
                <a href="/registration/" class="btn btn-sm btn-warning fw-bold text-dark"><i class="fas fa-user-plus me-1"></i> Online Registration Form</a>
                <a href="https://wa.me/918887839689?text=Hello%20Maurya%20Technical,%20I%20want%20to%20register%20for%20training" target="_blank" class="btn btn-sm btn-success fw-bold"><i class="fab fa-whatsapp me-1"></i> WhatsApp Desk</a>
            </div>
        `,
        placements: `
            <p class="fw-bold mb-1 text-success"><i class="fas fa-award me-1"></i> 100% Placement & Job Fair:</p>
            <p class="small mb-2 text-muted">Recent placements: Annu Singh (Vartax Global), Kanti Pal (NIVRAJ), Saloni Katara. Mega Job Fair 2026 drives organized with senior HR panel!</p>
            <div class="d-flex gap-2 flex-wrap">
                <a href="/placements/" class="btn btn-sm btn-outline-danger fw-bold">Placed Students</a>
                <a href="/job-fair/" class="btn btn-sm btn-danger fw-bold">Job Fair 2026</a>
            </div>
        `,
        whatsapp: `
            <p class="fw-bold mb-1 text-success"><i class="fab fa-whatsapp me-1"></i> Direct WhatsApp Desks:</p>
            <p class="small mb-2 text-muted">You can chat directly with our technical counselors on WhatsApp:</p>
            <div class="d-grid gap-2">
                <a href="https://wa.me/918887839689?text=Hello%20Maurya%20Technical,%20I%20need%20training%20counseling" target="_blank" class="btn btn-sm btn-success fw-bold text-start"><i class="fab fa-whatsapp me-2"></i> Director Desk (+91 88878 39689)</a>
                <a href="https://wa.me/918858298247?text=Hello%20HR%20Desk%20/%20Maurya%20Technical,%20I%20need%20admission%20details" target="_blank" class="btn btn-sm btn-outline-success fw-bold text-start"><i class="fab fa-whatsapp me-2"></i> HR Kirti Kushwaha (+91 88582 98247)</a>
            </div>
        `,
        location: `
            <p class="fw-bold mb-1 text-danger"><i class="fas fa-map-marker-alt me-1"></i> Head Office & Campus Location:</p>
            <p class="small mb-2 text-dark"><strong>Maurya Technical Private Limited</strong><br>Alambagh, Lucknow, Uttar Pradesh, India.<br>Helpline: <a href="tel:+918887839689">+91 88878 39689</a></p>
            <a href="/contact/" class="btn btn-sm btn-outline-danger fw-bold">View Location Map</a>
        `
    };

    // Quick Chips delegation
    const quickChips = document.getElementById('chatQuickChips');
    if (quickChips) {
        quickChips.addEventListener('click', function(e) {
            const btn = e.target.closest('.quick-chip-btn');
            if (!btn) return;
            const query = btn.getAttribute('data-query');
            const chipText = btn.innerText.trim();

            appendUserMessage(chipText);

            setTimeout(() => {
                if (botAnswers[query]) {
                    appendBotMessage(botAnswers[query]);
                } else {
                    handleTextQuery(chipText);
                }
            }, 350);
        });
    }

    function handleTextQuery(query) {
        const q = query.toLowerCase().trim();
        let reply = '';

        if (q.includes('fee') || q.includes('cost') || q.includes('charge') || q.includes('price') || q.includes('paisa') || q.includes('kitna')) {
            reply = botAnswers.fees;
        } else if (q.includes('course') || q.includes('python') || q.includes('cad') || q.includes('web') || q.includes('syllabus') || q.includes('subject') || q.includes('design')) {
            reply = botAnswers.courses;
        } else if (q.includes('regis') || q.includes('admission') || q.includes('join') || q.includes('apply') || q.includes('seat')) {
            reply = botAnswers.register;
        } else if (q.includes('place') || q.includes('job') || q.includes('salary') || q.includes('package') || q.includes('hiring')) {
            reply = botAnswers.placements;
        } else if (q.includes('address') || q.includes('location') || q.includes('office') || q.includes('kahan') || q.includes('kaha') || q.includes('lucknow')) {
            reply = botAnswers.location;
        } else if (q.includes('contact') || q.includes('phone') || q.includes('call') || q.includes('number') || q.includes('whatsapp')) {
            reply = botAnswers.whatsapp;
        } else {
            const encodedQuery = encodeURIComponent('Hello Maurya Technical, My Question: ' + query);
            reply = `
                <p class="mb-2">For your query, you can get direct live guidance from our training counselor on WhatsApp:</p>
                <a href="https://wa.me/918887839689?text=${encodedQuery}" target="_blank" class="btn btn-sm btn-success fw-bold d-inline-flex align-items-center gap-1">
                    <i class="fab fa-whatsapp"></i> Ask on WhatsApp (+91 88878 39689)
                </a>
            `;
        }

        setTimeout(() => {
            appendBotMessage(reply);
        }, 400);
    }

    if (chatInputForm) {
        chatInputForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const text = chatInputField.value.trim();
            if (!text) return;
            appendUserMessage(text);
            chatInputField.value = '';
            handleTextQuery(text);
        });
    }
});
