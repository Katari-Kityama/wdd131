const levelElement = document.querySelector('#level');
const healthElement = document.querySelector('#health');
const attacked = document.querySelector('#attacked');
const levelup = document.querySelector('#levelup');

let level = 5;
let health = 100;

attacked.addEventListener("click", function () {

    health = health - 20;
    healthElement.innerHTML = `<b>Health:</b> ${health}`;

    if (health === 0) {
    alert("Character Died");
    }
    
    console.log("Attacked!");
});   

levelup.addEventListener("click", function () {
  
    level = level + 1;
    levelElement.innerHTML = `<b>Level:</b> ${level}`;

    console.log("Level Up!");
});   
