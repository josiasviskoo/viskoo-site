import re

with open("public_html/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Hero text readability
# Change from <p class="hero-sub t-sm t-muted" to <p class="hero-sub t-body t-secondary"
html = html.replace('class="hero-sub t-sm t-muted"', 'class="hero-sub t-body t-secondary"')

# 2. "Muitos clientes..." text update
html = html.replace('Muitos clientes já entenderam que é estrutura', 'Muitos clientes já entenderam que estrutura bem feita é o que vende')

# 3. Dashboard layout
# Current:
# <div class="grid grid-2 reveal" style="align-items: center; gap: var(--space-8);">
#   <div style="order: 2;">
#     <h2 class="t-h2 mb-4">Visibilidade total da sua operação</h2>
#     <p class="t-body t-secondary mb-6">Pare de tomar decisões no escuro. Acompanhamos cada métrica importante para o seu negócio através de uma dashboard exclusiva.</p>
# ...
#   </div>
#   <div style="order: 1;">
#     <img src="assets/img/dashboard-viskoo-1024x433.png" alt="Dashboard Viskoo" class="w-full zoom-hover-sm" style="border-radius: var(--r-xl); border: 1px solid var(--border); box-shadow: var(--shadow-lg);">
#   </div>
# </div>

old_dash = """<section class="section" style="background: var(--bg-surface);">
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

new_dash = """<section class="section" style="background: var(--bg-surface);">
  <div class="container">
    <div class="reveal text-center mb-6">
      <h2 class="t-h2 mb-4">Visibilidade total da sua operação</h2>
      <p class="t-body t-secondary mb-6" style="max-width: 800px; margin-inline: auto;">Pare de tomar decisões no escuro. Acompanhamos cada métrica importante para o seu negócio através de uma dashboard exclusiva.</p>
      <ul class="flex gap-4 justify-center t-body t-secondary" style="list-style: none; flex-wrap: wrap;">
        <li class="flex items-center gap-2"><svg class="icon icon-sm" style="color: var(--accent);" viewBox="0 0 20 20" fill="currentColor"><circle cx="10" cy="10" r="5"/></svg> Acompanhamento em tempo real</li>
        <li class="flex items-center gap-2"><svg class="icon icon-sm" style="color: var(--accent);" viewBox="0 0 20 20" fill="currentColor"><circle cx="10" cy="10" r="5"/></svg> Clareza sobre o custo por cliente</li>
        <li class="flex items-center gap-2"><svg class="icon icon-sm" style="color: var(--accent);" viewBox="0 0 20 20" fill="currentColor"><circle cx="10" cy="10" r="5"/></svg> Decisões focadas no que funciona</li>
      </ul>
    </div>
    <div class="reveal">
      <img src="assets/img/dashboard-viskoo-1024x433.png" alt="Dashboard Viskoo" class="w-full" style="border-radius: var(--r-xl); border: 1px solid var(--border); box-shadow: var(--shadow-lg);">
    </div>
  </div>
</section>"""
html = html.replace(old_dash, new_dash)

# 4. text size of "Você não sabe exatamente..." in <div class="flex flex-col gap-3 mb-6">
# Change all <span class="t-sm"> inside these feature-items to <span class="t-body">
html = html.replace('<span class="t-sm">Você não sabe exatamente', '<span class="t-body">Você não sabe exatamente')
html = html.replace('<span class="t-sm">Já investiu em marketing', '<span class="t-body">Já investiu em marketing')
html = html.replace('<span class="t-sm">Recebe relatórios,', '<span class="t-body">Recebe relatórios,')
html = html.replace('<span class="t-sm">Depende de indicação', '<span class="t-body">Depende de indicação')
html = html.replace('<span class="t-sm">Não sabe onde cortar', '<span class="t-body">Não sabe onde cortar')
html = html.replace('<span class="t-sm">Executa várias ações', '<span class="t-body">Executa várias ações')

# 5. Clarify service vs method
old_apply = """<h2 class="t-h2 mb-4">OPlanoÚnico™ aplicado na sua empresa</h2>
        <p class="t-body t-secondary mb-4">Aqui o plano deixa de ser conceito e passa a ser execução. Eu aplico OPlanoÚnico™ junto com a empresa, organizando:</p>"""
new_apply = """<h2 class="t-h2 mb-4">OPlanoÚnico™ aplicado com a Mão na Massa</h2>
        <p class="t-body t-secondary mb-4">Não somos apenas um curso ou uma mentoria. Nós somos a <strong>mão de obra</strong>. A Viskoo atua prestando um serviço focado em execução ao seu lado. Aqui o plano deixa de ser conceito e passa a ser realidade, organizando:</p>"""
html = html.replace(old_apply, new_apply)

# 6. Increase text size in "OPlanoÚnico" (Antes do marketing...)
# <p class="t-secondary t-sm mb-4">Empresas que crescem não começam por anúncios...
html = html.replace('<p class="t-secondary t-sm mb-4">Empresas que crescem', '<p class="t-secondary t-body mb-4">Empresas que crescem')
html = html.replace('<ul class="flex flex-col gap-2 t-secondary t-sm"', '<ul class="flex flex-col gap-2 t-secondary t-body"')
html = html.replace('<p class="mt-4 t-sm"><strong>É um plano', '<p class="mt-4 t-body"><strong>É um plano')

# 7. Add Lightbox to all social proofs in the slider
# Ensure the slider images have onclick="openLightbox(this.src)" and cursor:pointer
# I previously used regex, let's just make sure it's applied correctly to ALL slider images.
def add_lightbox(match):
    img_tag = match.group(0)
    if 'onclick' not in img_tag:
        return img_tag.replace('class="w-full"', 'class="w-full" style="cursor: pointer;" onclick="openLightbox(this.src)"')
    return img_tag

# Only replace inside the slider track
slider_match = re.search(r'<div class="slider-track".*?>(.*?)</div>\s*</div>', html, re.DOTALL)
if slider_match:
    old_slider_content = slider_match.group(1)
    new_slider_content = re.sub(r'<img[^>]+>', add_lightbox, old_slider_content)
    html = html.replace(old_slider_content, new_slider_content)

# 8. Secret class text
# Change: <h4 class="t-h4 mb-3 t-accent">O que você vai aprender na Aula Secreta</h4>
old_secret = '<h4 class="t-h4 mb-3 t-accent">O que você vai aprender na Aula Secreta</h4>'
new_secret = '<h4 class="t-h4 mb-3 t-accent">Aula Secreta Liberada por Tempo Limitado</h4>'
html = html.replace(old_secret, new_secret)

# 9. Attack postar todo dia
# In CTA Section:
old_cta = """      O primeiro passo não é anunciar mais. É organizar o caminho da venda.
    </p>"""
new_cta = """      O primeiro passo não é anunciar mais, nem se desgastar postando todo dia qualquer coisa sem critério. Isso só drena sua energia e não traz retorno.<br><br>
      É preciso organizar o caminho da venda com inteligência.
    </p>"""
html = html.replace(old_cta, new_cta)

with open("public_html/index.html", "w", encoding="utf-8") as f:
    f.write(html)
