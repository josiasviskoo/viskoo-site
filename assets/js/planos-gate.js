(function (global) {
  var SALT = 'vsk-planos-2019-k7q3';

  function fnv1a(str) {
    var h = 0x811c9dc5;
    for (var i = 0; i < str.length; i++) {
      h ^= str.charCodeAt(i);
      h = (h * 0x01000193) >>> 0;
    }
    return h >>> 0;
  }

  function pad2(n) {
    return n < 10 ? '0' + n : '' + n;
  }

  function toHex8(n) {
    var s = (n >>> 0).toString(16);
    while (s.length < 8) s = '0' + s;
    return s;
  }

  function codeForDate(date) {
    var mm = pad2(date.getMonth() + 1);
    var yyyy = String(date.getFullYear());
    return toHex8(fnv1a(SALT + mm + '-' + yyyy));
  }

  function currentCode() {
    return codeForDate(new Date());
  }

  // Checks whether prices should be shown for the current URL.
  // A bare "?planos" link is redirected to the current month's code so it
  // keeps working forever; a stale/foreign code is treated as absent.
  function isRevealed() {
    var params = new URLSearchParams(location.search);
    var code = currentCode();

    if (params.has('planos')) {
      params.delete('planos');
      var rest = params.toString();
      location.replace(location.pathname + '?' + code + (rest ? '&' + rest : '') + location.hash);
      return false;
    }

    return params.has(code);
  }

  function reveal(prices, idPrefix) {
    if (!isRevealed()) return;
    document.body.classList.add('prices-revealed');
    prices.forEach(function (p, i) {
      var el = document.getElementById(idPrefix + i);
      if (el) el.textContent = p.value;
    });
  }

  global.PlanosGate = {
    currentCode: currentCode,
    isRevealed: isRevealed,
    reveal: reveal
  };
})(window);
