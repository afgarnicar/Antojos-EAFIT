document.addEventListener("DOMContentLoaded", function() {
    // Elementos del menú usuario
    const iconoUsuario = document.getElementById("icono-usuario");
    const menuUsuario = document.getElementById("menu-usuario");
    
    // Elementos del menú opciones
    const iconoMenu = document.getElementById("icono-menu");
    const menuOpciones = document.getElementById("menu-opciones");

    // Menú usuario
    if (iconoUsuario && menuUsuario) {
        iconoUsuario.addEventListener("click", function(event) {
            event.stopPropagation();
            menuUsuario.style.display = menuUsuario.style.display === "block" ? "none" : "block";
            // Cierra el otro menú
            if (menuOpciones) menuOpciones.style.display = "none";
        });
    }

    // Menú opciones
    if (iconoMenu && menuOpciones) {
        iconoMenu.addEventListener("click", function(event) {
            event.stopPropagation();
            menuOpciones.style.display = menuOpciones.style.display === "block" ? "none" : "block";
            // Cierra el otro menú
            if (menuUsuario) menuUsuario.style.display = "none";
        });
    }

    // Cerrar menús al hacer clic fuera
    document.addEventListener("click", function(event) {
        if (menuUsuario && !menuUsuario.contains(event.target) && event.target !== iconoUsuario) {
            menuUsuario.style.display = "none";
        }
        if (menuOpciones && !menuOpciones.contains(event.target) && event.target !== iconoMenu) {
            menuOpciones.style.display = "none";
        }
    });

    document.addEventListener("click", function(event) {
        // Para el menú usuario
        if (menuUsuario && !event.target.closest('.iconos-derecha')) {
            menuUsuario.style.display = "none";
        }
        
        // Para el menú opciones
        if (menuOpciones && !event.target.closest('.contenedor-izquierda')) {
            menuOpciones.style.display = "none";
        }
    });
});