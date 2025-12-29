document.addEventListener('DOMContentLoaded', function() {
    const slider = document.getElementById('categorySlider');
    const btnLeft = document.querySelector('.slider-btn-left');
    const btnRight = document.querySelector('.slider-btn-right');

    // عرض هر اسلاید (با احتساب فاصله)
    const slideWidth = 14 * 16 + 10; // 14rem + 10px gap (تقریبی)

    btnLeft.addEventListener('click', () => {
        slider.scrollBy({
            left: -slideWidth,
            behavior: 'smooth'
        });
    });

    btnRight.addEventListener('click', () => {
        slider.scrollBy({
            left: slideWidth,
            behavior: 'smooth'
        });
    });
});