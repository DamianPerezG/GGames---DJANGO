function actualizarDatos() {
    var mensajeBox = document.getElementById("mensajeBox");
    mensajeBox.style.display = "block";
    window.location.href = "{% url 'index' %}";
}

function volverInicio() {
    window.location.href = "{% url 'index' %}";
}
