const btns = document.querySelectorAll(".btn");
const bodyHeader = document.querySelector("#body-top-header");
btns.forEach((btn) => {
  btn.addEventListener("click", () => {
    bodyHeader.scrollIntoView({
      behavior: "smooth",
    });
  });
});

// const paths = document.querySelectorAll(".name path");
// let i = 0;
// let speed = 50;

// paths.forEach(function (item, index) {
//   i++;
//   let pathLength = item.getTotalLength();
//   item.setAttribute("stroke-dasharray", pathLength);
//   item.setAttribute("stroke-dashoffset", pathLength);

//   if (index == 0) {
//     item.innerHTML = `<animate id=${
//       "a" + i
//     } attributeName='stroke-dashoffset' begin='0s' dur='3s' to='0' fill='freeze' />`;
//   } else {
//     item.innerHTML =
//       "<animate id='a" +
//       i +
//       "' attributeName='stroke-dashoffset' begin='a" +
//       (i - 1) +
//       ".end' dur='" +
//       pathLength / speed +
//       "' to='0' fill='freeze' />";
//   }

//   console.log(index, pathLength, item.innerHTML);
// });

// const logo = document.querySelectorAll("#logo path");

// for (let i = 0; i < logo.length; i++) {
//   console.log(`ID ${i} długość: ${logo[i].getTotalLength()}`);
// }

// const logos = document.querySelectorAll("#logo path");

// let i = 0;
// let speed = 350;
// logos.forEach(function (item, index) {
//   i++;
//   let pathLength = item.getTotalLength();
//   item.setAttribute("stroke-dasharray", pathLength);
//   item.setAttribute("stroke-dashoffset", pathLength);

//   if (index == 0) {
//     item.innerHTML = `<animate id=${
//       "a" + i
//     } attributeName='stroke-dashoffset' begin='0s' dur='${
//       pathLength / speed
//     }s' to='0' fill='freeze' />`;
//   } else {
//     item.innerHTML =
//       "<animate id='a" +
//       i +
//       "' attributeName='stroke-dashoffset' begin='a" +
//       (i - 1) +
//       ".end' dur='" +
//       pathLength / speed +
//       "' to='0' fill='freeze' />";
//   }
// });
