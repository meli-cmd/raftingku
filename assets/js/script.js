// Cache DOM references once — querying on every scroll causes forced reflow
const _navbar     = document.querySelector('.navbar');
const _floatingWA = document.querySelector('.floating-wa');
const _backToTop  = document.querySelector('.back-to-top');

window.addEventListener('scroll', function() {
    const y = window.scrollY;

    if (_navbar) {
        if (y > 50) {
            _navbar.classList.add('scrolled');
        } else {
            _navbar.classList.remove('scrolled');
        }
    }

    if (y > 300) {
        if (_floatingWA) _floatingWA.classList.add('show');
        if (_backToTop)  _backToTop.classList.add('show');
    } else {
        if (_floatingWA) _floatingWA.classList.remove('show');
        if (_backToTop)  _backToTop.classList.remove('show');
    }

    // (no JS parallax needed — handled by background-attachment: fixed in CSS)
}, { passive: true });

document.addEventListener('DOMContentLoaded', function() {
    if (window.AOS) {
        AOS.init({ duration: 800, once: true, offset: 80 });
    } else {
        // Fallback: reveal elements that AOS would have hidden
        document.querySelectorAll('[data-aos]').forEach(el => {
            el.removeAttribute('data-aos');
            el.style.opacity = 1;
        });
    }

    const track = document.querySelector('.marquee-track');
    if (track) {
        const content = track.innerHTML;
        track.innerHTML = content + content;
    }

    if (_backToTop) {
        _backToTop.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Lazy load CTA background
    const ctaSection = document.querySelector('.cta-section');
    if (ctaSection) {
        const bgObserver = new IntersectionObserver(function(entries, observer) {
            if (entries[0].isIntersecting) {
                ctaSection.classList.add('bg-loaded');
                observer.disconnect();
            }
        }, { rootMargin: '300px' });
        bgObserver.observe(ctaSection);
    }
});
