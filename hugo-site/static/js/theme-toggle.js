(function () {
  const STORAGE_KEY = "site-theme";
  const html = document.documentElement;

  function applyTheme(theme) {
    if (theme === "dark" || theme === "light") {
      html.setAttribute("data-theme", theme);
    } else {
      html.removeAttribute("data-theme");
    }
  }

  // Read only the requested appearance preference; never write on page load.
  try {
    applyTheme(localStorage.getItem(STORAGE_KEY));
  } catch (_) {
    // Appearance controls still work when browser storage is unavailable.
  }

  document.addEventListener("DOMContentLoaded", function () {
    const button = document.querySelector(".theme-toggle");
    if (!button) return;

    button.addEventListener("click", function () {
      const current = html.getAttribute("data-theme") ||
        (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      const next = current === "dark" ? "light" : "dark";
      applyTheme(next);
      try {
        localStorage.setItem(STORAGE_KEY, next);
      } catch (_) {
        // The selected appearance remains usable for this page.
      }
    });
  });
})();
