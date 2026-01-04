// ================= CARROSSEL ESTRATÉGICO =================

const track = document.querySelector(".carousel-track");
const slides = document.querySelectorAll(".carousel-slide");
const nextBtn = document.querySelector(".carousel-next");
const prevBtn = document.querySelector(".carousel-prev");
const dots = document.querySelectorAll(".carousel-dots .dot");

let currentIndex = 0;
const totalSlides = slides.length;

// ajusta largura do track
function updateTrackPosition() {
    const slideWidth = slides[0].offsetWidth;
    track.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
}

// atualiza dots
function updateDots() {
    dots.forEach((dot, index) => {
        dot.classList.toggle("active", index === currentIndex);
    });
}

// próximo slide
function nextSlide() {
    currentIndex = (currentIndex + 1) % totalSlides;
    updateTrackPosition();
    updateDots();
}

// slide anterior
function prevSlide() {
    currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
    updateTrackPosition();
    updateDots();
}

// eventos
nextBtn.addEventListener("click", nextSlide);
prevBtn.addEventListener("click", prevSlide);

dots.forEach((dot, index) => {
    dot.addEventListener("click", () => {
        currentIndex = index;
        updateTrackPosition();
        updateDots();
    });
});

// ajuste ao redimensionar
window.addEventListener("resize", updateTrackPosition);

// inicialização
updateTrackPosition();
updateDots();
