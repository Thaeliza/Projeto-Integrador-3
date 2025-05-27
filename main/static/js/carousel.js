// seu_app/static/js/carousel.js

document.addEventListener('DOMContentLoaded', () => {
    const carouselSlide = document.querySelector('.carousel-slide');
    const carouselItems = document.querySelectorAll('.carousel-slide .carousel-item');

    if (!carouselSlide || carouselItems.length === 0) {
        console.warn('Carrossel principal não encontrado ou sem itens para inicializar. (Este console.warn é normal se o carrossel não estiver presente)');
        return;
    }

    let currentIndex = 0;
    // Garante que pelo menos um item exista para pegar a largura
    const itemWidth = carouselItems.length > 0 ? carouselItems[0].offsetWidth : 0;

    // Se houver itens, adicione clones para um loop suave
    if (carouselItems.length > 0) {
        const firstClone = carouselItems[0].cloneNode(true);
        const lastClone = carouselItems[carouselItems.length - 1].cloneNode(true);

        carouselSlide.appendChild(firstClone);
        carouselSlide.insertBefore(lastClone, carouselItems[0]);

        // Ajusta o índice inicial para o primeiro item real (após o clone do último)
        // Isso coloca o carrossel na posição do primeiro item original
        carouselSlide.style.transform = `translateX(${-itemWidth}px)`;
        carouselSlide.style.transition = 'none'; // Desativa transição para o ajuste inicial
    }

    let intervalId;

    function moveToNextSlide() {
        currentIndex++;
        // Re-habilita transição antes de mover
        carouselSlide.style.transition = 'transform 0.5s ease-in-out';
        carouselSlide.style.transform = `translateX(${-itemWidth * (currentIndex + 1)}px)`;

        // Detecta o fim do carrossel para resetar para o início clonado
        // (A transição para o clone ocorre, depois o reset rápido para o item original)
        if (currentIndex >= carouselItems.length) {
            setTimeout(() => {
                carouselSlide.style.transition = 'none'; // Desativa transição para reset
                currentIndex = 0; // Volta para o primeiro item original
                carouselSlide.style.transform = `translateX(${-itemWidth}px)`;
            }, 500); // Tempo correspondente à transição em CSS (0.5s)
        }
    }

    // Inicia a troca automática
    function startAutoSlide() {
        intervalId = setInterval(moveToNextSlide, 3000); // Muda o slide a cada 3 segundos
    }

    // Para a troca automática ao passar o mouse
    carouselSlide.addEventListener('mouseenter', () => clearInterval(intervalId));
    carouselSlide.addEventListener('mouseleave', startAutoSlide);

    // Inicia o carrossel quando o DOM estiver carregado
    startAutoSlide();
});