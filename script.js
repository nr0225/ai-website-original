const menu = document.getElementById("menu");
const toggle = document.querySelector(".nav-toggle");
const year = document.getElementById("year");

if (year) {
  year.textContent = new Date().getFullYear();
}

if (menu && toggle) {
  toggle.addEventListener("click", () => {
    const isOpen = menu.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(isOpen));
  });

  menu.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      menu.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
    }
  });
}
