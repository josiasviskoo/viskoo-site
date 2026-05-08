import re

with open("public_html/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Change WhatsApp/Agendar Diagnóstico links to Calendar
html = html.replace('https://wa.me/55', 'https://calendar.app.google/U81aADH1LgpMBPdH8')

# 2. Change Quiz links
html = html.replace('href="#" class="btn btn-outline btn-lg" style="background: rgba(255,255,255,0.05);">Aplicar ao Quiz', 'href="https://viskoo.com.br/quizz" target="_blank" class="btn btn-outline btn-lg" style="background: rgba(255,255,255,0.05);">Aplicar ao Quiz')

html = html.replace('href="#" class="btn btn-outline btn-xl" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">Aplicar ao Quiz', 'href="https://viskoo.com.br/quizz" target="_blank" class="btn btn-outline btn-xl" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">Aplicar ao Quiz')


with open("public_html/index.html", "w", encoding="utf-8") as f:
    f.write(html)
