// static/js/step-navigation.js

document.addEventListener('DOMContentLoaded', function() {

    // Получаем элементы шагов
    const step1 = document.getElementById('step1');
    const step2 = document.getElementById('step2');
    const step3 = document.getElementById('step3');

    // Получаем элементы индикаторов шагов (прогресс-бар)
    const stepIndicator1 = document.getElementById('stepIndicator1');
    const stepIndicator2 = document.getElementById('stepIndicator2');
    const stepIndicator3 = document.getElementById('stepIndicator3');

    // Читаем текущее значение шага из скрытого поля
    const currentStepInput = document.getElementById('current_step');
    let currentStepVal = parseInt(currentStepInput.value, 10) || 1;

    // Функция для показа указанного шага
    function showStep(stepNumber) {
        // Скрываем все шаги
        step1.classList.add('hidden');
        step2.classList.add('hidden');
        step3.classList.add('hidden');
        // Снимаем активное состояние с индикаторов
        stepIndicator1.classList.remove('active');
        stepIndicator2.classList.remove('active');
        stepIndicator3.classList.remove('active');

        // Показываем нужный шаг и устанавливаем активный индикатор
        if (stepNumber === 1) {
            step1.classList.remove('hidden');
            stepIndicator1.classList.add('active');
        } else if (stepNumber === 2) {
            step2.classList.remove('hidden');
            stepIndicator2.classList.add('active');
        } else if (stepNumber === 3) {
            step3.classList.remove('hidden');
            stepIndicator3.classList.add('active');
        }
        // Обновляем значение текущего шага в скрытом поле
        currentStepInput.value = stepNumber.toString();
        currentStepVal = stepNumber;
    }

    // Назначаем обработчики для кнопок перехода между шагами
    const btnStep1Next = document.getElementById('btnStep1Next');
    const btnStep2Back = document.getElementById('btnStep2Back');
    const btnStep2Next = document.getElementById('btnStep2Next');
    const btnStep3Back = document.getElementById('btnStep3Back');

    btnStep1Next.addEventListener('click', function() {
        if (typeof validateStep1 === 'function') {
            if (validateStep1()) {
                showStep(2);
            }
        } else {
            showStep(2);
        }
    });

    btnStep2Back.addEventListener('click', function() {
        showStep(1);
    });

    btnStep2Next.addEventListener('click', function() {
        if (typeof validateStep2 === 'function') {
            if (validateStep2()) {
                if (typeof autoSetPhoneCodeByCountry === 'function') {
                    autoSetPhoneCodeByCountry();
                }
                showStep(3);
                if (typeof checkStep3Validity === 'function') {
                    checkStep3Validity();
                }
            }
        } else {
            showStep(3);
        }
    });

    btnStep3Back.addEventListener('click', function() {
        showStep(2);
    });

    // При загрузке страницы устанавливаем видимость текущего шага
    showStep(currentStepVal);

    // --- Добавляем функцию updateVisibility для управления видимостью полей (шаг 2) ---
    function updateVisibility() {
        const pravneVal = pravneSelect.value || "";
        if (pravneVal === "Fyzická osoba") {
            fyzickaFields.classList.remove('hidden');
            pravnickaFields.classList.add('hidden');
            dphInfo.classList.add('hidden');
            setDatumNarodeniaRequired(true);
        } else if (pravneVal === "Právnická osoba (bez DPH)" || pravneVal === "Právnická osoba (platca DPH)") {
            pravnickaFields.classList.remove('hidden');
            fyzickaFields.classList.add('hidden');
            if (pravneVal === "Právnická osoba (platca DPH)") {
                dphInfo.classList.remove('hidden');
                icDphBlock.classList.remove('hidden');
            } else {
                dphInfo.classList.add('hidden');
                icDphBlock.classList.add('hidden');
            }
            setDatumNarodeniaRequired(false);
        } else {
            fyzickaFields.classList.add('hidden');
            pravnickaFields.classList.add('hidden');
            dphInfo.classList.add('hidden');
            setDatumNarodeniaRequired(false);
        }
    }
    // Делаем updateVisibility глобально доступной
    window.updateVisibility = updateVisibility;
});
