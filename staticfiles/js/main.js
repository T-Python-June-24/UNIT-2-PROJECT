// DOM Elements
const exploreBtn = document.getElementById("explore-btn");
const splineViewer = document.querySelector("spline-viewer");

// Constants
const GLOW_CIRCLES_LIMIT = 3;

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

// Initialization
const init = () => {
  setupExploreButton();
  removeSplineLogo();
};

// Run initialization when DOM is loaded
document.addEventListener("DOMContentLoaded", init);

// Toggle mobile menu
document.getElementById("menu-toggle").addEventListener("click", function () {
  document.getElementById("mobile-menu").classList.toggle("hidden");
});

// Dark mode toggle
function toggleDarkMode(isDarkMode) {
  setTimeout(() => {
    if (isDarkMode) {
      window.location.href = "/dark_mode/";
    } else {
      window.location.href = "/light_mode/";
    }
  }, 200); // 200ms delay
}
