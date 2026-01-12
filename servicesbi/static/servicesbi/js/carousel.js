// ================= CARROSSEL ESTRATÉGICO =================
document.addEventListener("DOMContentLoaded", () => {

    const track = document.querySelector(".carousel-track");
    const slides = document.querySelectorAll(".carousel-slide");
    const nextBtn = document.querySelector(".carousel-next");
    const prevBtn = document.querySelector(".carousel-prev");
    const dots = document.querySelectorAll(".carousel-dots .dot");
    const carousel = document.querySelector(".strategic-carousel");

    if (!track || slides.length === 0) return;

    let currentIndex = 0;
    const totalSlides = slides.length;

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
    /* ================= FIM AUTO PLAY ================= */

    function getSlideOffset() {
        const slide = slides[0];
        const slideRect = slide.getBoundingClientRect();

        const trackStyle = window.getComputedStyle(track);
        const gap = parseFloat(trackStyle.columnGap || trackStyle.gap || 0);

        return slideRect.width + gap;
    }

   function updateTrackPosition() {
    const slide = slides[0];
    const gap = parseInt(getComputedStyle(track).gap) || 0;
    const slideWidth = slide.getBoundingClientRect().width + gap;

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

    // BOTÕES
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

    // DOTS
    dots.forEach((dot, index) => {
        dot.addEventListener("click", () => {
            stopAutoPlay();
            currentIndex = index;
            updateTrackPosition();
            updateDots();
            startAutoPlay();
        });
    });

    // PAUSA NO HOVER
    if (carousel) {
        carousel.addEventListener("mouseenter", stopAutoPlay);
        carousel.addEventListener("mouseleave", startAutoPlay);
    }

    // RESIZE
    window.addEventListener("resize", updateTrackPosition);

    // INIT
    updateTrackPosition();
    updateDots();
    startAutoPlay();
});
