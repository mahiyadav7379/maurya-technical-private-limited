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
    }

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
});
