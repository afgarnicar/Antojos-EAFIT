const backBanner = document.querySelector('.back-banner');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
const images = document.querySelectorAll('.back-banner img');

let currentIndex = 1; // Empezamos con la imagen central

function updateCarousel() {
  images.forEach((img, index) => {
    if (index === currentIndex - 1) {
      img.classList.remove('right');
      img.classList.add('left');
    } else if (index === currentIndex) {
      img.classList.remove('left', 'right');
      img.classList.add('center');
    } else if (index === currentIndex + 1) {
      img.classList.remove('left');
      img.classList.add('right');
    } else {
      img.classList.remove('left', 'center', 'right');
    }
  });
}

prevBtn.addEventListener('click', () => {
  currentIndex = (currentIndex - 1 + images.length) % images.length;
  updateCarousel();
});

nextBtn.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % images.length;
  updateCarousel();
});

// Inicializar el carrusel
updateCarousel();



