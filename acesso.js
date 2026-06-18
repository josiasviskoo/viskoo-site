/*!
 * Viskoo — Controle de Acesso Interno
 * ─────────────────────────────────────────────────────────
 * PARA ALTERAR A SENHA: mude APENAS a variável SENHA abaixo.
 * Este é o único arquivo que precisa ser editado.
 * ─────────────────────────────────────────────────────────
 */
(function () {

  /* ════════════════════════════════════
     ↓  SENHA — altere somente aqui  ↓
     ════════════════════════════════════ */
  var SENHA = "viskoo@2026";
  /* ════════════════════════════════════
     ↑  SENHA — altere somente aqui  ↑
     ════════════════════════════════════ */

  var CHAVE_SESSAO = "vk_acesso_ok";

  /* Já autenticado nesta sessão: liberar imediatamente */
  if (sessionStorage.getItem(CHAVE_SESSAO) === "1") return;

  /* ─── CSS do gate ─── */
  var css = [
    "#vk-gate{",
      "position:fixed;inset:0;z-index:99999;",
      "background:#080808;",
      "display:flex;align-items:center;justify-content:center;",
      "font-family:'DM Sans',-apple-system,BlinkMacSystemFont,sans-serif;",
      "-webkit-font-smoothing:antialiased;",
      "padding:24px;",
      "opacity:1;",
      "transition:opacity 0.35s cubic-bezier(0.25,0.46,0.45,0.94);",
    "}",
    "#vk-gate-box{",
      "background:#111111;",
      "border:1px solid rgba(255,255,255,0.07);",
      "border-radius:20px;",
      "padding:40px 36px 36px;",
      "width:100%;max-width:360px;",
      "box-shadow:0 12px 48px rgba(0,0,0,0.7);",
      "text-align:center;",
    "}",
    "#vk-gate-logo{",
      "display:inline-flex;align-items:center;justify-content:center;",
      "width:44px;height:44px;",
      "background:#f48322;",
      "border-radius:10px;",
      "font-weight:700;font-size:18px;color:#000;",
      "margin:0 auto 20px;",
    "}",
    "#vk-gate-title{",
      "font-size:18px;font-weight:700;",
      "color:#f0f0f0;letter-spacing:-0.03em;",
      "margin-bottom:6px;",
    "}",
    "#vk-gate-sub{",
      "font-size:13px;",
      "color:rgba(240,240,240,0.40);",
      "margin-bottom:28px;line-height:1.55;",
    "}",
    "#vk-gate-input{",
      "width:100%;",
      "background:#1a1a1a;",
      "border:1px solid rgba(255,255,255,0.07);",
      "border-radius:10px;",
      "color:#f0f0f0;",
      "font-family:'DM Mono','Fira Mono',monospace;",
      "font-size:20px;",
      "letter-spacing:0.22em;",
      "padding:13px 16px;",
      "outline:none;text-align:center;",
      "transition:border-color 0.15s,box-shadow 0.15s;",
      "margin-bottom:12px;",
      "-webkit-appearance:none;appearance:none;",
    "}",
    "#vk-gate-input::placeholder{",
      "color:rgba(240,240,240,0.22);",
      "letter-spacing:0.16em;font-size:14px;",
    "}",
    "#vk-gate-input:focus{",
      "border-color:#f48322;",
      "box-shadow:0 0 0 3px rgba(244,131,34,0.15);",
    "}",
    "#vk-gate-btn{",
      "width:100%;height:46px;",
      "background:#f48322;color:#000;",
      "border:none;border-radius:10px;",
      "font-family:'DM Sans',-apple-system,sans-serif;",
      "font-size:14px;font-weight:600;",
      "cursor:pointer;",
      "letter-spacing:0.01em;",
      "transition:background 0.15s,transform 0.1s cubic-bezier(0.34,1.56,0.64,1);",
    "}",
    "#vk-gate-btn:hover{background:#ff9a3c;}",
    "#vk-gate-btn:active{transform:scale(0.97);}",
    "#vk-gate-err{",
      "font-size:12px;color:#ff453a;",
      "margin-top:12px;min-height:16px;",
      "opacity:0;transition:opacity 0.2s;",
    "}",
    "#vk-gate-err.vk-show{opacity:1;}",
    "@keyframes vk-shake{",
      "0%,100%{transform:translateX(0);}",
      "20%,60%{transform:translateX(-7px);}",
      "40%,80%{transform:translateX(7px);}",
    "}",
    ".vk-shake{animation:vk-shake 0.38s ease;}",
  ].join("");

  /* Injeta estilos no <head> imediatamente (antes da body ser pintada) */
  var styleEl = document.createElement("style");
  styleEl.textContent = css;
  (document.head || document.documentElement).appendChild(styleEl);

  /* ─── Markup do gate ─── */
  var gate = document.createElement("div");
  gate.id = "vk-gate";
  gate.innerHTML =
    '<div id="vk-gate-box">' +
      '<div id="vk-gate-logo">V</div>' +
      '<div id="vk-gate-title">Acesso restrito</div>' +
      '<div id="vk-gate-sub">Documento confidencial da Viskoo.<br>Insira a senha para continuar.</div>' +
      '<input id="vk-gate-input" type="password" placeholder="••••••••" autocomplete="off" />' +
      '<button id="vk-gate-btn">Entrar</button>' +
      '<div id="vk-gate-err">Senha incorreta. Tente novamente.</div>' +
    '</div>';

  /* ─── Lógica de verificação ─── */
  function verificar() {
    var input = document.getElementById("vk-gate-input");
    var err   = document.getElementById("vk-gate-err");
    var box   = document.getElementById("vk-gate-box");

    if (input.value === SENHA) {
      sessionStorage.setItem(CHAVE_SESSAO, "1");
      var g = document.getElementById("vk-gate");
      g.style.opacity = "0";
      setTimeout(function () {
        if (g && g.parentNode) g.parentNode.removeChild(g);
        if (styleEl && styleEl.parentNode) styleEl.parentNode.removeChild(styleEl);
      }, 380);
    } else {
      input.value = "";
      err.classList.add("vk-show");
      box.classList.remove("vk-shake");
      /* force reflow para reiniciar animação */
      void box.offsetWidth;
      box.classList.add("vk-shake");
      setTimeout(function () { err.classList.remove("vk-show"); }, 3500);
      input.focus();
    }
  }

  /* ─── Monta o gate no DOM ─── */
  function montar() {
    document.body.appendChild(gate);

    var input = document.getElementById("vk-gate-input");
    var btn   = document.getElementById("vk-gate-btn");

    input.focus();

    btn.addEventListener("click", verificar);
    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter") verificar();
    });
  }

  if (document.body) {
    montar();
  } else {
    document.addEventListener("DOMContentLoaded", montar);
  }

}());
