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

document.addEventListener("DOMContentLoaded", function () {

  /* ---------------------------------------------------------------
     Sticky navbar shadow on scroll
     --------------------------------------------------------------- */
  var navbar = document.getElementById("scNavbar");
  if (navbar) {
    var toggleNavbarShadow = function () { navbar.classList.toggle("is-scrolled", window.scrollY > 12); };
    toggleNavbarShadow();
    window.addEventListener("scroll", toggleNavbarShadow, { passive: true });
  }

  /* ---------------------------------------------------------------
     Back-to-top button
     --------------------------------------------------------------- */
  var backTop = document.getElementById("scBackTop");
  if (backTop) {
    var toggleBackTop = function () { backTop.classList.toggle("is-visible", window.scrollY > 500); };
    toggleBackTop();
    window.addEventListener("scroll", toggleBackTop, { passive: true });
    backTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });
  }

  /* ---------------------------------------------------------------
     Scroll-reveal animation via IntersectionObserver
     --------------------------------------------------------------- */
  var revealEls = document.querySelectorAll(".sc-reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("is-visible"); observer.unobserve(entry.target); }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ---------------------------------------------------------------
     Button ripple effect
     --------------------------------------------------------------- */
  document.querySelectorAll("[data-ripple]").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      var rect = btn.getBoundingClientRect();
      var ripple = document.createElement("span");
      var size = Math.max(rect.width, rect.height);
      ripple.className = "sc-ripple";
      ripple.style.width = ripple.style.height = size + "px";
      ripple.style.left = (e.clientX - rect.left - size / 2) + "px";
      ripple.style.top = (e.clientY - rect.top - size / 2) + "px";
      btn.appendChild(ripple);
      setTimeout(function () { ripple.remove(); }, 650);
    });
  });

  /* ---------------------------------------------------------------
     Wishlist toggle (visual only — wire to a real endpoint later)
     --------------------------------------------------------------- */
  document.querySelectorAll("[data-wishlist-btn]").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      btn.classList.toggle("active");
      var icon = btn.querySelector("i");
      if (icon) { icon.classList.toggle("bi-heart"); icon.classList.toggle("bi-heart-fill"); }
    });
  });

  /* ---------------------------------------------------------------
     Add-to-cart micro feedback for DECORATIVE buttons only
     (type="button", no form). The real PDP add-to-cart button is a
     type="submit" inside an actual form and must NOT be intercepted.
     --------------------------------------------------------------- */
  document.querySelectorAll('button.sc-add-cart-btn[type="button"]').forEach(function (btn) {
    btn.addEventListener("click", function () {
      var original = btn.innerHTML;
      btn.innerHTML = '<i class="bi bi-check2"></i> Added';
      btn.disabled = true;
      setTimeout(function () { btn.innerHTML = original; btn.disabled = false; }, 1200);
    });
  });

});