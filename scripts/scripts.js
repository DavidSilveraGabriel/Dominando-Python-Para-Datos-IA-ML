document.addEventListener('DOMContentLoaded', () => {
    const currentPath = window.location.pathname;
    const fileName = currentPath.substring(currentPath.lastIndexOf('/') + 1);
    let currentSlideNumber = parseInt(fileName.replace('.html', ''));

    // This should be dynamically determined or passed from a config
    const totalSlides = 7; // Assuming 7 slides in Modulo_00 for now

    function updateProgressBar() {
        const progressBar = document.querySelector('.progress-bar');
        if (progressBar) {
            const progress = (currentSlideNumber / totalSlides) * 100;
            progressBar.style.width = `${progress}%`;
        }
    }

    window.navigateSlide = (direction) => {
        let nextSlideNumber = currentSlideNumber + direction;

        if (nextSlideNumber < 1) {
            nextSlideNumber = 1; // Stay on the first slide
        } else if (nextSlideNumber > totalSlides) {
            nextSlideNumber = totalSlides; // Stay on the last slide
        }

        if (nextSlideNumber !== currentSlideNumber) {
            const newFileName = `${nextSlideNumber}.html`;
            const newPath = currentPath.replace(fileName, newFileName);
            window.location.href = newPath;
        }
    };

    updateProgressBar();
});
