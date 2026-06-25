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

// ============================================================
// RESEARCH UI — POINTER LIGHT, SCROLL PROGRESS, AND 3D CARDS
// ============================================================
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

window.addEventListener('scroll', () => {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const progress = scrollable > 0 ? (window.scrollY / scrollable) * 100 : 0;
    document.documentElement.style.setProperty('--scroll-progress', progress.toFixed(2));
}, { passive: true });

if (!reducedMotion && window.matchMedia('(pointer: fine)').matches) {
    window.addEventListener('pointermove', (event) => {
        document.documentElement.style.setProperty('--pointer-x', `${event.clientX}px`);
        document.documentElement.style.setProperty('--pointer-y', `${event.clientY}px`);
    }, { passive: true });

    document.querySelectorAll('.tilt-card').forEach((card) => {
        card.addEventListener('pointermove', (event) => {
            const rect = card.getBoundingClientRect();
            const x = (event.clientX - rect.left) / rect.width;
            const y = (event.clientY - rect.top) / rect.height;
            const rotateY = (x - 0.5) * 8;
            const rotateX = (0.5 - y) * 7;

            card.style.setProperty('--tilt-x', `${rotateX.toFixed(2)}deg`);
            card.style.setProperty('--tilt-y', `${rotateY.toFixed(2)}deg`);
            card.style.setProperty('--card-x', `${(x * 100).toFixed(1)}%`);
            card.style.setProperty('--card-y', `${(y * 100).toFixed(1)}%`);
        });

        card.addEventListener('pointerleave', () => {
            card.style.setProperty('--tilt-x', '0deg');
            card.style.setProperty('--tilt-y', '0deg');
            card.style.setProperty('--card-x', '50%');
            card.style.setProperty('--card-y', '20%');
        });
    });
}

// ============================================================
// LIVE HERO — ANIMATED NEURAL NETWORK
// ============================================================
const neuralCanvas = document.getElementById('heroNeuralCanvas');

if (neuralCanvas) {
    const context = neuralCanvas.getContext('2d');
    const hero = neuralCanvas.closest('.home-hero');
    const nodes = [];
    const pointer = { x: 0, y: 0, active: false };
    let width = 0;
    let height = 0;
    let animationFrame = null;

    const nodeCount = () => Math.max(28, Math.min(72, Math.floor(width / 24)));

    const createNodes = () => {
        nodes.length = 0;
        for (let index = 0; index < nodeCount(); index++) {
            nodes.push({
                x: Math.random() * width,
                y: Math.random() * height,
                vx: (Math.random() - 0.5) * 0.18,
                vy: (Math.random() - 0.5) * 0.18,
                radius: Math.random() * 1.6 + 0.7,
                phase: Math.random() * Math.PI * 2,
            });
        }
    };

    const resizeNeuralCanvas = () => {
        const rect = hero.getBoundingClientRect();
        const scale = Math.min(window.devicePixelRatio || 1, 1.75);
        width = Math.max(1, rect.width);
        height = Math.max(1, rect.height);
        neuralCanvas.width = Math.floor(width * scale);
        neuralCanvas.height = Math.floor(height * scale);
        neuralCanvas.style.width = `${width}px`;
        neuralCanvas.style.height = `${height}px`;
        context.setTransform(scale, 0, 0, scale, 0, 0);
        createNodes();
    };

    const drawNeuralScene = (time) => {
        context.clearRect(0, 0, width, height);

        nodes.forEach((node) => {
            node.x += node.vx;
            node.y += node.vy;
            if (node.x < -10) node.x = width + 10;
            if (node.x > width + 10) node.x = -10;
            if (node.y < -10) node.y = height + 10;
            if (node.y > height + 10) node.y = -10;
        });

        for (let first = 0; first < nodes.length; first++) {
            const a = nodes[first];
            for (let second = first + 1; second < nodes.length; second++) {
                const b = nodes[second];
                const distance = Math.hypot(a.x - b.x, a.y - b.y);
                if (distance < 135) {
                    const alpha = (1 - distance / 135) * 0.28;
                    const gradient = context.createLinearGradient(a.x, a.y, b.x, b.y);
                    gradient.addColorStop(0, `rgba(96, 165, 250, ${alpha})`);
                    gradient.addColorStop(1, `rgba(103, 232, 249, ${alpha * 0.8})`);
                    context.strokeStyle = gradient;
                    context.lineWidth = 0.7;
                    context.beginPath();
                    context.moveTo(a.x, a.y);
                    context.lineTo(b.x, b.y);
                    context.stroke();
                }
            }

            if (pointer.active) {
                const pointerDistance = Math.hypot(a.x - pointer.x, a.y - pointer.y);
                if (pointerDistance < 190) {
                    context.strokeStyle = `rgba(167, 139, 250, ${(1 - pointerDistance / 190) * 0.34})`;
                    context.beginPath();
                    context.moveTo(a.x, a.y);
                    context.lineTo(pointer.x, pointer.y);
                    context.stroke();
                }
            }
        }

        nodes.forEach((node) => {
            const pulse = 0.65 + Math.sin(time * 0.0015 + node.phase) * 0.35;
            context.fillStyle = `rgba(165, 243, 252, ${0.40 + pulse * 0.42})`;
            context.shadowColor = '#22d3ee';
            context.shadowBlur = 8 * pulse;
            context.beginPath();
            context.arc(node.x, node.y, node.radius + pulse * 0.45, 0, Math.PI * 2);
            context.fill();
        });
        context.shadowBlur = 0;

        animationFrame = requestAnimationFrame(drawNeuralScene);
    };

    hero.addEventListener('pointermove', (event) => {
        const rect = hero.getBoundingClientRect();
        pointer.x = event.clientX - rect.left;
        pointer.y = event.clientY - rect.top;
        pointer.active = true;
    }, { passive: true });

    hero.addEventListener('pointerleave', () => {
        pointer.active = false;
    });

    const resizeObserver = new ResizeObserver(resizeNeuralCanvas);
    resizeObserver.observe(hero);
    resizeNeuralCanvas();

    if (!reducedMotion) {
        animationFrame = requestAnimationFrame(drawNeuralScene);
    } else {
        drawNeuralScene(0);
        if (animationFrame) cancelAnimationFrame(animationFrame);
    }
}
