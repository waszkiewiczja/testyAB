console.log("teeeeeees");
const linksplit = document.querySelector("#linksplit");

let keyvalue = 1;
if (keyvalue == 1) {
  linksplit.href = "#333";
} else if (keyvalue == 2) {
  linksplit.href = "#444";
}
console.log(linksplit.href);

let mojeCookies = document.cookie.split(";");
console.log(mojeCookies);

const javascriptclick = document.querySelector("#javascriptclick");

console.log(`Javascript click: ${javascriptclick.innerHTML}`);

for (let i = 0; i < mojeCookies.length; i++) {
  let singleCookie = mojeCookies[i].split("=");
  if (singleCookie[0] == "splitAB") {
    console.log("jabadu");
    console.log(singleCookie[0], singleCookie[1]);
  } else {
    document.cookie = `splitAB = ${javascriptclick.innerHTML}`;
    let newjavascriptclick = Number(javascriptclick.innerHTML) + 1;
    console.log(`New JS ${newjavascriptclick}`);
  }
}

// wchodze na strone , sprawdzam czy jest cookie. jak nie ma to tworze cookie, jak jest to sprawdzam wartosc
// jak jest cookie, to nie przeładowuje ponownie strony; jak nie ma cookie to to przeladowuje

let formid = document.querySelector("#id_js_views").value;

if (formid % 2 == 0) {
  console.log("parzyste");
}
if (formid % 2 == 1) {
  console.log("nieparzyste");
} else {
  console.log("error");
}

formid = (formid * 1 + 1).toString();
document.querySelector("#id_js_views").setAttribute("value", formid);

// form.submit.click();

// ocument.addEventListener("DOMContentLoaded", function () {
//   let mojeCookie = document.cookie.split(";");
//   console.log(mojeCookie);
// });

const head = document.getElementsByTagName("head");
console.log(head[0]);

const odwiedziny = document.querySelector("#odwiedziny");
console.log(odwiedziny.innerHTML);

const myButton = document.querySelector("#myButton");

myButton.addEventListener("click", () => {
  const myScript = document.querySelector("#myScript");
  const copy = myScript.innerHTML;
  navigator.clipboard.writeText(copy);
  console.log(copy);
  document.querySelector("#myButton").textContent = "Copied";

  if (previous) {
    previous.textContent = "Copy";
  }
  previous = myButton;
});

window.addEventListener("DOMContentLoaded", () => {
  document.querySelector(
    "#myScript"
  ).innerText = ` <script> hujemu5hje \n user_id:  \n  </script> `;
});

let previous = null;
