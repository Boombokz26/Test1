// static/js/ui-components.js

document.addEventListener('DOMContentLoaded', function() {

    // Модальное окно для kaucie
    const kaucieLink = document.getElementById('kaucieLink');
    const kaucieModalOverlay = document.getElementById('kaucieModalOverlay');
    const kaucieModalClose = document.getElementById('kaucieModalClose');

    if (kaucieLink && kaucieModalOverlay && kaucieModalClose) {
        kaucieLink.addEventListener('click', function(event) {
            event.preventDefault();
            kaucieModalOverlay.style.display = 'block';
        });

        kaucieModalClose.addEventListener('click', function() {
            kaucieModalOverlay.style.display = 'none';
        });

        kaucieModalOverlay.addEventListener('click', function(event) {
            if (event.target === kaucieModalOverlay) {
                kaucieModalOverlay.style.display = 'none';
            }
        });
    }

    // Тултип для телефона (подсказка)
    const phoneInfoIcon = document.getElementById('phoneInfoIcon');
    const phoneTooltip = document.getElementById('phoneTooltip');

    if (phoneInfoIcon && phoneTooltip) {
        phoneInfoIcon.addEventListener('click', function() {
            if (phoneTooltip.style.display === 'block') {
                phoneTooltip.style.display = 'none';
            } else {
                phoneTooltip.style.display = 'block';
                // Позиционируем тултип относительно иконки
                const rect = phoneInfoIcon.getBoundingClientRect();
                phoneTooltip.style.position = 'absolute';
                phoneTooltip.style.left = rect.left + 'px';
                phoneTooltip.style.top = (rect.bottom + 5) + 'px';
            }
        });

        // Закрываем тултип при клике вне его
        document.addEventListener('click', function(ev) {
            if (ev.target !== phoneInfoIcon && !phoneTooltip.contains(ev.target)) {
                phoneTooltip.style.display = 'none';
            }
        });
    }
});
