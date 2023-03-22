window.addEventListener('load', function() {
  var width = window.innerWidth;
  var height = window.innerHeight;
  document.body.style.height = height + 'px';
  document.body.style.width = width + 'px';
});

window.addEventListener('resize', function() {
  var height = window.innerHeight;
  var width = window.innerWidth;
  document.body.style.height = height + 'px';
  document.body.style.width = width + 'px';
});