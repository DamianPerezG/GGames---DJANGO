function validarFormulario(event) {
    event.preventDefault();
    var email = document.getElementById("inputEmail4").value;
    var password = document.getElementById("inputPassword4").value;
    var direccion = document.getElementById("inputAddress").value;
    var otros = document.getElementById("inputAddress2").value;
    var ciudad = document.getElementById("inputCity").value;
    var region = document.getElementById("inputReg").value;
    var numCelular = document.getElementById("inputCel").value;

    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,12}$/;
    var celularPattern = /^\d{9}$/;

    if (email.trim() === "" || password.trim() === "" || direccion.trim() === "" || otros.trim() === "" ||
        ciudad.trim() === "" || region === "Choose..." || numCelular.trim() === "") {
        alert("Debes completar todos los campos.");
        return false;
    }

    if (!emailPattern.test(email)) {
        alert("El correo electrónico no tiene un formato válido.");
        return false;
    }

    if (!passwordPattern.test(password)) {
        alert("La contraseña debe tener al menos una letra, un número, no contener espacios, y estar entre 8 y 12 caracteres.");
        return false;
    }

    if (!celularPattern.test(numCelular)) {
        alert("El número de celular debe tener 9 dígitos.");
        return false;
    }

    if (!document.getElementById("gridCheck").checked) {
        alert("Debes aceptar los términos y condiciones.");
        return false;
    }

    return true;
}

document.getElementById("formularioRegistro").addEventListener("submit", validarFormulario);