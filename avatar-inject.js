// Replace OI initials with actual photo
(function() {
  function injectAvatar() {
    var divs = document.querySelectorAll('.byline-avatar, .author-bio-avatar');
    divs.forEach(function(div) {
      div.innerHTML = '';
      var img = document.createElement('img');
      img.src = 'avatar.jpg';
      img.alt = 'Dr. Oliver Inderwildi';
      img.style.cssText = 'width:100%;height:100%;object-fit:cover;object-position:center 20%;display:block;border-radius:50%;';
      div.style.cssText += ';padding:0;font-size:0;';
      div.appendChild(img);
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectAvatar);
  } else {
    injectAvatar();
  }
})();
