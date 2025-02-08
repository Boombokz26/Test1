// static/js/date-limits.js

document.addEventListener("DOMContentLoaded", function () {
    // Установка ограничений для даты начала аренды склада
    const dateField = document.querySelector('#prenajat_sklad_od');
    if (dateField) {
        fetch('/validate-date-range/')
            .then(response => response.json())
            .then(data => {
                dateField.min = data.min_date;
                dateField.max = data.max_date;
                if (!dateField.value) {
                    dateField.value = data.min_date;
                }
            })
            .catch(error => {
                console.error('Ошибка при получении диапазона дат для prenajat_sklad_od:', error);
            });
    }

    // Установка ограничений для даты рождения
    const birthField = document.querySelector('#id_datum_narodenia');
    if (birthField) {
        fetch('/validate-birth-date-range/')
            .then(response => response.json())
            .then(data => {
                birthField.min = data.min_date;
                birthField.max = data.max_date;
            })
            .catch(error => {
                console.error('Ошибка при получении диапазона дат для id_datum_narodenia:', error);
            });
    }
});
