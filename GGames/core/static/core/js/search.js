document.addEventListener("DOMContentLoaded", function() {
    var gameList = document.getElementById("gameList");
    var searchBar = document.getElementById("searchInput");

    // Ocultar la lista de juegos al inicio
    gameList.style.display = "none";

    searchBar.addEventListener("keyup", function() {
        var searchInput = searchBar.value.toUpperCase().trim();
        var gameItems = gameList.getElementsByTagName("li");

        if (searchInput === "") {
            // Si la búsqueda está vacía, ocultar la lista de juegos
            gameList.style.display = "none";
            // Restaurar la visibilidad de todos los elementos de la lista
            for (var i = 0; i < gameItems.length; i++) {
                gameItems[i].style.display = "block";
            }
        } else {
            // Filtrar y mostrar solo los juegos que coinciden con la búsqueda
            for (var i = 0; i < gameItems.length; i++) {
                var gameName = gameItems[i].textContent || gameItems[i].innerText;
                if (gameName.toUpperCase().includes(searchInput)) {
                    gameItems[i].style.display = "block";
                } else {
                    gameItems[i].style.display = "none";
                }
            }

            // Mostrar la lista de juegos debajo de la barra de búsqueda
            gameList.style.display = "block";
            searchBar.parentNode.appendChild(gameList); // Mover la lista debajo de la barra de búsqueda
        }
    });
});
