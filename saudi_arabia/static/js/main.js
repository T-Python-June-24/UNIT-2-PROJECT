// DOM Elements
const exploreBtn = document.getElementById("explore-btn");
const splineViewer = document.querySelector("spline-viewer");

// Explore button animation
const setupExploreButton = () => {
  exploreBtn.addEventListener("mouseenter", () => {
    exploreBtn.style.transform = "scale(1.05)";
  });
  exploreBtn.addEventListener("mouseleave", () => {
    exploreBtn.style.transform = "scale(1)";
  });
};

// Remove Spline logo
const removeSplineLogo = () => {
  if (splineViewer && splineViewer.shadowRoot) {
    const logo = splineViewer.shadowRoot.querySelector("#logo");
    if (logo) {
      logo.remove();
    }
  }
};




document
  .getElementById("menu-toggle")
  .addEventListener("click", function () {
    const mobileMenu = document.getElementById("mobile-menu");
    const menuToggle = this.querySelector("svg");

    mobileMenu.classList.toggle("show");
    menuToggle.style.transform = mobileMenu.classList.contains("show")
      ? "rotate(45deg)"
      : "rotate(0deg)";
  });

function createGlowEffects() {
  const container = document.getElementById("blurred-circles-container");
  const colors = ["#4ecdc4", "#45aaf2", "#7ed56f", "#2ecc71", "#16a085"];

  for (let i = 0; i < 10; i++) {
    const circle = document.createElement("div");
    circle.classList.add("blurred-circle");
    circle.style.width = `${Math.random() * 300 + 100}px`;
    circle.style.height = circle.style.width;
    circle.style.backgroundColor =
      colors[Math.floor(Math.random() * colors.length)];
    circle.style.left = `${Math.random() * 100}%`;
    circle.style.top = `${Math.random() * 100}%`;

    container.appendChild(circle);

    animateCircle(circle);
  }
}

function animateCircle(circle) {
  const xDistance = Math.random() * 400 - 100;
  const yDistance = Math.random() * 400 - 100;

  gsap.to(circle, {
    x: xDistance,
    y: yDistance,
    duration: 3,
    ease: "sine.inOut",
    repeat: -1,
    yoyo: true,
  });
}

createGlowEffects();
// Initialization
const init = () => {
  setupExploreButton();
  removeSplineLogo();
  createGlowEffects();
};

// Run initialization when DOM is loaded
document.addEventListener("DOMContentLoaded", init);


