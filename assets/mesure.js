// Compteur du site (migration 74) : d'où viennent les visiteurs.
// Ni cookie, ni IP, ni identifiant : canal `?src=`, langue de la page,
// domaine d'origine. Relaie aussi le canal à Google Play (referrer UTM)
// pour que la Play Console attribue les installations Android.
(function () {
  'use strict';
  var URL_API = 'https://zkrkaimrybxbdrznxhxx.supabase.co/rest/v1/rpc/log_site_visit';
  var KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InprcmthaW1yeWJ4YmRyem54aHh4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODExMDkzMTYsImV4cCI6MjA5NjY4NTMxNn0.28Ns814SQSFXaKRR0-ZrHoX1G8Cpnhf6sNCZ6kgtAio';
  var PLAY = 'https://play.google.com/store/apps/details?id=com.ramio';
  var TESTFLIGHT = 'https://testflight.apple.com/join/';

  var src = '';
  try { src = (new URLSearchParams(location.search).get('src') || '').slice(0, 40); } catch (e) {}
  var lang = /\/en\/?$/.test(location.pathname) ? 'en' : 'fr';
  var ref = '';
  try { ref = document.referrer ? new URL(document.referrer).hostname : ''; } catch (e) {}

  function log(kind) {
    try {
      fetch(URL_API, {
        method: 'POST',
        keepalive: true,
        headers: { apikey: KEY, Authorization: 'Bearer ' + KEY, 'Content-Type': 'application/json' },
        body: JSON.stringify({ p_kind: kind, p_src: src, p_lang: lang, p_ref: ref })
      }).catch(function () {});
    } catch (e) {}
  }

  function ready() {
    var links = document.querySelectorAll('a[href]');
    for (var i = 0; i < links.length; i++) {
      var a = links[i];
      if (a.href.indexOf(PLAY) === 0) {
        if (src) {
          var utm = 'utm_source=' + src + '&utm_medium=site&utm_campaign=beta-' + lang;
          a.href = PLAY + '&referrer=' + encodeURIComponent(utm);
        }
        a.addEventListener('click', function () { log('play'); });
      } else if (a.href.indexOf(TESTFLIGHT) === 0) {
        a.addEventListener('click', function () { log('testflight'); });
      }
    }
    log('visit');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ready);
  } else {
    ready();
  }
})();
