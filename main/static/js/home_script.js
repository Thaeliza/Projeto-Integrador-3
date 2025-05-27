// seu_app/static/js/home_scripts.js

document.addEventListener('DOMContentLoaded', () => {

    // Função genérica para configurar carrosséis baseados em flexbox
    function setupFlexCarousel(containerSelector, trackSelector, prevBtnSelector, nextBtnSelector, autoPlay = false, intervalTime = 3000) {
        const carouselContainer = document.querySelector(containerSelector);
        if (!carouselContainer) {
            // console.warn(`Carrossel '${containerSelector}' não encontrado.`);
            return;
        }

        const carouselTrack = carouselContainer.querySelector(trackSelector);
        const cardWrappers = Array.from(carouselTrack.children); // Converte para Array para usar métodos de array

        if (cardWrappers.length === 0) {
            // console.warn(`Nenhum item encontrado para o carrossel '${containerSelector}'.`);
            return;
        }

        const prevBtn = carouselContainer.querySelector(prevBtnSelector);
        const nextBtn = carouselContainer.querySelector(nextBtnSelector);

        let currentIndex = 0;
        let cardsPerView = 3; // Padrão para desktop, ajustado via CSS @media queries ou cálculo dinâmico

        // Calcula a largura do slide baseada nos itens visíveis
        function getSlideWidth() {
            if (cardWrappers.length === 0) return 0;
            // Para flexbox, é mais fácil calcular a largura do contêiner visível e dividir pelo número de itens
            const trackWidth = carouselTrack.offsetWidth; // Largura visível do track
            return trackWidth / cardsPerView; // Largura que cada item deve ocupar
        }

        // Função para atualizar cardsPerView com base na largura da janela
        function updateCardsPerViewOnResize() {
            if (window.innerWidth <= 480) {
                cardsPerView = 1;
            } else if (window.innerWidth <= 768) {
                cardsPerView = 2;
            } else {
                cardsPerView = 3;
            }
            updateCarouselPosition(); // Atualiza a posição ao redimensionar
            updateButtonsState(); // Atualiza o estado dos botões
        }

        // Atualiza a posição do carrossel
        function updateCarouselPosition() {
            // A largura total de um "bloco" de movimento (1 item + seu padding)
            // Calculamos a largura do primeiro card e seu padding-right
            const firstCard = cardWrappers[0];
            const cardComputedStyle = window.getComputedStyle(firstCard);
            const cardMarginRight = parseFloat(cardComputedStyle.marginRight) || 0; // Se tiver margem
            const cardWidth = firstCard.offsetWidth + cardMarginRight; // Largura real do item + margem

            // A translação é baseada no currentIndex e na largura de cada card
            const offset = -currentIndex * cardWidth;
            carouselTrack.style.transition = 'transform 0.5s ease-in-out';
            carouselTrack.style.transform = `translateX(${offset}px)`;
        }

        // Atualiza o estado dos botões (habilitado/desabilitado)
        function updateButtonsState() {
            if (prevBtn) prevBtn.disabled = currentIndex === 0;
            if (nextBtn) nextBtn.disabled = currentIndex >= cardWrappers.length - cardsPerView;
        }

        // Event Listeners para botões
        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                if (currentIndex > 0) {
                    currentIndex--;
                    updateCarouselPosition();
                    updateButtonsState();
                }
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                // Checa se ainda há cards para mostrar
                if (currentIndex < cardWrappers.length - cardsPerView) {
                    currentIndex++;
                    updateCarouselPosition();
                    updateButtonsState();
                }
            });
        }

        // Auto-play (opcional)
        let autoPlayInterval;
        function startAutoPlay() {
            if (autoPlay) {
                autoPlayInterval = setInterval(() => {
                    if (currentIndex < cardWrappers.length - cardsPerView) {
                        currentIndex++;
                    } else {
                        currentIndex = 0; // Volta ao início para loop
                    }
                    updateCarouselPosition();
                    updateButtonsState();
                }, intervalTime);
            }
        }

        function stopAutoPlay() {
            clearInterval(autoPlayInterval);
        }

        // Inicia e para auto-play ao passar o mouse
        if (autoPlay) {
            carouselContainer.addEventListener('mouseenter', stopAutoPlay);
            carouselContainer.addEventListener('mouseleave', startAutoPlay);
        }


        // Inicializa carrossel
        updateCardsPerViewOnResize(); // Define o número de cards por vista e a posição inicial
        updateCarouselPosition(); // Posiciona o carrossel no carregamento
        updateButtonsState(); // Define o estado inicial dos botões
        startAutoPlay(); // Inicia o auto-play se configurado

        // Adiciona listener para redimensionamento da janela
        window.addEventListener('resize', updateCardsPerViewOnResize);
    }

    // Configura o carrossel de Notícias (ativado com auto-play)
    setupFlexCarousel('.carousel-container2', '.carousel-track2', '.carousel-prev-btn2', '.carousel-next-btn2', true, 4000); // 4 segundos

    // Configura o carrossel de Depoimentos (ativado com auto-play)
    setupFlexCarousel('.carousel-container3', '.carousel-track3', '.carousel-prev-btn3', '.carousel-next-btn3', true, 5000); // 5 segundos
});