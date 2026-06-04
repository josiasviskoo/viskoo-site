// Backup do JS do recurso PiP da VSL
const heroVslShell = document.querySelector('.hero-vsl-shell');
const heroVslWrap = document.querySelector('.hero-vsl');
const heroVsl = document.getElementById('heroVsl');
const heroVslPlay = document.querySelector('.hero-vsl-play');
const heroVslToggle = document.querySelector('.hero-vsl-toggle');
let heroVslPlayer = null;
let heroVslReady = false;
let heroVslPendingPlay = false;
let heroVslStarted = false;
let heroVslPlaying = false;
let heroVslInView = true;
let heroVslScrollTicking = false;

function updateHeroVslFloat() {
  if (!heroVslWrap) return;
  const shouldFloat = heroVslStarted && !heroVslInView;
  heroVslWrap.classList.toggle('is-floating', shouldFloat);
  if (heroVslShell) heroVslShell.classList.toggle('is-floating', shouldFloat);
  const heroSection = heroVslWrap.closest('.hero');
  if (heroSection) heroSection.classList.toggle('is-vsl-floating', shouldFloat);
}

function checkHeroVslVisibility() {
  if (!heroVslShell) return;
  const rect = heroVslShell.getBoundingClientRect();
  heroVslInView = rect.bottom > 0 && rect.top < window.innerHeight && rect.height > 0;
  updateHeroVslFloat();
}

function syncHeroVslState(state) {
  if (state === 1 || state === 3) {
    heroVslPlaying = true;
    heroVslStarted = true;
    heroVslPendingPlay = false;
  } else if (state === 0 || state === 2) {
    heroVslPlaying = false;
  }
  if (heroVslPlay) heroVslPlay.classList.toggle('hidden', heroVslStarted);
  if (heroVslToggle) {
    heroVslToggle.classList.toggle('is-paused', !heroVslPlaying);
    heroVslToggle.setAttribute('aria-label', heroVslPlaying ? 'Pausar vídeo' : 'Reproduzir vídeo');
  }
  updateHeroVslFloat();
}

function playHeroVsl() {
  heroVslPendingPlay = true;
  heroVslStarted = true;
  heroVslPlaying = true;
  if (heroVslPlay) heroVslPlay.classList.toggle('hidden', heroVslStarted);
  if (heroVslToggle) {
    heroVslToggle.classList.toggle('is-paused', false);
    heroVslToggle.setAttribute('aria-label', 'Pausar vídeo');
  }

  if (heroVslReady && heroVslPlayer && heroVslPlayer.playVideo) {
    heroVslPlayer.playVideo();
    heroVslPendingPlay = false;
  }

  updateHeroVslFloat();
}

function pauseHeroVsl() {
  heroVslPendingPlay = false;
  if (heroVslReady && heroVslPlayer && heroVslPlayer.pauseVideo) {
    heroVslPlayer.pauseVideo();
  }
  heroVslPlaying = false;
  if (heroVslToggle) {
    heroVslToggle.classList.toggle('is-paused', true);
    heroVslToggle.setAttribute('aria-label', 'Reproduzir vídeo');
  }
  updateHeroVslFloat();
}

window.onYouTubeIframeAPIReady = function() {
  if (!heroVsl) return;
  heroVslPlayer = new YT.Player('heroVsl', {
    events: {
      onReady: () => {
        heroVslReady = true;
        if (heroVslPendingPlay) playHeroVsl();
      },
      onStateChange: (event) => syncHeroVslState(event.data)
    }
  });
};

if (heroVsl) {
  const ytApi = document.createElement('script');
  ytApi.src = 'https://www.youtube.com/iframe_api';
  document.head.appendChild(ytApi);
}

if (heroVsl && heroVslPlay) {
  heroVslPlay.addEventListener('click', () => {
    playHeroVsl();
  });
}

if (heroVslToggle) {
  heroVslToggle.addEventListener('click', () => {
    if (!heroVslWrap.classList.contains('is-floating')) return;
    if (heroVslPlaying) {
      pauseHeroVsl();
    } else {
      playHeroVsl();
    }
  });
}

if (heroVslShell) {
  const heroVslObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      heroVslInView = entry.isIntersecting && entry.intersectionRatio >= 0.2;
      updateHeroVslFloat();
    });
  }, { threshold: [0, 0.2] });
  heroVslObserver.observe(heroVslShell);
  window.addEventListener('scroll', () => {
    if (heroVslScrollTicking) return;
    heroVslScrollTicking = true;
    requestAnimationFrame(() => {
      checkHeroVslVisibility();
      heroVslScrollTicking = false;
    });
  }, { passive: true });
  window.addEventListener('resize', checkHeroVslVisibility);
  checkHeroVslVisibility();
}
