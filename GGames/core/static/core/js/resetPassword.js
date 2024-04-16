function resetPassword() {
    var email = document.getElementById("email").value;
    if (email.trim() === "") {
        alert("Por favor, ingresa tu correo electrónico.");
    } else {
        alert("Se ha enviado un correo para restablecer tu contraseña a " + email);

        window.location.href = "login.html";
    }
}
