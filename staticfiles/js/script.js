document.addEventListener('DOMContentLoaded', function () {
    const carouselContainer = document.querySelector('.carousel-container');
    const carouselTrack = document.querySelector('.carousel-track');
    const cardsWrapper = document.querySelectorAll('.card-wrapper');
    const cardWidth = cardsWrapper[0].offsetWidth;
    let currentIndex = 0;
    const visibleCards = 3; // Número de cards visíveis
    const scrollInterval = 3000; // Intervalo de tempo em milissegundos (3 segundos)

    function scrollToCard(index) {
        const translateX = -index * cardWidth;
        carouselTrack.style.transform = `translateX(${translateX}px)`;
    }

    function autoScroll() {
        currentIndex++;
        if (currentIndex > cardsWrapper.length - visibleCards) {
            currentIndex = 0; // Voltar ao início quando chegar ao fim
        }
        scrollToCard(currentIndex);
        setTimeout(autoScroll, scrollInterval);
    }

    // Iniciar a rolagem automática
    if (cardsWrapper.length > visibleCards) {
        setTimeout(autoScroll, scrollInterval);
    }
});