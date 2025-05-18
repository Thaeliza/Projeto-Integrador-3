document.addEventListener('DOMContentLoaded', function () {
    let slideIndex = 0;
    showSlides(slideIndex);

    function moveSlide(n) {
        showSlides(slideIndex += n);
    }

    function showSlides(n) {
        let slides = document.getElementsByClassName("carousel-item");
        if (n >= slides.length) { slideIndex = 0 }
        if (n < 0) { slideIndex = slides.length - 1 }
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        if (slides[slideIndex]) {
            slides[slideIndex].style.display = "block";
        }
    }

    function autoSlide() {
        moveSlide(1);
        setTimeout(autoSlide, 3000); // Muda a cada 3 segundos
    }

    document.querySelector('.prev').addEventListener('click', function () {
        moveSlide(-1);
    });

    document.querySelector('.next').addEventListener('click', function () {
        moveSlide(1);
    });

    autoSlide(); // Inicia a mudança automática
});
