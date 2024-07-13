// DOM Elements
const exploreBtn = document.getElementById("explore-btn");
const splineViewer = document.querySelector("spline-viewer");

// Constants
const GLOW_CIRCLES_LIMIT = 3;
const BLURRED_CIRCLES_COUNT = 5;

// Explore button animation
const setupExploreButton = () => {
  exploreBtn.addEventListener("mouseenter", () => {
    exploreBtn.style.transform = "scale(1.05)";
  });
  exploreBtn.addEventListener("mouseleave", () => {
    exploreBtn.style.transform = "scale(1)";
  });
};

// Glow effect
const glowContainer = document.createElement("div");
glowContainer.id = "glow-container";
document.body.appendChild(glowContainer);

const glowCircles = [];

const createGlowCircle = (x, y) => {
  const circle = document.createElement("div");
  circle.classList.add("glow-circle");
  circle.style.left = `${x - 100}px`;
  circle.style.top = `${y - 100}px`;
  glowContainer.appendChild(circle);
  glowCircles.push(circle);

  if (glowCircles.length > GLOW_CIRCLES_LIMIT) {
    const oldestCircle = glowCircles.shift();
    glowContainer.removeChild(oldestCircle);
  }
};

const setupGlowEffect = () => {
  document.addEventListener("mousemove", (e) => {
    createGlowCircle(e.clientX, e.clientY);
  });
};

// Blurred circles effect
const blurredCirclesContainer = document.createElement("div");
blurredCirclesContainer.id = "blurred-circles-container";
document.body.appendChild(blurredCirclesContainer);

const createBlurredCircle = () => {
  const circle = document.createElement("div");
  circle.classList.add("blurred-circle");

  const size = Math.random() * 200 + 100;
  const x = Math.random() * window.innerWidth;
  const y = Math.random() * window.innerHeight;

  circle.style.width = `${size}px`;
  circle.style.height = `${size}px`;
  circle.style.left = `${x}px`;
  circle.style.top = `${y}px`;

  const hue = Math.random() * 60 + 90; // Green to yellow hues
  const saturation = Math.random() * 30 + 70;
  const lightness = Math.random() * 20 + 40;
  circle.style.backgroundColor = `hsl(${hue}, ${saturation}%, ${lightness}%)`;

  blurredCirclesContainer.appendChild(circle);
};

const setupBlurredCircles = () => {
  for (let i = 0; i < BLURRED_CIRCLES_COUNT; i++) {
    createBlurredCircle();
  }
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
  setupGlowEffect();
  setupBlurredCircles();
  removeSplineLogo();
};


const glow = document.getElementById('glow');
   
document.addEventListener('mousemove', (e) => {
  glow.style.left = e.clientX - 100 + 'px';
  glow.style.top = e.clientY - 100 + 'px';
  glow.style.opacity = '1';
});

document.addEventListener('mouseout', () => {
  glow.style.opacity = '0';
});


// Run initialization when DOM is loaded
document.addEventListener("DOMContentLoaded", init);
