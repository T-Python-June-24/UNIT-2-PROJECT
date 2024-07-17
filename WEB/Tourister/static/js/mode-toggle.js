document.addEventListener('DOMContentLoaded', function () {
    const modeToggle = document.getElementById('mode-toggle');
    const body = document.body;

    // Check local storage for theme
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme) {
        body.classList.add(currentTheme);
        if (currentTheme === 'dark-mode') {
            modeToggle.textContent = '🌞';
        } else {
            modeToggle.textContent = '🌙';
        }
    }

    modeToggle.addEventListener('click', function () {
        if (body.classList.contains('light-mode')) {
            body.classList.remove('light-mode');
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark-mode');
            modeToggle.textContent = '🌞';
        } else {
            body.classList.remove('dark-mode');
            body.classList.add('light-mode');
            localStorage.setItem('theme', 'light-mode');
            modeToggle.textContent = '🌙';
        }
    });
});
