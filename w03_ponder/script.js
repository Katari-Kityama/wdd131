const menuButton = document.querySelector('.menu-btn'); 
const nav = document.querySelector('nav');

menuButton.addEventListener('click', function() {
  
    menuButton.classList.toggle('change');
    nav.classList.toggle('unhide');
});

