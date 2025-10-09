
const gallery = document.querySelector('.gallery');
const modal = document.querySelector('dialog');
const modalImage = modal.querySelector('img');
const closeButton = modal.querySelector('.close-viewer');

// Event listener for opening the modal
gallery.addEventListener('click', openModal);

function openModal(e) {
    console.log(e.target);
    const img = e.target;
    
    const src = img.getAttribute('src');
    const alt = img.getAttribute('alt');

    const full = src.replace('_sm', '_full');

    modalImage.src = full;
    modalImage.alt = alt;

    modal.showModal();
}

// Close modal on button click
closeButton.addEventListener('click', () => {
    modal.close();
    modalImage.src = ''; // Makes things less confusing by preventing the old image from showing briefly
});

// Close modal if clicking outside the image
modal.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.close();
        modalImage.src = ''; // Makes things less confusing by preventing the old image from showing briefly
    }
});
          
// ------------------------------------------
// Snippet below is from w03_ponder/script.js 
// and is for the menu button functionality

const menuButton = document.querySelector('.menu-btn'); 
const nav = document.querySelector('nav');

menuButton.addEventListener('click', function() {
  
    menuButton.classList.toggle('change');
    nav.classList.toggle('unhide');
});

// ------------------------------------------