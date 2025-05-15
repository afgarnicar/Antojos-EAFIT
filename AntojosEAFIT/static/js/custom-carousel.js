$(document).ready(function() {
    console.log("Document ready");
    
    // Verificar si el elemento existe
    if ($(".recommended-carousel").length) {
        console.log("Carousel element found");
        
        try {
            $(".recommended-carousel").owlCarousel({
                loop: true,
                margin: 20,
                nav: true,
                dots: true,
                autoplay: true,
                autoplayTimeout: 5000,
                autoplayHoverPause: true,
                navText: [
                    "<i class='fas fa-chevron-left'></i>",
                    "<i class='fas fa-chevron-right'></i>"
                ],
                responsive: {
                    0: {
                        items: 1
                    },
                    576: {
                        items: 2
                    },
                    992: {
                        items: 3
                    }
                }
            });
            console.log("Carousel initialized successfully");
        } catch (error) {
            console.error("Error initializing carousel:", error);
        }
    } else {
        console.error("Carousel element not found");
    }
}); 