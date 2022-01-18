const body = document.querySelector("body");
const mainMenu = document.querySelector(".main-menu");
const mobileMenu = document.querySelector("#mobile-menu");
const button3LinesX = document.querySelector(".button-3lines-x");
const navComputer = document.querySelector(".nav-computer");

// .
// Menu change
const changeMenu = () => {
  body.classList.toggle("body-overflow-active");
  mainMenu.classList.toggle("main-menu-mobile");
  navComputer.classList.toggle("nav-computer-active");
  mobileMenu.classList.toggle("mobile-is-active");
};
button3LinesX.addEventListener("click", changeMenu);

const removeMenu = () => {
  body.classList.remove("body-overflow-active");
  mainMenu.classList.remove("main-menu-mobile");
  navComputer.classList.remove("nav-computer-active");
  mobileMenu.classList.remove("mobile-is-active");
};
