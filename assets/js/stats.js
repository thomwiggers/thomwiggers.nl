/* stats.js */
var _paq = window._paq = window._paq || [];
/* tracker methods like "setCustomDimension" should be called before "trackPageView" */
_paq.push(["setDoNotTrack", true]);
_paq.push(['addDownloadExtensions', "bib"]);
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
_paq.push(['setRequestMethod', 'POST']);
(function() {
  var u="https://matomo.rded.nl/";
  _paq.push(['setTrackerUrl', u+'m.track']);
  _paq.push(['setSiteId', '1']);
  var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
  g.type='text/javascript'; g.async=true; g.src=u+'js/'; s.parentNode.insertBefore(g,s);
})();
