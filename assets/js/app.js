/* Meta_001 interactions. No dependencies, no tracking. */
(function () {
  'use strict';
  var d = document, root = d.documentElement;
  var $ = function (s, c) { return (c || d).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  /* ---- colour scheme */
  var SCHEMES = ['lagoon', 'midnight', 'savanna', 'reef'];
  function setScheme(s) {
    if (SCHEMES.indexOf(s) < 0) s = 'lagoon';
    if (s === 'lagoon') root.removeAttribute('data-scheme'); else root.setAttribute('data-scheme', s);
    store.set('scheme', s);
    $$('.sw').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.scheme === s ? 'true' : 'false'); });
  }
  setScheme(store.get('scheme') || 'lagoon');
  d.addEventListener('click', function (e) {
    var sw = e.target.closest('.sw'); if (sw) { setScheme(sw.dataset.scheme); return; }
    var pb = e.target.closest('.pal-btn');
    if (pb) { var p = pb.closest('.pal'); p.classList.toggle('open'); pb.setAttribute('aria-expanded', p.classList.contains('open')); return; }
    if (!e.target.closest('.pal')) $$('.pal.open').forEach(function (p) { p.classList.remove('open'); });
    var mb = e.target.closest('.menu-btn');
    if (mb) { var n = $('.nav'); n.classList.toggle('open'); mb.setAttribute('aria-expanded', n.classList.contains('open')); }
  });
  d.addEventListener('keydown', function (e) { if (e.key === 'Escape') $$('.pal.open').forEach(function (p) { p.classList.remove('open'); }); });

  /* ---- progress bar and reveal */
  var pb = $('.bar-progress');
  function prog() { if (!pb) return; var h = root.scrollHeight - innerHeight; pb.style.width = (h > 0 ? scrollY / h * 100 : 0) + '%'; }
  addEventListener('scroll', prog, { passive: true }); prog();
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (en) {
      if (!en.isIntersecting) return;
      en.target.classList.add('in'); io.unobserve(en.target);
      $$('[data-count]', en.target).concat(en.target.hasAttribute('data-count') ? [en.target] : []).forEach(count);
    });
  }, { threshold: .15 }) : null;
  $$('.rv,.bars,.console,.kpis').forEach(function (el) { if (io) io.observe(el); else el.classList.add('in'); });
  function count(el) {
    if (el.dataset.done) return; el.dataset.done = 1;
    var t = el.dataset.count, m = t.match(/^([^\d]*)([\d,.]+)(.*)$/);
    if (!m || reduce) { el.textContent = t; return; }
    var n = parseFloat(m[2].replace(/,/g, '')), dec = (m[2].split('.')[1] || '').length, start = performance.now(), dur = 1100;
    (function tick(now) {
      var k = Math.min(1, (now - start) / dur), v = n * (1 - Math.pow(1 - k, 3));
      el.textContent = m[1] + v.toLocaleString('en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec }) + m[3];
      if (k < 1) requestAnimationFrame(tick); else el.textContent = t;
    })(start);
  }

  /* ---- generic filter (chips + cards) */
  function applyField(f) {
    $$('[data-fields]').forEach(function (el) {
      var on = f === 'all' || el.dataset.fields.split(' ').indexOf(f) >= 0;
      if (el.classList.contains('kpi') || el.classList.contains('g-bar')) el.classList.toggle('dim', !on);
      else el.classList.toggle('hide', !on);
    });
    $$('[data-field-chip]').forEach(function (c) { c.setAttribute('aria-pressed', c.dataset.fieldChip === f ? 'true' : 'false'); });
    $$('.bar[data-bar]').forEach(function (c) { c.setAttribute('aria-pressed', c.dataset.bar === f ? 'true' : 'false'); });
    var cnt = $('[data-visible-count]'); if (cnt) cnt.textContent = $$('.sc:not(.hide),.card[data-fields]:not(.hide)').length;
  }
  d.addEventListener('click', function (e) {
    var c = e.target.closest('[data-field-chip],.bar[data-bar]');
    if (!c) return;
    var f = c.dataset.fieldChip || c.dataset.bar;
    if (c.matches('.bar') && c.getAttribute('aria-pressed') === 'true') f = 'all';
    applyField(f);
    if (location.pathname.indexOf('work') >= 0) history.replaceState(null, '', f === 'all' ? location.pathname : '#f-' + f);
  });
  if ($('[data-field-chip]')) {
    var m = location.hash.match(/^#f-(\w+)/); if (m) applyField(m[1]); else applyField('all');
  }

  /* ---- dashboard gantt */
  $$('.g-bar').forEach(function (b) {
    function show() {
      var i = $('#g-info'); if (!i) return;
      i.innerHTML = '<b>' + b.dataset.title + '</b> · ' + b.dataset.org + '<br><small>' + b.dataset.when + '</small><br>' + b.dataset.lead;
      $$('.g-bar').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
    }
    b.addEventListener('mouseenter', show); b.addEventListener('focus', show); b.addEventListener('click', show);
  });

  /* ---- touch: first tap opens a card's hover points */
  var coarse = matchMedia('(hover: none)').matches;
  if (coarse) d.addEventListener('click', function (e) {
    var c = e.target.closest('.card.has-pts'); if (!c) return;
    if (!c.classList.contains('open')) { e.preventDefault(); e.stopImmediatePropagation(); $$('.card.open').forEach(function (o) { o.classList.remove('open'); }); c.classList.add('open'); }
  }, true);

  /* ---- project sheet */
  var sheet = $('#sheet');
  function openProject(id, push) {
    var t = $('#tpl-' + id); if (!t || !sheet) return false;
    $('.sheet-body', sheet).innerHTML = ''; $('.sheet-body', sheet).appendChild(t.content.cloneNode(true));
    if (!sheet.open) sheet.showModal();
    sheet.scrollTop = 0;
    if (push !== false) history.replaceState(null, '', '#' + id);
    return true;
  }
  d.addEventListener('click', function (e) {
    var o = e.target.closest('[data-open]'); if (o && sheet) { e.preventDefault(); openProject(o.dataset.open); return; }
    if (e.target.closest('.sheet-x')) { sheet.close(); return; }
    if (e.target === sheet) sheet.close();
  });
  if (sheet) {
    sheet.addEventListener('close', function () { if (/^#[a-z0-9]+$/.test(location.hash)) history.replaceState(null, '', location.pathname); });
    var h = location.hash.replace('#', ''); if (h && !/^f-/.test(h)) openProject(h, false);
    addEventListener('hashchange', function () { var k = location.hash.replace('#', ''); if (k && !/^f-/.test(k)) openProject(k, false); });
  }

  /* ---- search + topic filters (articles, medium) */
  function topicFilter(scope) {
    var q = ($('.search', scope) || {}).value || '', t = (scope.dataset.topic || 'all');
    q = q.toLowerCase();
    $$('[data-topics]', scope).forEach(function (el) {
      var ok = (t === 'all' || el.dataset.topics.split('|').indexOf(t) >= 0) && (!q || el.textContent.toLowerCase().indexOf(q) >= 0);
      el.classList.toggle('hide', !ok);
    });
    var c = $('[data-n]', scope); if (c) c.textContent = $$('[data-topics]:not(.hide)', scope).length;
  }
  $$('[data-topic-scope]').forEach(function (scope) {
    $$('[data-topic-chip]', scope).forEach(function (b) {
      b.addEventListener('click', function () {
        scope.dataset.topic = b.dataset.topicChip;
        $$('[data-topic-chip]', scope).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        topicFilter(scope);
      });
    });
    var s = $('.search', scope); if (s) s.addEventListener('input', function () { topicFilter(scope); });
  });

  /* ---- business steps */
  $$('.steps').forEach(function (ul) {
    var copy = $('.step-copy', ul.parentNode);
    $$('button', ul).forEach(function (b, i) {
      b.addEventListener('click', function () {
        $$('button', ul).forEach(function (x) { x.setAttribute('aria-selected', x === b ? 'true' : 'false'); });
        copy.textContent = b.dataset.copy;
      });
    });
  });

  /* ---- expertise accordion + experience filter */
  $$('.ex > button').forEach(function (b) {
    b.addEventListener('click', function () { var ex = b.parentNode; var o = ex.classList.toggle('open'); b.setAttribute('aria-expanded', o); });
  });
  $$('[data-exp-chip]').forEach(function (c) {
    c.addEventListener('click', function () {
      var f = c.dataset.expChip;
      $$('[data-exp-chip]').forEach(function (x) { x.setAttribute('aria-pressed', x === c ? 'true' : 'false'); });
      $$('.ex').forEach(function (e) { e.classList.toggle('hide', f !== 'all' && e.dataset.tag !== f); });
    });
  });
  $$('[data-role-chip]').forEach(function (c) {
    c.addEventListener('click', function () {
      var f = c.dataset.roleChip;
      $$('[data-role-chip]').forEach(function (x) { x.setAttribute('aria-pressed', x === c ? 'true' : 'false'); });
      $$('.tl > li').forEach(function (l) { l.classList.toggle('hide', f !== 'all' && l.dataset.fields.split(' ').indexOf(f) < 0); });
    });
  });

  /* ---- scrollspy for the More page */
  var toc = $$('.toc a');
  if (toc.length && io) {
    var spy = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) toc.forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#' + en.target.id); }); });
    }, { rootMargin: '-30% 0px -60% 0px' });
    toc.forEach(function (a) { var s = $(a.getAttribute('href')); if (s) spy.observe(s); });
  }

  /* ---- YouTube thumbnails and lite embeds */
  $$('.thumb[data-yt]').forEach(function (t) {
    var id = t.dataset.yt, img = $('img', t), fb = $('.fallback', t);
    var sizes = ['maxresdefault', 'hqdefault', 'mqdefault'], k = 0;
    function load() { img.src = 'https://i.ytimg.com/vi/' + id + '/' + sizes[k] + '.jpg'; }
    img.addEventListener('load', function () { if (img.naturalWidth < 200 && k < sizes.length - 1) { k++; load(); } else { fb.style.display = 'none'; } });
    img.addEventListener('error', function () { if (k < sizes.length - 1) { k++; load(); } else { img.style.display = 'none'; } });
    load();
    t.addEventListener('click', function () {
      var f = d.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0';
      f.title = t.dataset.title; f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen'; f.allowFullscreen = true; f.loading = 'lazy';
      t.replaceWith(f);
    });
  });

  /* ---- contact: WhatsApp message builder, copy, vCard */
  var tx = $('#wa-text');
  if (tx) {
    var base = 'Hello Kiprop, ';
    var sel = {};
    function build() {
      var parts = Object.keys(sel).filter(function (k) { return sel[k]; });
      tx.value = base + (parts.length ? 'I am writing about ' + parts.join(', ') + '. ' : '') + 'My name is ';
      $('#wa-send').href = 'https://wa.me/254716494214?text=' + encodeURIComponent(tx.value);
    }
    $$('[data-topic-pick]').forEach(function (b) {
      b.addEventListener('click', function () {
        var k = b.dataset.topicPick; sel[k] = !sel[k]; b.setAttribute('aria-pressed', sel[k] ? 'true' : 'false'); build();
      });
    });
    tx.addEventListener('input', function () { $('#wa-send').href = 'https://wa.me/254716494214?text=' + encodeURIComponent(tx.value); });
    build();
  }
  function toast(m) { var t = $('.toast'); if (!t) return; t.textContent = m; t.classList.add('on'); setTimeout(function () { t.classList.remove('on'); }, 1800); }
  $$('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var v = b.dataset.copy;
      (navigator.clipboard ? navigator.clipboard.writeText(v) : Promise.reject()).then(function () { toast('Copied ' + v); }, function () { toast(v); });
    });
  });

  /* ---- hide images that fail to load (the gradient behind shows instead) */
  $$('.ph img,.story img,.feat img,.author img').forEach(function (i) { i.addEventListener('error', function () { i.style.visibility = 'hidden'; }); if (i.complete && !i.naturalWidth) i.style.visibility = 'hidden'; });

  /* ---- prefetch on intent */
  var pf = {};
  function prefetch(a) {
    if (!a.href || a.origin !== location.origin || pf[a.href] || a.hash && a.pathname === location.pathname) return;
    pf[a.href] = 1; var l = d.createElement('link'); l.rel = 'prefetch'; l.href = a.href; d.head.appendChild(l);
  }
  d.addEventListener('mouseover', function (e) { var a = e.target.closest('a'); if (a) prefetch(a); });
  d.addEventListener('touchstart', function (e) { var a = e.target.closest('a'); if (a) prefetch(a); }, { passive: true });

  /* ---- shared-element naming for cross-page transitions */
  addEventListener('pageswap', function (e) {
    if (!e.viewTransition) return;
    var a = document.activeElement; root.dataset.vt = a && a.dataset && a.dataset.vt || '';
  });
})();
