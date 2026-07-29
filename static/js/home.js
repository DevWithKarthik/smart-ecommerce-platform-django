document.addEventListener("DOMContentLoaded", function () {

    /* ---------------------------------------------------------------
       Live countdown for the promo banner.
       Deadline is fixed the first time a visitor sees it (stored in
       localStorage) so the timer counts down consistently across
       reloads instead of resetting to "7 days" every refresh.
       --------------------------------------------------------------- */
    var promo = document.getElementById("scPromo");
    var countdownEl = document.getElementById("scCountdown");
    if (promo && countdownEl) {
        var days = parseInt(promo.getAttribute("data-countdown-days"), 10) || 7;
        var storageKey = "sc_promo_deadline";
        var deadline = parseInt(localStorage.getItem(storageKey), 10);

        if (!deadline || isNaN(deadline) || deadline < Date.now()) {
            deadline = Date.now() + days * 24 * 60 * 60 * 1000;
            localStorage.setItem(storageKey, String(deadline));
        }

        var dayEl = countdownEl.querySelector('[data-unit="days"]');
        var hourEl = countdownEl.querySelector('[data-unit="hours"]');
        var minEl = countdownEl.querySelector('[data-unit="minutes"]');
        var secEl = countdownEl.querySelector('[data-unit="seconds"]');

        var pad = function (n) { return String(n).padStart(2, "0"); };

        var tick = function () {
            var diff = Math.max(0, deadline - Date.now());
            var d = Math.floor(diff / 86400000);
            var h = Math.floor((diff % 86400000) / 3600000);
            var m = Math.floor((diff % 3600000) / 60000);
            var s = Math.floor((diff % 60000) / 1000);
            if (dayEl) dayEl.textContent = pad(d);
            if (hourEl) hourEl.textContent = pad(h);
            if (minEl) minEl.textContent = pad(m);
            if (secEl) secEl.textContent = pad(s);
            if (diff <= 0) clearInterval(timer);
        };

        tick();
        var timer = setInterval(tick, 1000);
    }

});