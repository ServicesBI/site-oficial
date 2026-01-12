// ================= CARROSSEL ESTRATÉGICO =================
document.addEventListener("DOMContentLoaded", () => {

    const viewport = document.querySelector(".carousel-viewport");
    const track = document.querySelector(".carousel-track");
    const slides = Array.from(document.querySelectorAll(".carousel-slide"));
    const nextBtn = document.querySelector(".carousel-next");
    const prevBtn = document.querySelector(".carousel-prev");
    const dots = Array.from(document.querySelectorAll(".carousel-dots .dot"));
    const carousel = document.querySelector(".strategic-carousel");

    if (!viewport || !track || slides.length === 0) return;

    let currentIndex = 0;
    const totalSlides = slides.length;
    let slideWidth = viewport.offsetWidth;

    /* ================= AUTO PLAY ================= */
    let autoPlayTimer = null;
    const AUTO_PLAY_DELAY = 4500;

    function startAutoPlay() {
        stopAutoPlay();
        autoPlayTimer = setInterval(nextSlide, AUTO_PLAY_DELAY);
    }

    function stopAutoPlay() {
        if (autoPlayTimer) {
            clearInterval(autoPlayTimer);
            autoPlayTimer = null;
        }
    }

    /* ================= SWIPE TOUCH ================= */

let startX = 0;
let startY = 0;
let isSwiping = false;
const SWIPE_THRESHOLD = 50; // px mínimos

viewport.addEventListener("touchstart", (e) => {
    const touch = e.touches[0];
    startX = touch.clientX;
    startY = touch.clientY;
    isSwiping = false;
}, { passive: true });

viewport.addEventListener("touchmove", (e) => {
    if (!e.touches || e.touches.length === 0) return;

    const touch = e.touches[0];
    const deltaX = touch.clientX - startX;
    const deltaY = touch.clientY - startY;

    // Se o movimento vertical for maior, deixa rolar a página
    if (Math.abs(deltaY) > Math.abs(deltaX)) return;

    // Gesto horizontal detectado
    if (Math.abs(deltaX) > 10) {
        isSwiping = true;
        e.preventDefault();
    }
}, { passive: false });

viewport.addEventListener("touchend", (e) => {
    if (!isSwiping) return;

    const endX = e.changedTouches[0].clientX;
    const diffX = endX - startX;

    if (Math.abs(diffX) > SWIPE_THRESHOLD) {
        stopAutoPlay();

        if (diffX < 0) {
            nextSlide();
        } else {
            prevSlide();
        }

        startAutoPlay();
    }

    isSwiping = false;
});


    /* ================= CORE ================= */

    function updateSlideWidth() {
        slideWidth = viewport.offsetWidth;
    }

    function updateTrackPosition(animate = true) {
        track.style.transition = animate ? "transform 0.45s ease" : "none";
        track.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
    }

    function updateDots() {
        dots.forEach((dot, index) => {
            dot.classList.toggle("active", index === currentIndex);
        });
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % totalSlides;
        updateTrackPosition();
        updateDots();
    }

    function prevSlide() {
        currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
        updateTrackPosition();
        updateDots();
    }

    /* ================= CONTROLES ================= */

    if (nextBtn) {
        nextBtn.addEventListener("click", () => {
            stopAutoPlay();
            nextSlide();
            startAutoPlay();
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener("click", () => {
            stopAutoPlay();
            prevSlide();
            startAutoPlay();
        });
    }

    dots.forEach((dot, index) => {
        dot.addEventListener("click", () => {
            stopAutoPlay();
            currentIndex = index;
            updateTrackPosition()
