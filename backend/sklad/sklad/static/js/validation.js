// static/js/validation.js

document.addEventListener('DOMContentLoaded', function() {
    /* ============================
       (A) Проверка совпадения паролей
       ============================ */
    const hesloField = document.getElementById('id_heslo');
    const heslo2Field = document.getElementById('id_heslo_2');
    const heslo2Error = document.getElementById('error_id_heslo_2');
    const heslo2OkMark = document.getElementById('ok_id_heslo_2');
    const rentButton = document.getElementById('rent_button');

    // Запрещаем вставку во второе поле пароля
    heslo2Field.addEventListener('paste', function(e) {
        e.preventDefault();
    });

    function checkPasswordsMatch() {
        const pass1 = hesloField.value.trim();
        const pass2 = heslo2Field.value.trim();
        if (!pass2) {
            heslo2Error.textContent = "";
            heslo2Error.classList.remove('active');
            heslo2Field.classList.remove('invalid-input');
            heslo2OkMark.style.display = 'none';
        } else if (pass1 !== pass2) {
            heslo2Error.textContent = "Heslá sa nezhodujú. Použite rovnaké heslo, prosím.";
            heslo2Error.classList.add('active');
            heslo2Field.classList.add('invalid-input');
            heslo2OkMark.style.display = 'none';
        } else {
            heslo2Error.textContent = "";
            heslo2Error.classList.remove('active');
            heslo2Field.classList.remove('invalid-input');
            heslo2OkMark.style.display = 'inline';
        }
    }

    hesloField.addEventListener('input', checkPasswordsMatch);
    heslo2Field.addEventListener('input', checkPasswordsMatch);
    heslo2Field.addEventListener('blur', checkPasswordsMatch);

    /* ============================
       (B) Валидация полей на шаге 3
       ============================ */
    window.checkStep3Validity = function() {
        let valid = true;

        // 1) Проверка телефона (остаток номера)
        const phoneRestInput = document.getElementById('phone_rest');
        const phoneErrorSpan = document.getElementById('phone_error');
        const phoneVal = phoneRestInput.value.trim();
        if (!phoneVal) {
            phoneErrorSpan.textContent = "Telefónne číslo musí byť zadané";
            phoneErrorSpan.classList.add('active');
            phoneRestInput.classList.add('invalid-input');
            valid = false;
        } else if (phoneVal.startsWith('0')) {
            phoneErrorSpan.textContent = "Telefónne číslo nemôže začínať číslom 0";
            phoneErrorSpan.classList.add('active');
            phoneRestInput.classList.add('invalid-input');
            valid = false;
        } else {
            phoneErrorSpan.textContent = "";
            phoneErrorSpan.classList.remove('active');
            phoneRestInput.classList.remove('invalid-input');
        }

        // 2) Проверка email (если элемент существует)
        const emailField = document.getElementById('id_email');
        if (emailField) {
            const emailVal = emailField.value.trim();
            if (!emailVal.includes("@") || !emailVal.includes(".")) { 
                valid = false; 
            }
        }

        // 3) Проверка поля пароля
        const hesloVal = hesloField.value.trim();
        if (!hesloVal) {
            valid = false;
        }

        // 4) Проверка галочек (suhlas_kaucia и suhlas_zmluva)
        const suhlasKaucia = document.getElementById('id_suhlas_kaucia');
        const suhlasZmluva = document.getElementById('id_suhlas_zmluva');
        if (suhlasKaucia && !suhlasKaucia.checked) {
            valid = false;
        }
        if (suhlasZmluva && !suhlasZmluva.checked) {
            valid = false;
        }

        if (valid) {
            rentButton.removeAttribute('disabled');
        } else {
            rentButton.setAttribute('disabled', 'disabled');
        }
    };

    const suhlasKaucia = document.getElementById('id_suhlas_kaucia');
    const suhlasZmluva = document.getElementById('id_suhlas_zmluva');
    if (suhlasKaucia) {
        suhlasKaucia.addEventListener('change', function() {
            checkStep3Validity();
        });
    }
    if (suhlasZmluva) {
        suhlasZmluva.addEventListener('change', function() {
            checkStep3Validity();
        });
    }
});
