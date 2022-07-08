// Navbar toggle for smaller screens
const burgerIcon = document.querySelector('#burger');
const navbarMenu = document.querySelector('#nav-links');

//Adding event listener to cause the menu to show up when user clicks on three lines in the upper right corner
"event.preventDefault()"
burgerIcon.addEventListener("click", (event) => {
  navbarMenu.classList.toggle("is-active");
  event.preventDefault();
});