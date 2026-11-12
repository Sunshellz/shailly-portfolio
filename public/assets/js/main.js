/* Shailly — portfolio interactions */
(function () {
  'use strict';

  var doc = document;
  doc.documentElement.classList.add('js');

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- mobile navigation ---------- */
  var toggle = doc.querySelector('.nav-toggle');
  var menu = doc.getElementById('mobile-menu');
  var header = doc.querySelector('.site-header');

  function closeMenu() {
    if (!menu || !toggle) return;
    menu.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    doc.body.style.overflow = '';
    window.setTimeout(function () {
      if (!menu.classList.contains('is-open')) menu.hidden = true;
    }, 300);
  }

  function openMenu() {
    if (!menu || !toggle) return;
    menu.hidden = false;
    // force a frame so the transition runs
    window.requestAnimationFrame(function () {
      menu.classList.add('is-open');
    });
    toggle.setAttribute('aria-expanded', 'true');
    doc.body.style.overflow = 'hidden';
  }

  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var isOpen = toggle.getAttribute('aria-expanded') === 'true';
      if (isOpen) closeMenu(); else openMenu();
    });

    menu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeMenu);
    });

    doc.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        closeMenu();
        toggle.focus();
      }
    });

    // only render the full-screen menu on small screens
    var mq = window.matchMedia('(min-width: 1025px)');
    var onDesktop = function (e) {
      if (e.matches) closeMenu();
    };
    if (mq.addEventListener) mq.addEventListener('change', onDesktop);
    else if (mq.addListener) mq.addListener(onDesktop);
  }

  /* ---------- sticky header state ---------- */
  if (header) {
    var lastState = false;
    var onScroll = function () {
      var scrolled = window.scrollY > 12;
      if (scrolled !== lastState) {
        header.classList.toggle('is-scrolled', scrolled);
        lastState = scrolled;
      }
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- active navigation ---------- */
  var path = window.location.pathname.replace(/index\.html$/, '');
  if (path.length > 1) path = path.replace(/\/$/, '');

  function isCurrent(href) {
    var url = new URL(href, window.location.origin);
    var target = url.pathname.replace(/index\.html$/, '');
    if (target.length > 1) target = target.replace(/\/$/, '');
    if (target === '' || target === '/') return path === '' || path === '/';
    return path === target || path.indexOf(target + '/') === 0;
  }

  doc.querySelectorAll('[data-nav]').forEach(function (link) {
    if (isCurrent(link.getAttribute('href'))) {
      link.classList.add('is-active');
      link.setAttribute('aria-current', 'page');
    }
    link.removeAttribute('data-nav');
  });

  /* ---------- reveal on scroll ---------- */
  var revealItems = Array.prototype.slice.call(doc.querySelectorAll('.reveal'));

  if ('IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    revealItems.forEach(function (el) { io.observe(el); });
  } else {
    revealItems.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---------- current year ---------- */
  doc.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
