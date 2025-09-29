
let selectElem = document.querySelector('#theme-select');
let pageContent = document.querySelector('body');

selectElem.addEventListener('change', changeTheme);

// Changes the class of the body to change the theme depending on what option is selected
function changeTheme() {
    let current = selectElem.value;
    if (current === 'Dark') {
         // dark mode 
        document.body.className = "dark-mode";
    } else if (current === 'Light') {
        // light mode
        document.body.className = "light-mode";
    } else {
        // default
        document.body.className = "light-mode";
    }
}
          