// ---- 单文件加载器：并行解包内嵌资源 → 内存表 → 按需生成 blob URL → 启动 game.js ----
(function () {
  'use strict';
  var T0 = performance.now(), TOTAL = 12232734;
  var boot = document.getElementById('boot'), bt = document.getElementById('boot-t');
  var pr = document.createElement('div'); pr.className = 'pr'; pr.innerHTML = '<i></i>';
  var pn = document.createElement('div'); pn.className = 'pn';
  boot.appendChild(pr); boot.appendChild(pn);
  var bar = pr.firstChild;
  function prog(f, label) { bar.style.transform = 'scaleX(' + Math.max(0, Math.min(1, f)).toFixed(3) + ')'; pn.textContent = Math.round(f * 100) + '%'; if (label) bt.textContent = label; }
  var failed = false;
  function fail(msg) { failed = true; var b = document.getElementById('boot'); if (!b) { b = document.createElement('div'); b.id = 'boot'; document.body.appendChild(b); b.appendChild(bt); } b.className = 'err'; bt.textContent = msg; console.error('[faceoff] ' + msg); }
  // 诊断：平台安全策略（CSP）、脚本错误、未处理的 Promise 拒绝都直接显示在载入页上，方便上传后排查
  var cspHits = [];
  document.addEventListener('securitypolicyviolation', function (e) { cspHits.push((e.violatedDirective || e.effectiveDirective) + ' ← ' + (e.blockedURI || 'inline')); });
  window.addEventListener('error', function (e) { if (!window.__game || !window.__game.ready) fail('载入出错：' + (e.message || e) + (e.filename ? '（' + String(e.filename).slice(0, 60) + ':' + e.lineno + '）' : '') + (cspHits.length ? '｜安全策略拦截：' + cspHits.join('；') : '')); });
  window.addEventListener('unhandledrejection', function (e) { if (!window.__game || !window.__game.ready) fail('载入出错：' + ((e.reason && (e.reason.message || e.reason)) || '未知') + (cspHits.length ? '｜安全策略拦截：' + cspHits.join('；') : '')); });
  if (typeof DecompressionStream !== 'function') { fail('这个浏览器太旧，打不开单文件版：请用最新版 Chrome（或 Safari 16.4+ / Firefox 113+）'); return; }
  var MEM = Object.create(null), URLS = Object.create(null), REV = Object.create(null);
  var blobUrlCount = 0;
  function getUrl(k) {
    if (!k || !MEM[k]) return null;
    if (!URLS[k]) { var u = URL.createObjectURL(MEM[k]); URLS[k] = u; REV[u] = MEM[k]; blobUrlCount++; }
    return URLS[k];
  }
  window.__FO_SINGLE = { mem: MEM, urls: URLS, getUrl: getUrl, t0: T0 };
  var BASE = location.href.replace(/[?#].*$/, '').replace(/[^/]*$/, '');
  function rel(u) {
    u = String(u);
    if (u.indexOf(BASE) === 0) u = u.slice(BASE.length);
    else if (/^[a-z][a-z0-9+.-]*:/i.test(u)) return null;
    u = u.replace(/^\.\//, '').replace(/[?#].*$/, '');
    try { u = decodeURIComponent(u); } catch (e) { /* 保持原样 */ }
    return u;
  }
  var hasFromB64 = typeof Uint8Array.fromBase64 === 'function';
  var decodeMs = 0;
  function b64bytes(s) {
    var t0 = performance.now();
    var out;
    if (hasFromB64) {
      out = Uint8Array.fromBase64(s);
    } else {
      var bin = atob(s), n = bin.length;
      out = new Uint8Array(n);
      for (var i = 0; i < n; i++) out[i] = bin.charCodeAt(i);
    }
    decodeMs += performance.now() - t0;
    return out;
  }
  function inflate(bytes) { return new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream('deflate-raw'))).arrayBuffer(); }
  async function unpack(el) {
    var rawStr = el.el ? el.el.textContent : el.b;
    if (el.el) el.el.textContent = '';
    el.b = null;
    var bytes = b64bytes(rawStr);
    rawStr = null;
    var data = el.z == 1 ? await inflate(bytes) : bytes;
    bytes = null;
    return new Blob([data], { type: el.t });
  }
  // fetch 拦截：内存表里有的直接返回；别的照常（blob: / data: / 网络）
  var realFetch = window.fetch.bind(window);
  window.fetch = function (input, init) {
    var u = typeof input === 'string' ? input : input && input.url !== undefined ? input.url : String(input);
    if (typeof u === 'string' && u.indexOf('blob:') === 0 && REV[u]) return Promise.resolve(new Response(REV[u], { status: 200, statusText: 'OK', headers: { 'Content-Type': REV[u].type || 'application/octet-stream' } }));
    var r = rel(u);
    if (r !== null && MEM[r]) return Promise.resolve(new Response(MEM[r], { status: 200, statusText: 'OK', headers: { 'Content-Type': MEM[r].type || 'application/octet-stream' } }));
    if (r !== null && /^assets\//.test(r)) { console.warn('[faceoff] 单文件里没有：' + r); return Promise.resolve(new Response('', { status: 404, statusText: 'Not Found' })); }
    return realFetch(input, init);
  };
  // <style> 里的 url(assets/…) → 按需生成 blob:（@font-face）
  function fixCss(node) {
    var t = node.textContent; if (!t || t.indexOf('assets/') < 0) return;
    var n = t.replace(/url\((["']?)(\.?\/?assets\/[^"')]+)\1\)/g, function (m, q, p) { var u = getUrl(rel(p)); return u ? 'url("' + u + '")' : m; });
    if (n !== t) node.textContent = n;
  }
  new MutationObserver(function (list) { list.forEach(function (m) { m.addedNodes.forEach(function (n) { if (n.tagName === 'STYLE') fixCss(n); }); }); }).observe(document.head, { childList: true });
  (async function () {
    try {
      // 资源块：单文件 = 页面里的 <script type="text/x-fo">；文件夹版 = assets/pack-NN.js 推进 window.__FO_B 的 [路径, 类型, 压缩?, 原始字节, base64]
      var els = window.__FO_B ? window.__FO_B.map(function (a) { return { p: a[0], t: a[1], z: a[2], n: a[3], b: a[4] }; })
        : Array.prototype.slice.call(document.querySelectorAll('script[type="text/x-fo"]')).map(function (el) { return { el: el, p: el.getAttribute('data-p'), t: el.getAttribute('data-t'), z: +el.getAttribute('data-z'), n: +el.getAttribute('data-n') || 0 }; });
      window.__FO_B = null;
      var totalCount = els.length;
      // 优先解包 game.js 与 maps/index.json，其余并发解包（上限 6 路，兼顾速度与峰值内存）
      els.sort(function (a, b) {
        var pa = a.p === 'assets/game.js' ? 0 : a.p === 'assets/maps/index.json' ? 1 : 2;
        var pb = b.p === 'assets/game.js' ? 0 : b.p === 'assets/maps/index.json' ? 1 : 2;
        return pa - pb;
      });
      var done = 0, game = null, nextIdx = 0;
      prog(0, '正在解包资源');
      var CONCURRENCY = Math.min(6, Math.max(1, els.length));
      async function worker() {
        while (nextIdx < els.length) {
          var i = nextIdx++;
          var el = els[i];
          els[i] = null;
          var p = el.p, n = el.n;
          var blob = await unpack(el);
          if (p === 'assets/game.js') game = blob; else MEM[p] = blob;
          done += n;
          prog(done / TOTAL * 0.92);
        }
      }
      var workers = [];
      for (var w = 0; w < CONCURRENCY; w++) workers.push(worker());
      await Promise.all(workers);
      els = null;
      // 地图清单里的缩略图（<img src>）按需改成 blob:
      if (MEM['assets/maps/index.json']) {
        var j = JSON.parse(await MEM['assets/maps/index.json'].text());
        (j.maps || []).forEach(function (m) { var k = m.thumb && rel(m.thumb); if (k) m.thumb = getUrl(k) || null; });
        MEM['assets/maps/index.json'] = new Blob([JSON.stringify(j)], { type: 'application/json' });
      }
      document.querySelectorAll('style').forEach(fixCss);
      var unpackMs = performance.now() - T0;
      window.__FO_SINGLE.unpackMs = unpackMs;
      window.__FO_SINGLE.metrics = { unpackMs: +unpackMs.toFixed(1), decodeMs: +decodeMs.toFixed(1), assetCount: totalCount, totalRaw: done, blobUrls: blobUrlCount };
      prog(0.95, '正在载入');
      if (!game) { fail('单文件里没有 game.js（打包出错）'); return; }
      // 启动 game.js：先用内联 module；若被平台安全策略拦截（不允许内联脚本），改用 blob: 地址；都不行就把原因显示出来
      var code = await game.text(), started = false;
      game = null;
      window.addEventListener('faceoff:started', function () { started = true; });
      var inj = function (mode) {
        var s = document.createElement('script'); s.type = 'module';
        if (mode === 'inline') s.textContent = code + '\n;window.dispatchEvent(new Event("faceoff:started"));';
        else { var u = URL.createObjectURL(new Blob([code + '\n;window.dispatchEvent(new Event("faceoff:started"));'], { type: 'text/javascript' })); s.src = u; s.onload = function () { URL.revokeObjectURL(u); }; s.onerror = function () { URL.revokeObjectURL(u); fail('游戏脚本没能执行（blob 方式）' + (cspHits.length ? '｜安全策略拦截：' + cspHits.join('；') : '')); }; }
        document.body.appendChild(s);
      };
      var n0 = cspHits.length; inj('inline');
      await new Promise(function (r) { setTimeout(r, 600); });
      if (!started && !failed && cspHits.length > n0) { prog(0.97, '正在载入（备用方式）'); inj('blob'); }
      code = null;
      setTimeout(function () { if (!failed && !(window.__game && window.__game.ready) && document.getElementById('boot')) fail('载入超时（60 秒）。' + (cspHits.length ? '安全策略拦截：' + cspHits.join('；') : '没有捕获到错误，请把这段文字和截图发给开发者') + '｜started=' + started); }, 60000);
    } catch (e) { fail('解包失败：' + (e && e.message || e)); }
  })();
})();
