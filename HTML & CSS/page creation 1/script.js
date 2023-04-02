
const hamburger = document.getElementById('hamburgerId'); 
const navUL =  document.getElementById("navBarId");

hamburger.addEventListener('click', () => { 
    alert("This file is connected!");
    navUL.classList.toggle('show');
});