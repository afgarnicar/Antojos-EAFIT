document.addEventListener("DOMContentLoaded", function() {
    const iconoUsuario = document.getElementById("icono-usuario");
    const menuUsuario = document.getElementById("menu-usuario");
    const contenedorUsuario = document.getElementById("contenedor-usuario")

    iconoUsuario.addEventListener("click", function(event) {
        event.stopPropagation();
        menuUsuario.style.display = menuUsuario.style.display === "block" ? "none" : "block";
    });

    document.addEventListener("click", function (event) {
        if(!menuUsuario.contains(event.target) && event.target !== iconoUsuario){
            menuUsuario.style.display = "none";
        }
    });

    document.addEventListener("click", function (event) {
        if(!contenedorUsuario.contains(event.target)){
            contenedorUsuario.style.display = "none";
        }
    });
});