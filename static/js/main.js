// NAVBAR SHADOW
window.addEventListener("scroll", () => {
  const navbar = document.querySelector(".navbar");
  if (navbar) {
    navbar.classList.toggle("shadow", window.scrollY > 50);
  }
});

// CATEGORY AUTO SCROLL

document.addEventListener("DOMContentLoaded", function () {

  const row = document.querySelector(".category-row");

  if (!row) return; 

  let speed = 2;
  let autoScroll;

  function startScroll() {
    if (window.innerWidth > 768) return;

    autoScroll = setInterval(() => {
      row.scrollLeft += speed;

      if (row.scrollLeft + row.clientWidth >= row.scrollWidth) {
        row.scrollLeft = 0;
      }
    }, 16);
  }

  function stopScroll() {
    clearInterval(autoScroll);
  }

  row.addEventListener("touchstart", stopScroll);
  row.addEventListener("touchend", startScroll);

  window.addEventListener("resize", () => {
    stopScroll();
    startScroll();
  });

  startScroll();
});

document.addEventListener("click", function (e) {
    if (e.target.classList.contains("attribute-btn")) {

        const group = e.target.closest(".attribute-options");
        const buttons = group.querySelectorAll(".attribute-btn");

        buttons.forEach(btn => btn.classList.remove("active"));
        e.target.classList.add("active");
    }
});

