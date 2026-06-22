(function () {
  const STORAGE_KEY = "site-theme";
  const html = document.documentElement;

  function applyTheme(theme) {
    if (theme === "dark" || theme === "light") {
      html.setAttribute("data-theme", theme);
      localStorage.setItem(STORAGE_KEY, theme);
    } else {
      html.removeAttribute("data-theme");
      localStorage.removeItem(STORAGE_KEY);
    }
  }

  const savedTheme = localStorage.getItem(STORAGE_KEY);
  if (savedTheme) {
    applyTheme(savedTheme);
  }

  document.addEventListener("DOMContentLoaded", function () {
    const button = document.querySelector(".theme-toggle");
    if (!button) return;

    button.addEventListener("click", function () {
      const current = html.getAttribute("data-theme");

      if (current === "dark") {
        applyTheme("light");
      } else {
        applyTheme("dark");
      }
    });
  });
})();