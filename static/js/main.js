// ============================================================
// SCROLL ANIMATION — Intersection Observer
// ============================================================
document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.08, rootMargin: '0px 0px -40px 0px' }
    );

    // Observe all scroll-animate variants
    document.querySelectorAll(
        '.scroll-animate, .scroll-animate-left, .scroll-animate-right'
    ).forEach((el) => observer.observe(el));

    // Staggered children: observe parent, trigger children in sequence
    document.querySelectorAll('.stagger-children').forEach((parent) => {
        const childObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.querySelectorAll('.scroll-animate').forEach((child, i) => {
                        setTimeout(() => child.classList.add('visible'), i * 80);
                    });
                    childObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.05 });
        childObserver.observe(parent);
    });
});

// ============================================================
// RIPPLE EFFECT on .btn-ripple clicks
// ============================================================
document.addEventListener('click', (e) => {
    const btn = e.target.closest('.btn-ripple');
    if (!btn) return;

    const circle = document.createElement('span');
    const rect   = btn.getBoundingClientRect();
    const size   = Math.max(rect.width, rect.height);
    circle.style.cssText = `
        position:absolute;
        width:${size}px;height:${size}px;
        left:${e.clientX - rect.left - size/2}px;
        top:${e.clientY - rect.top - size/2}px;
        border-radius:50%;
        background:rgba(255,255,255,0.3);
        transform:scale(0);
        animation:ripple-anim 0.55s ease-out forwards;
        pointer-events:none;
    `;
    btn.style.position = btn.style.position || 'relative';
    btn.style.overflow = 'hidden';
    btn.appendChild(circle);
    circle.addEventListener('animationend', () => circle.remove());
});

// Inject ripple keyframe once
if (!document.getElementById('ripple-style')) {
    const s = document.createElement('style');
    s.id = 'ripple-style';
    s.textContent = `@keyframes ripple-anim {
        to { transform: scale(2.5); opacity: 0; }
    }`;
    document.head.appendChild(s);
}

// ============================================================
// SMOOTH COUNTER ANIMATION for .stat-number elements
// ============================================================
function animateCounter(el) {
    const raw   = el.textContent.trim();
    const num   = parseInt(raw.replace(/\D/g, ''), 10);
    if (isNaN(num) || num === 0) return;

    const suffix = raw.replace(/[0-9]/g, '');
    const dur    = 1200;
    const start  = performance.now();

    const tick = (now) => {
        const progress = Math.min((now - start) / dur, 1);
        const eased    = 1 - Math.pow(1 - progress, 3); // ease-out cubic
        el.textContent = Math.floor(eased * num) + suffix;
        if (progress < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
}

const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('.stat-number').forEach((el) => {
    counterObserver.observe(el);
});

// ============================================================
// NAVBAR: highlight active link
// ============================================================
const currentPath = window.location.pathname;
document.querySelectorAll('.nav-link').forEach((link) => {
    if (link.getAttribute('href') === currentPath) {
        link.classList.add('nav-active');
    }
});
