document.addEventListener('DOMContentLoaded', function () {
    // Seleciona os elementos do carrossel no HTML
    const carouselContainer = document.querySelector('.carousel-container'); // Ajustado para .carousel-container
    const carouselSlide = document.querySelector('.carousel-slide');
    const carouselItems = document.querySelectorAll('.carousel-item');

    // Verifica se todos os elementos necessários foram encontrados para evitar erros
    if (!carouselContainer || !carouselSlide || carouselItems.length === 0) {
        console.error("Elementos do carrossel não encontrados. Verifique os nomes das classes HTML.");
        return; // Interrompe a execução do script se os elementos estiverem faltando
    }

    // Obtém a largura de um único item do carrossel. Assume que todos os itens têm a mesma largura.
    const itemWidth = carouselItems[0].offsetWidth;
    let currentIndex = 0; // Índice do slide atual, começando do primeiro (0)
    const visibleItems = 1; // Número de itens visíveis de cada vez (geralmente 1 para carrosséis de imagem)
    const scrollInterval = 3000; // Intervalo de tempo em milissegundos (3 segundos) para a rolagem automática

    /**
     * Move o carrossel para um item específico.
     * @param {number} index O índice do item para o qual o carrossel deve se mover.
     */
    function scrollToItem(index) {
        // Calcula a distância a ser movida para a esquerda (negativo)
        const translateX = -index * itemWidth;
        carouselSlide.style.transform = `translateX(${translateX}px)`;
        // Adiciona uma transição suave para o movimento
        carouselSlide.style.transition = 'transform 0.5s ease-in-out';
    }

    /**
     * Função para a rolagem automática do carrossel.
     */
    function autoScroll() {
        currentIndex++; // Avança para o próximo slide
        // Se o índice atual for maior ou igual ao número total de itens, volta para o primeiro slide (loop)
        if (currentIndex >= carouselItems.length) {
            currentIndex = 0;
        }
        scrollToItem(currentIndex); // Move o carrossel para o novo slide
        // Chama a função novamente após o intervalo definido para continuar a rolagem automática
        setTimeout(autoScroll, scrollInterval);
    }

    // Inicia a rolagem automática se houver mais itens do que os visíveis (para que o carrossel possa se mover)
    if (carouselItems.length > visibleItems) {
        setTimeout(autoScroll, scrollInterval);
    }

    // --- Estilos Básicos (Adicionados via JS para garantia, mas idealmente no CSS) ---
    // Estes estilos são importantes para o funcionamento do carrossel com Flexbox.
    // Se você já os tem no seu arquivo CSS, pode remover esta seção do JS.
    carouselSlide.style.display = 'flex'; // Garante que os itens fiquem em linha
    // Define a largura total da "pista" do carrossel para acomodar todos os itens lado a lado
    carouselSlide.style.width = `${carouselItems.length * itemWidth}px`;
    carouselItems.forEach(item => {
        item.style.flexShrink = 0; // Impede que os itens encolham
        item.style.width = `${itemWidth}px`; // Garante que cada item tenha a largura correta
    });
    carouselContainer.style.overflow = 'hidden'; // Oculta o conteúdo que excede a largura do contêiner
});