document.addEventListener('DOMContentLoaded', function () {
    const carouselSlide = document.querySelector('.carousel-slide');
    if (carouselSlide) {
        const carouselItems = document.querySelectorAll('.carousel-item');
        const totalItems = carouselItems.length;
        let currentIndex = 0;

        function moveToNextSlide() {
            currentIndex = (currentIndex + 1) % totalItems;
            updateCarousel();
        }

        function updateCarousel() {
            const offset = -currentIndex * 100; // Move 100% para cada item
            carouselSlide.style.transform = `translateX(${offset}%)`;
        }

        // Iniciar o carrossel automático a cada 5 segundos
        setInterval(moveToNextSlide, 5000);

        // Opcional: Adicionar botões de navegação se você os tiver no HTML
        // const prevBtn = document.querySelector('.carousel-prev-btn');
        // const nextBtn = document.querySelector('.carousel-next-btn');
        // if (prevBtn) {
        //     prevBtn.addEventListener('click', function() {
        //         currentIndex = (currentIndex - 1 + totalItems) % totalItems;
        //         updateCarousel();
        //     });
        // }
        // if (nextBtn) {
        //     nextBtn.addEventListener('click', function() {
        //         moveToNextSlide();
        //     });
        // }
    }
});