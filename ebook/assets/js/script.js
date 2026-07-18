// Reveal on scroll
const revealEls = document.querySelectorAll('.reveal');
const io = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
      io.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });
revealEls.forEach(el => io.observe(el));

// FAQ accordion
document.querySelectorAll('.faq-item').forEach(item => {
  const q = item.querySelector('.faq-q');
  q.addEventListener('click', () => {
    const wasOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
    if (!wasOpen) item.classList.add('open');
  });
});

// Prova social slider (drag to scroll)
const proofSlider = document.getElementById('proofSlider');
if (proofSlider) {
  let isDown = false;
  let startX;
  let scrollLeft;
  proofSlider.addEventListener('mousedown', (e) => {
    isDown = true;
    proofSlider.classList.add('dragging');
    startX = e.pageX - proofSlider.offsetLeft;
    scrollLeft = proofSlider.scrollLeft;
  });
  proofSlider.addEventListener('mouseleave', () => {
    isDown = false;
    proofSlider.classList.remove('dragging');
  });
  proofSlider.addEventListener('mouseup', () => {
    isDown = false;
    proofSlider.classList.remove('dragging');
  });
  proofSlider.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - proofSlider.offsetLeft;
    const walk = (x - startX) * 2;
    proofSlider.scrollLeft = scrollLeft - walk;
  });
}

// Prova social lightbox
const proofLightboxImages = [
  '../assets/img/cliente-todo-dia-02.jpg',
  '../assets/img/cliente-todo-dia-01.jpg',
  '../assets/img/ps02-1.png',
  '../assets/img/ps04.png',
  '../assets/img/ps05.png',
  '../assets/img/ps07.png',
  '../assets/img/depoimento-marina-resultado.png'
];
let proofLightboxIndex = 0;

function openProofLightbox(index) {
  proofLightboxIndex = index;
  document.getElementById('proof-lightbox-img').src = proofLightboxImages[proofLightboxIndex];
  document.getElementById('proof-lightbox-overlay').classList.add('open');
}
function closeProofLightbox() {
  document.getElementById('proof-lightbox-overlay').classList.remove('open');
}
function navigateProofLightbox(direction, event) {
  event.stopPropagation();
  proofLightboxIndex = (proofLightboxIndex + direction + proofLightboxImages.length) % proofLightboxImages.length;
  document.getElementById('proof-lightbox-img').src = proofLightboxImages[proofLightboxIndex];
}
