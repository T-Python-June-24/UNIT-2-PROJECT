if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  document.documentElement.classList.add('dark')
} else {
  document.documentElement.classList.remove('dark')
}

const themeToggleOn = document.getElementById('theme-toggle-on');
    const themeToggleOff = document.getElementById('theme-toggle-off');

    function updateToggleButton() {
      if (document.documentElement.classList.contains('dark')) {
        themeToggleOn.classList.add('hidden');
        themeToggleOff.classList.remove('hidden');
      } else {
        themeToggleOn.classList.remove('hidden');
        themeToggleOff.classList.add('hidden');
      }
    }

    themeToggleOn.addEventListener('click', () => {
      document.documentElement.classList.add('dark');
      localStorage.theme = 'dark';
      updateToggleButton();
    });

    themeToggleOff.addEventListener('click', () => {
      document.documentElement.classList.remove('dark');
      localStorage.theme = 'light';
      updateToggleButton();
    });

    updateToggleButton();