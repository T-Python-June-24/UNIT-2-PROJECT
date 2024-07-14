function updateBannerText() {
    const inputText = document.getElementById('banner-text').value;
    const animatedText = document.getElementById('animated-text');
    animatedText.textContent = inputText;

    
    const textBanner = document.querySelector('.text-banner');
    textBanner.style.animation = 'none';
    textBanner.offsetHeight; 
    textBanner.style.animation = '';
}
