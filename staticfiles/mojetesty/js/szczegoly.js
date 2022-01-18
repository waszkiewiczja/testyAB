console.log("jazda");

let losowa = Math.round(Math.random());

window.addEventListener("DOMContentLoaded", () => {
  const user = document.querySelector("#user");
  const iduser = document.querySelector("#iduser");
  const idtest = document.querySelector("#idtest");
  const link1 = document.querySelector("#link1");
  console.log(link1);
  console.log(typeof link1.innerText);
  const link2 = document.querySelector("#link2");
  const links = [link1.innerText, link2.innerText];
  console.log(links);

  document.querySelector("#myScript").innerText = ` <script> 
  \n let random = Math.round(Math.random());
  \n let links = ['${link1.innerHTML}', '${link2.innerHTML}'];
  \n user_id=${iduser.innerHTML};
  \n test_id=${idtest.innerHTML};
  \n
  if (random == 0) {
  \t } else {
    window.location.href = links[1];
  }

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(
            cookie.substring(name.length + 1)
          );
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie("csrftoken");

  window.addEventListener("DOMContentLoaded", () => {
    fetch("http://127.0.0.1:8000/dotestow/api/tests/1/dodaj/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({ js_views: 1 }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("skuces");
      })
      .catch((err) => {
        console.log(err);
      });
  });

  \n</script> `;
});

const myButton = document.querySelector("#myButton");
let previous = null;

myButton.addEventListener("click", () => {
  const myInput = document.querySelector("#myScript");
  const copy = myInput.innerText;
  console.log(copy);
  navigator.clipboard.writeText(copy);
  document.querySelector("#myButton").textContent = "Skopiowano";

  if (previous) {
    previous.textContent = "Copy";
  }
  previous = myButton;
});

/**
 * Auto-indent overflowing lines
 * @author Rob W http://stackoverflow.com/u/938089
 * @param code_elem HTMLCodeElement (or any element containing *plain text*)
 */
function autoindent(code_elem) {
  // Grab the lines
  var textContent = document.textContent === null ? "textContent" : "innerText";
  var lines = code_elem[textContent].split(/\r?\n/),
    fragment = document.createDocumentFragment(),
    dummy,
    space_width,
    i,
    prefix_len,
    line_elem;

  // Calculate the width of white space
  // Assume that inline element inherit styles from parent (<code>)
  dummy = document.createElement("span");
  code_elem.appendChild(dummy);
  // offsetWidth includes padding and border, explicitly override the style:
  dummy.style.cssText = "border:0;padding:0;";
  dummy[textContent] = " ";
  space_width = dummy.offsetWidth;
  // Wipe contents
  code_elem.innerHTML = "";

  for (i = 0; i < lines.length; i++) {
    // NOTE: All preceeding white space (including tabs is included)
    prefix_len = /^\s*/.exec(lines[i])[0].length;
    line_elem = fragment.appendChild(document.createElement("div"));
    line_elem.style.marginLeft = space_width * prefix_len + "px";
    line_elem[textContent] = lines[i].substring(prefix_len);
  }
  // Finally, append (all elements inside) the fragment:
  code_elem.appendChild(fragment);
}
