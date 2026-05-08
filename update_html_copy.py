import re

with open("public_html/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Secret Class YouTube Link
html = html.replace('<a href="#" class="btn btn-primary btn-lg">Quero acessar a aula</a>', '<a href="https://youtu.be/opIfEweGgck" target="_blank" class="btn btn-primary btn-lg">Quero acessar a aula</a>')

# 2. Hero Section
old_hero = """<h1 class="hero-title">Se você não sabe de onde vem seu cliente, você não tem marketing.<br><em>Tem sorte.</em></h1>
    <p class="hero-sub t-body t-secondary">Saia da tentativa e entre na previsibilidade de vendas.</p>
    <p class="hero-sub t-body t-secondary" style="max-width: 600px; margin: 0 auto var(--space-5);">
      Empresas estruturadas não dependem de indicação, “mês bom” ou improviso. Elas seguem um plano claro, executável e baseado em dados.<br><br>
      Eu ajudo empresas a organizarem o marketing em um sistema previsível, onde cada ação tem direção, função e objetivo mensurável.
    </p>"""
new_hero = """<h1 class="hero-title">Se você não sabe de onde vem seu cliente, você não tem marketing.<br><em>Falta processo.</em></h1>
    <p class="hero-sub t-body t-secondary">Saia da montanha-russa do faturamento e entre na previsibilidade de vendas.</p>
    <p class="hero-sub t-body t-secondary" style="max-width: 600px; margin: 0 auto var(--space-5);">
      Ter clientes todos os dias não é uma questão de sorte ou de "rezar por indicações", mas sim um processo de engenharia bem estruturado.<br><br>
      Eu ajudo empresas a organizarem o marketing em um sistema previsível, onde cada ação tem direção, função e objetivo mensurável.
    </p>"""
html = html.replace(old_hero, new_hero)

# 3. Method 5 Pillars
# Replace the small "O que não é" card in Method section
old_small_not = """      <div class="card card-body">
        <h4 class="t-h4 mb-3 t-accent">O que não é</h4>
        <ul class="flex flex-col gap-2 t-secondary t-body" style="list-style: none;">
          <li><span class="t-muted">→</span> Não é curso.</li>
          <li><span class="t-muted">→</span> Não é teoria.</li>
          <li><span class="t-muted">→</span> Não é mais uma “estratégia milagrosa”.</li>
        </ul>
        <p class="mt-4 t-body"><strong>É um plano aplicado dentro da realidade da empresa.</strong></p>
      </div>"""
new_pillars = """      <div class="card card-body">
        <h4 class="t-h4 mb-3 t-accent">Os 5 Pilares do OPlanoÚnico™</h4>
        <ul class="flex flex-col gap-3 t-secondary t-body" style="list-style: none;">
          <li><strong class="t-white" style="color:var(--text-primary);">1. Mensagem Base:</strong> Definição do que atrai o cliente certo.</li>
          <li><strong class="t-white" style="color:var(--text-primary);">2. Base Receptiva:</strong> Preparação para quem encontrar a empresa estar pronto para comprar.</li>
          <li><strong class="t-white" style="color:var(--text-primary);">3. Ponto de Decisão:</strong> Redução de fricção na conversão.</li>
          <li><strong class="t-white" style="color:var(--text-primary);">4. Aquisição Ativa:</strong> Eficiência máxima nos anúncios.</li>
          <li><strong class="t-white" style="color:var(--text-primary);">5. Painel de Decisão:</strong> Gestão baseada em dados, não em achismo.</li>
        </ul>
      </div>"""
html = html.replace(old_small_not, new_pillars)

# 4. Positioning - Title in Dashboard
old_dash_title = '<h2 class="t-h2 mb-4">Visibilidade total da sua operação</h2>'
new_dash_title = '<h2 class="t-h2 mb-4">Marketing não é opinião. É decisão.</h2>'
html = html.replace(old_dash_title, new_dash_title)

# 4. Positioning - Apply Text
old_apply_text = '<p class="t-body t-secondary mb-4">Não somos apenas um curso ou uma mentoria. Nós somos a <strong>mão de obra</strong>. A Viskoo atua prestando um serviço focado em execução ao seu lado. Aqui o plano deixa de ser conceito e passa a ser realidade, organizando:</p>'
new_apply_text = '<p class="t-body t-secondary mb-4">Você está contratando profissionais que aplicam um <strong>método validado</strong>, e não pessoas que apenas vendem ferramentas ou executam tarefas soltas. Nós somos a <strong>mão de obra</strong> prestando um serviço focado em execução lado a lado com a sua empresa. Aqui o plano deixa de ser conceito e passa a ser realidade, organizando:</p>'
html = html.replace(old_apply_text, new_apply_text)

# 5. Qualificação ("Para quem é")
old_qual = """        <ul class="flex flex-col gap-3 t-secondary t-body" style="list-style: none;">
          <li class="flex items-center gap-2"><svg class="icon icon-sm" style="color: #30d158;" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg> Querem clareza e valorizam estrutura</li>
          <li class="flex items-center gap-2"><svg class="icon icon-sm" style="color: #30d158;" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg> Entendem que crescimento exige método</li>
          <li class="flex items-center gap-2"><svg class="icon icon-sm" style="color: #30d158;" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg> Buscam previsibilidade ao invés de promessas</li>
          <li class="flex items-center gap-2"><svg class="icon icon-sm" style="color: #30d158;" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg> Desejam parar de testar ações soltas</li>
          <li class="flex items-center gap-2"><svg class="icon icon-sm" style="color: #30d158;" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg> Entendem que marketing é processo</li>
        </ul>"""

new_qual = """        <ul class="flex flex-col gap-3 t-secondary t-body" style="list-style: none;">
          <li class="flex items-start gap-2"><svg class="icon icon-sm" style="color: #30d158; flex-shrink: 0; margin-top: 4px;" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg> Não buscam atalhos fáceis, mas sim processos validados.</li>
          <li class="flex items-start gap-2"><svg class="icon icon-sm" style="color: #30d158; flex-shrink: 0; margin-top: 4px;" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg> Não esperam que a agência faça milagres sozinha sem colaboração.</li>
          <li class="flex items-start gap-2"><svg class="icon icon-sm" style="color: #30d158; flex-shrink: 0; margin-top: 4px;" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg> Priorizam a qualidade do resultado financeiro em vez do volume de tarefas.</li>
        </ul>"""
html = html.replace(old_qual, new_qual)

# 6. Final CTA
old_final = """      É preciso organizar o caminho da venda com inteligência.
    </p>"""
new_final = """      É preciso organizar o caminho da venda com inteligência.<br><br>
      <strong style="color: var(--text-primary);">O que define o próximo resultado não é mais informação. É decisão.</strong>
    </p>"""
html = html.replace(old_final, new_final)

# 7. Add Quiz Button (Hero)
old_hero_btn = """    <div class="hero-actions mb-6">
      <a href="https://wa.me/55" class="btn btn-primary btn-lg">Conversar no WhatsApp</a>
    </div>"""
new_hero_btn = """    <div class="hero-actions mb-6 flex gap-3 justify-center flex-wrap">
      <a href="https://wa.me/55" class="btn btn-primary btn-lg">Conversar no WhatsApp</a>
      <a href="#" class="btn btn-outline btn-lg" style="background: rgba(255,255,255,0.05);">Aplicar ao Quiz</a>
    </div>"""
html = html.replace(old_hero_btn, new_hero_btn)

# 7. Add Quiz Button (Final CTA)
old_final_btn = '<a href="https://wa.me/55" class="btn btn-primary btn-xl">Conversar no WhatsApp</a>'
new_final_btn = """<div class="flex gap-3 justify-center flex-wrap">
      <a href="https://wa.me/55" class="btn btn-primary btn-xl">Conversar no WhatsApp</a>
      <a href="#" class="btn btn-outline btn-xl" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">Aplicar ao Quiz</a>
    </div>"""
html = html.replace(old_final_btn, new_final_btn)

with open("public_html/index.html", "w", encoding="utf-8") as f:
    f.write(html)
