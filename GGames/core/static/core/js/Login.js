document.addEventListener("DOMContentLoaded", function() {
    var loginForm = document.getElementById("loginForm");

    loginForm.addEventListener("submit", function(event) {
        event.preventDefault();

        var email = document.getElementById("email").value;
        var password = document.getElementById("pwd").value;

        var passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,12}$/;

        if (email.trim() === "" || password.trim() === "") {
            alert("Debes completar todos los campos.");
            return;
        }

        if (!passwordPattern.test(password)) {
            alert("La contraseña debe tener al menos una letra y un número, no debe contener espacios, y estar entre 8 y 12 caracteres.");
            return;
        }

        alert("Sesión iniciada correctamente");
        loginForm.submit();
    });
});
