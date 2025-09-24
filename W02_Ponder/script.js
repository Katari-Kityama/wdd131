
let selectElem = document.querySelector('#theme-select');
let pageContent = document.querySelector('body');

selectElem.addEventListener('change', changeTheme);

function changeTheme() {
    let current = selectElem.value;
    if (current === 'LightForest') {
        document.body.style.backgroundImage = 'url("LightTrees.jpg")';
        pageContent.style.fontFamily = "Papyrus, fantasy";
    } else if (current === 'ShadowForest') {
        document.body.style.backgroundImage = 'url("ShadowTrees.jpg")';
        pageContent.style.fontFamily = "Impact, sans-serif";
    } else if (current === 'RingedPlanet') {
        document.body.style.backgroundImage = 'url("RingedPlanet.jpg")';
        pageContent.style.fontFamily = "'Big Caslon', serif";
    } else {
        // default
        document.body.style.backgroundImage = "none";
        pageContent.style.fontFamily = "Georgia, serif";
    }
}
          