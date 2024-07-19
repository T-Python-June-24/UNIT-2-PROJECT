// document.addEventListener("DOMContentLoaded", function () {
//   const navbar = document.getElementById("navbar");

//   window.addEventListener("scroll", function () {
//     if (window.scrollY > 50) {
//       navbar.classList.add("scrolled");
//     } else {
//       navbar.classList.remove("scrolled");
//     }
//   });

//   const lightModeButton = document.getElementById("light-mode-toggle");
//   const darkModeButton = document.getElementById("dark-mode-toggle");

//   function setLightMode() {
//     document.body.classList.remove("dark-mode");
//     lightModeButton.classList.add("active");
//     darkModeButton.classList.remove("active");
//   }

//   function setDarkMode() {
//     document.body.classList.add("dark-mode");
//     lightModeButton.classList.remove("active");
//     darkModeButton.classList.add("active");
//   }

//   lightModeButton.addEventListener("click", setLightMode);
//   darkModeButton.addEventListener("click", setDarkMode);

//   // Set initial mode based on the current body class
//   if (document.body.classList.contains("dark-mode")) {
//     setDarkMode();
//   } else {
//     setLightMode();
//   }
// });
document.addEventListener("scroll", function () {
  const navbar = document.querySelector(".navbar");
  if (window.scrollY > 700) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});

document.addEventListener("scroll", () => {
  const counters = document.querySelectorAll(".number");
  const speed = 100; 
  counters.forEach((counter) => {
    const updateCount = () => {
      const target = +counter.getAttribute("data-target");
      const count = +counter.innerText;

      const increment = target / speed;

      if (count < target) {
        counter.innerText = Math.ceil(count + increment);
        setTimeout(updateCount, 20);
      } else {
        counter.innerText = target;
      }
    };

    updateCount();
  });
});


let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  slides[slideIndex - 1].style.display = "block";
  setTimeout(showSlides, 5000); 
}