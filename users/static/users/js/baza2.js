console.log("jejejejeje");

let klucz = 1;
console.log(klucz);
// if (klucz == 1) {
//   window.location.href = "http://127.0.0.1:8000/dotestow/strona/a/";
// } else {
//   window.location.href = "http://127.0.0.1:8000/dotestow/strona/b/";
// }

const head = document.getElementsByTagName("head");
console.log(head[0].children);

// let meta = document.createElement("meta");
// meta.httpEquiv = "refresh";
// meta.content = "0; url=http://wp.pl";
// document.getElementsByTagName("head")[0].appendChild(meta);
// document.getElementsByTagName("head")[0].prepend(meta);
// console.log(head[0]);

let script = document.createElement("script");
script.type = "text/javascript";
// script.innerHTML = 'window.location.href = "http://wp.pl";';
// script.innerHTML = 'window.location.replace = "http://wp.pl";';
document.getElementsByTagName("head")[0].prepend(script);

console.log(head[0]);

const myButton = document.querySelector("#myButton");
let previous = null;

myButton.addEventListener("click", () => {
  const myInput = document.querySelector("#myInput");
  const copy = myInput.innerHTML;
  console.log(copy);
  navigator.clipboard.writeText(copy);
  document.querySelector("#myButton").textContent = "Copied";

  if (previous) {
    previous.textContent = "Copy";
  }
  previous = myButton;
});

const myButtonScript = document.querySelector("#myButtonScript");

window.addEventListener("DOMContentLoaded", () => {
  const user = document.querySelector("#user");
  const iduser = document.querySelector("#iduser");
  document.querySelector(
    "#myScript"
  ).innerText = ` <script> hujemu5hje \n user_id: ${iduser.innerHTML} \n  </script> `;
});

myButtonScript.addEventListener("click", () => {
  const myScript = document.querySelector("#myScript");
  const copy = myScript.innerHTML;
  console.log(copy);
  navigator.clipboard.writeText(copy);

  if (previous) {
    previous.textContent = "Copy";
  }
  previous = myButtonScript;
});
