document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".color-hex-input").forEach(function (hexInput) {
        const colorInput = hexInput.parentElement.querySelector(".color-picker-input");

        // HEX → picker
        hexInput.addEventListener("input", function () {
            if (/^#[0-9A-Fa-f]{6}$/.test(hexInput.value)) {
                colorInput.value = hexInput.value;
            }
        });

        // picker → HEX
        colorInput.addEventListener("input", function () {
            hexInput.value = colorInput.value;
        });
    });
});
