import re

with open("public_html/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update text "Empresas que já aplicam..."
html = html.replace('Empresas que já aplicam o método', 'Muitos clientes já entenderam que é estrutura')

# 2. Fix the Process section (Move conference image) and Add Dashboard Section
old_process = """<!-- BLOCO DE AUTORIDADE / PROCESSO -->
<section class="section">
  <div class="container">
    <div class="section-header text-center reveal">
      <p class="section-label">Acompanhamento</p>
      <h2 class="section-title">Como funciona a estrutura</h2>
      <p class="section-desc" style="margin: 0 auto;">Processo focado em dados, decisões e crescimento contínuo.</p>
    </div>
    <div class="grid grid-3 reveal">
      <div class="card card-body">
        <div class="icon-wrap mb-4">
          <svg class="icon icon-md" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
        </div>
        <h3 class="t-h3 mb-2">30 dias</h3>
        <p class="t-sm t-secondary">Plano de ação inicial entregue com clareza de prioridades.</p>
      </div>
      <div class="card card-body card-accent">
        <div class="icon-wrap mb-4" style="background: var(--accent-dim); color: var(--accent);">
          <svg class="icon icon-md" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
        </div>
        <h3 class="t-h3 mb-2">1 hora semanal</h3>
        <p class="t-sm t-secondary mb-4">Reunião estratégica focada em dados, decisões e próximos passos.</p>
        <img src="assets/img/imagem-video-conferencia.png" alt="Call com Cliente" style="width: 100%; border-radius: var(--r-md); border: 1px solid rgba(244,131,34,0.3);">
      </div>
      <div class="card card-body">
        <div class="icon-wrap mb-4">
          <svg class="icon icon-md" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
        </div>
        <h3 class="t-h3 mb-2">Rotina contínua</h3>
        <p class="t-sm t-secondary">Execução organizada com priorização do que realmente gera crescimento.</p>
      </div>
    </div>
  </div>
</section>"""

new_process = """<!-- BLOCO DE AUTORIDADE / PROCESSO -->
<section class="section">
  <div class="container">
    <div class="section-header text-center reveal">
      <p class="section-label">Acompanhamento</p>
      <h2 class="section-title">Como funciona a estrutura</h2>
      <p class="section-desc" style="margin: 0 auto;">Processo focado em dados, decisões e crescimento contínuo.</p>
    </div>
    <div class="grid grid-2 reveal" style="gap: var(--space-8); align-items: center;">
      <div class="flex flex-col gap-4">
        <div class="card card-body">
          <div class="icon-wrap mb-4">
            <svg class="icon icon-md" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          </div>
          <h3 class="t-h3 mb-2">30 dias</h3>
          <p class="t-sm t-secondary">Plano de ação inicial entregue com clareza de prioridades.</p>
        </div>
        <div class="card card-body card-accent">
          <div class="icon-wrap mb-4" style="background: var(--accent-dim); color: var(--accent);">
            <svg class="icon icon-md" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          </div>
          <h3 class="t-h3 mb-2">1 hora semanal</h3>
          <p class="t-sm t-secondary">Reunião estratégica focada em dados, decisões e próximos passos.</p>
        </div>
        <div class="card card-body">
          <div class="icon-wrap mb-4">
            <svg class="icon icon-md" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
          </div>
          <h3 class="t-h3 mb-2">Rotina contínua</h3>
          <p class="t-sm t-secondary">Execução organizada com priorização do que realmente gera crescimento.</p>
        </div>
      </div>
      <div>
        <img src="assets/img/imagem-video-conferencia.png" alt="Call com Cliente" class="w-full zoom-hover-sm" style="border-radius: var(--r-xl); border: 1px solid var(--border); box-shadow: var(--shadow-lg);">
      </div>
    </div>
  </div>
</section>

<!-- BLOCO DE DASHBOARD -->
<section class="section" style="background: var(--bg-surface);">
  <div class="container">
    <div class="grid grid-2 reveal" style="align-items: center; gap: var(--space-8);">
      <div style="order: 2;">
        <h2 class="t-h2 mb-4">Visibilidade total da sua operação</h2>
        <p class="t-body t-secondary mb-6">Pare de tomar decisões no escuro. Acompanhamos cada métrica importante para o seu negócio através de uma dashboard exclusiva.</p>
        <ul class="flex flex-col gap-3 t-sm t-secondary" style="list-style: none;">
          <li class="flex items-center gap-2"><svg class="icon icon-sm" style="color: var(--accent);" viewBox="0 0 20 20" fill="currentColor"><circle cx="10" cy="10" r="5"/></svg> Acompanhamento em tempo real</li>
          <li class="flex items-center gap-2"><svg class="icon icon-sm" style="color: var(--accent);" viewBox="0 0 20 20" fill="currentColor"><circle cx="10" cy="10" r="5"/></svg> Clareza sobre o custo por cliente</li>
          <li class="flex items-center gap-2"><svg class="icon icon-sm" style="color: var(--accent);" viewBox="0 0 20 20" fill="currentColor"><circle cx="10" cy="10" r="5"/></svg> Decisões focadas no que funciona</li>
        </ul>
      </div>
      <div style="order: 1;">
        <img src="assets/img/dashboard-viskoo-1024x433.png" alt="Dashboard Viskoo" class="w-full zoom-hover-sm" style="border-radius: var(--r-xl); border: 1px solid var(--border); box-shadow: var(--shadow-lg);">
      </div>
    </div>
  </div>
</section>"""

html = html.replace(old_process, new_process)
# Adjust Dor / identificação background to differentiate from dashboard
html = html.replace('<!-- BLOCO DE DOR / IDENTIFICAÇÃO -->\n<section class="section" style="background: var(--bg-surface);">', '<!-- BLOCO DE DOR / IDENTIFICAÇÃO -->\n<section class="section">')


# 3. O que não é less modest
old_not = """      <div class="card card-body" style="border-top: 3px solid #ff453a;">
        <h3 class="t-h4 mb-2 flex items-center gap-2"><span style="color:#ff453a;">✕</span> Não é milagre</h3>
        <p class="t-sm t-secondary">Nenhuma agência cria resultado sozinha sem organização da empresa.</p>
      </div>
      <div class="card card-body" style="border-top: 3px solid #ff453a;">
        <h3 class="t-h4 mb-2 flex items-center gap-2"><span style="color:#ff453a;">✕</span> Não é volume</h3>
        <p class="t-sm t-secondary">O foco não é quantidade de posts, reuniões ou entregas soltas sem propósito.</p>
      </div>
      <div class="card card-body" style="border-top: 3px solid #ff453a;">
        <h3 class="t-h4 mb-2 flex items-center gap-2"><span style="color:#ff453a;">✕</span> Não é improviso</h3>
        <p class="t-sm t-secondary">Cada ação precisa ter função estratégica bem definida antes de ser executada.</p>
      </div>"""
      
new_not = """      <div class="card card-body" style="background: rgba(255,69,58,0.05); border: 1px solid rgba(255,69,58,0.3); padding: var(--space-6);">
        <h3 class="t-h3 mb-3 flex items-center gap-2"><span style="color:#ff453a; font-size: 24px;">✕</span> Não é milagre</h3>
        <p class="t-body" style="color: rgba(240,240,240,0.8);">Nenhuma agência cria resultado sozinha sem organização da empresa.</p>
      </div>
      <div class="card card-body" style="background: rgba(255,69,58,0.05); border: 1px solid rgba(255,69,58,0.3); padding: var(--space-6);">
        <h3 class="t-h3 mb-3 flex items-center gap-2"><span style="color:#ff453a; font-size: 24px;">✕</span> Não é volume</h3>
        <p class="t-body" style="color: rgba(240,240,240,0.8);">O foco não é quantidade de posts, reuniões ou entregas soltas sem propósito.</p>
      </div>
      <div class="card card-body" style="background: rgba(255,69,58,0.05); border: 1px solid rgba(255,69,58,0.3); padding: var(--space-6);">
        <h3 class="t-h3 mb-3 flex items-center gap-2"><span style="color:#ff453a; font-size: 24px;">✕</span> Não é improviso</h3>
        <p class="t-body" style="color: rgba(240,240,240,0.8);">Cada ação precisa ter função estratégica bem definida antes de ser executada.</p>
      </div>"""
html = html.replace(old_not, new_not)

# "O que é" bigger too
old_is = """      <div class="card card-body card-accent">
        <h3 class="t-h4 mb-2 flex items-center gap-2"><span style="color: #30d158;">✓</span> É estrutura</h3>
        <p class="t-sm t-secondary">Organização metódica e validada antes da escala.</p>
      </div>
      <div class="card card-body card-accent">
        <h3 class="t-h4 mb-2 flex items-center gap-2"><span style="color: #30d158;">✓</span> É clareza</h3>
        <p class="t-sm t-secondary">Entender o que fazer, por que fazer e o que medir.</p>
      </div>
      <div class="card card-body card-accent">
        <h3 class="t-h4 mb-2 flex items-center gap-2"><span style="color: #30d158;">✓</span> É previsibilidade</h3>
        <p class="t-sm t-secondary">Transformar marketing em um processo lucrativo.</p>
      </div>"""
new_is = """      <div class="card card-body card-accent" style="padding: var(--space-6);">
        <h3 class="t-h3 mb-3 flex items-center gap-2"><span style="color: #30d158; font-size: 24px;">✓</span> É estrutura</h3>
        <p class="t-body" style="color: rgba(240,240,240,0.8);">Organização metódica e validada antes da escala.</p>
      </div>
      <div class="card card-body card-accent" style="padding: var(--space-6);">
        <h3 class="t-h3 mb-3 flex items-center gap-2"><span style="color: #30d158; font-size: 24px;">✓</span> É clareza</h3>
        <p class="t-body" style="color: rgba(240,240,240,0.8);">Entender o que fazer, por que fazer e o que medir.</p>
      </div>
      <div class="card card-body card-accent" style="padding: var(--space-6);">
        <h3 class="t-h3 mb-3 flex items-center gap-2"><span style="color: #30d158; font-size: 24px;">✓</span> É previsibilidade</h3>
        <p class="t-body" style="color: rgba(240,240,240,0.8);">Transformar marketing em um processo lucrativo.</p>
      </div>"""
html = html.replace(old_is, new_is)


# 4. Carousel Fix
old_slider = '<div class="slider-track" style="padding-bottom: var(--space-4);">'
new_slider = '<div class="slider-track" id="testimonialSlider" style="padding-bottom: var(--space-4); cursor: grab; display: flex; overflow-x: auto; scroll-behavior: smooth;">'
html = html.replace(old_slider, new_slider)

# Adding cursor pointer and onclick to slides
html = re.sub(r'(<img src="assets/img/[^"]+" alt="[^"]+" class="w-full" style="border-radius: var\(--r-xl\); object-fit: cover; aspect-ratio: 1;)">', 
              r'\1 cursor: pointer;" onclick="openLightbox(this.src)">', html)

# Script and lightbox HTML
script_to_add = """  // Lightbox functionality
  function openLightbox(src) {
    document.getElementById('lightbox-img').src = src;
    document.getElementById('lightbox-overlay').classList.add('open');
  }
  function closeLightbox() {
    document.getElementById('lightbox-overlay').classList.remove('open');
  }
  
  // Slider drag functionality
  const slider = document.getElementById('testimonialSlider');
  let isDown = false;
  let startX;
  let scrollLeft;
  
  if(slider) {
    slider.addEventListener('mousedown', (e) => {
      isDown = true;
      slider.style.cursor = 'grabbing';
      startX = e.pageX - slider.offsetLeft;
      scrollLeft = slider.scrollLeft;
    });
    slider.addEventListener('mouseleave', () => {
      isDown = false;
      slider.style.cursor = 'grab';
    });
    slider.addEventListener('mouseup', () => {
      isDown = false;
      slider.style.cursor = 'grab';
    });
    slider.addEventListener('mousemove', (e) => {
      if (!isDown) return;
      e.preventDefault();
      const x = e.pageX - slider.offsetLeft;
      const walk = (x - startX) * 2;
      slider.scrollLeft = scrollLeft - walk;
    });
  }
</script>

<!-- Lightbox Overlay -->
<div id="lightbox-overlay" class="modal-overlay" onclick="closeLightbox()" style="position: fixed; inset: 0; background: rgba(0,0,0,0.85); z-index: 9999; display: flex; align-items: center; justify-content: center; opacity: 0; pointer-events: none; transition: opacity 0.3s ease;">
  <div style="position: relative; max-width: 90vw; max-height: 90vh;">
    <button onclick="closeLightbox()" style="position: absolute; top: -40px; right: 0; background: transparent; border: none; color: #fff; font-size: 30px; cursor: pointer;">&times;</button>
    <img id="lightbox-img" src="" style="max-width: 100%; max-height: 90vh; border-radius: var(--r-md); object-fit: contain;">
  </div>
</div>"""

html = html.replace('</script>', script_to_add)


# 5. Remove border from Josias photo
html = html.replace('max-width: 440px; border-radius: var(--r-xl); border: 1px solid var(--border); box-shadow: var(--shadow-lg);', 'max-width: 440px;')

# 6. Remove price 10x...
price_block = """        <div class="mb-5">
          <p class="t-h3 t-accent">10x de R$11,66 <span class="t-body t-secondary">ou R$97 à vista</span></p>
        </div>"""
html = html.replace(price_block, "")


with open("public_html/index.html", "w", encoding="utf-8") as f:
    f.write(html)
