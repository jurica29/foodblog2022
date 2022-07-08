// Navbar toggle for smaller screens
const burgerIcon = document.querySelector('#burger');
const navbarMenu = document.querySelector('#nav-links');

"event.preventDefault()"
burgerIcon.addEventListener("click", (event) => {
  navbarMenu.classList.toggle("is-active");
  event.preventDefault();
});