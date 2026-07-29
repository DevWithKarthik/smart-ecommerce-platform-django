document.addEventListener("DOMContentLoaded", function () {

    var qtyInput = document.getElementById("pdpQty");
    var minusBtn = document.getElementById("pdpQtyMinus");
    var plusBtn = document.getElementById("pdpQtyPlus");

    if (qtyInput && minusBtn && plusBtn) {
        minusBtn.addEventListener("click", function () {
            var val = parseInt(qtyInput.value, 10) || 1;
            qtyInput.value = Math.max(1, val - 1);
        });
        plusBtn.addEventListener("click", function () {
            var val = parseInt(qtyInput.value, 10) || 1;
            qtyInput.value = val + 1;
        });
    }

});