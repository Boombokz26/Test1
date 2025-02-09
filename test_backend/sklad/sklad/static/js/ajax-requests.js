// static/js/ajax-requests.js

// Вспомогательная функция: восстанавливает выбранную опцию в элементе select
function restoreSelectedOption(selectEl, val) {
    let found = false;
    for (let i = 0; i < selectEl.options.length; i++) {
        if (selectEl.options[i].value === val) {
            selectEl.selectedIndex = i;
            found = true;
            break;
        }
    }
    if (!found && selectEl.options.length > 0) {
        selectEl.selectedIndex = 0;
    }
}

// Функция для загрузки "lokalita" на основе выбранного "typ_skladu"
function loadLokalita(autoNext = true) {
    const typSkladu = document.querySelector('#id_typ_skladu');
    const lokalita = document.querySelector('#id_lokalita');
    const velkost = document.querySelector('#id_velkost_skladu');
    const cislo = document.querySelector('#id_cislo_skladu');
    const dobaContainer = document.getElementById('doba_container');

    const currentLocVal = lokalita.value;
    fetch(`/ajax/lokalita/?typ_skladu=${typSkladu.value}`)
        .then(r => r.json())
        .then(data => {
            lokalita.innerHTML = '';
            if (data.length > 0) {
                data.forEach(val => {
                    const opt = document.createElement('option');
                    opt.value = val;
                    opt.textContent = val;
                    lokalita.appendChild(opt);
                });
                restoreSelectedOption(lokalita, currentLocVal);
                if (autoNext) loadVelkost(true);
            }
        });
}

// Функция для загрузки "velkost_skladu" на основе "typ_skladu" и "lokalita"
function loadVelkost(autoNext = true) {
    const typSkladu = document.querySelector('#id_typ_skladu');
    const lokalita = document.querySelector('#id_lokalita');
    const velkost = document.querySelector('#id_velkost_skladu');
    const cislo = document.querySelector('#id_cislo_skladu');
    const dobaContainer = document.getElementById('doba_container');

    const currentVelVal = velkost.value;
    fetch(`/ajax/velkost/?typ_skladu=${typSkladu.value}&lokalita=${lokalita.value}`)
        .then(r => r.json())
        .then(data => {
            velkost.innerHTML = '';
            if (data.length > 0) {
                data.forEach(val => {
                    const opt = document.createElement('option');
                    opt.value = val;
                    opt.textContent = val;
                    velkost.appendChild(opt);
                });
                restoreSelectedOption(velkost, currentVelVal);
                if (autoNext) loadCislo(true);
            } else {
                velkost.innerHTML = '<option value="">(empty)</option>';
                cislo.innerHTML = '<option value="">(empty)</option>';
                dobaContainer.innerHTML = '';
            }
            if (typeof updateVisibility === "function") {
                updateVisibility();
            }
        });
}

// Функция для загрузки "cislo_skladu" на основе "typ_skladu", "lokalita" и "velkost_skladu"
function loadCislo(autoNext = true) {
    const typSkladu = document.querySelector('#id_typ_skladu');
    const lokalita = document.querySelector('#id_lokalita');
    const velkost = document.querySelector('#id_velkost_skladu');
    const cislo = document.querySelector('#id_cislo_skladu');
    const dobaContainer = document.getElementById('doba_container');

    const currentCisloVal = cislo.value;
    fetch(`/ajax/cislo_skladu/?typ_skladu=${typSkladu.value}&lokalita=${lokalita.value}&velkost_skladu=${velkost.value}`)
        .then(r => r.json())
        .then(data => {
            cislo.innerHTML = '';
            if (data.length > 0) {
                data.forEach(val => {
                    const opt = document.createElement('option');
                    opt.value = val;
                    opt.textContent = val;
                    cislo.appendChild(opt);
                });
                restoreSelectedOption(cislo, currentCisloVal);
                if (autoNext) loadDobaPrenajmu();
            } else {
                cislo.innerHTML = '<option value="">(empty)</option>';
                dobaContainer.innerHTML = '';
            }
            if (typeof updateVisibility === "function") {
                updateVisibility();
            }
            showSkladInfo();
        });
}

// Функция для загрузки вариантов "doba_prenajmu" на основе выбранного "cislo_skladu"
function loadDobaPrenajmu() {
    const cislo = document.querySelector('#id_cislo_skladu');
    const dobaContainer = document.getElementById('doba_container');

    fetch(`/ajax/doba_prenajmu/?cislo_skladu=${cislo.value}`)
        .then(r => r.json())
        .then(data => {
            dobaContainer.innerHTML = '';
            if (data.length > 0) {
                data.forEach((item, index) => {
                    const label = document.createElement('label');
                    label.className = 'doba-option';
                    label.style.position = 'relative';

                    const radio = document.createElement('input');
                    radio.type = 'radio';
                    radio.name = 'doba_prenajmu';
                    radio.value = item.value;
                    if (index === 0) radio.checked = true;
                    label.appendChild(radio);

                    const match = item.text.match(/^(.*?)\s*\((.*)\)\s*$/);
                    if (match) {
                        const topLine = match[1].trim();
                        const secondLine = '(' + match[2].trim() + ')';
                        label.appendChild(document.createTextNode(topLine));
                        label.appendChild(document.createElement('br'));
                        label.appendChild(document.createTextNode(secondLine));
                    } else {
                        label.appendChild(document.createTextNode(item.text));
                    }

                    let stickerText = '';
                    if (item.value === '6mes') {
                        stickerText = '⭐️ Populárne';
                    } else if (item.value === '12mes') {
                        stickerText = '🔥 Výhodné';
                    }

                    if (stickerText) {
                        const sticker = document.createElement('span');
                        sticker.className = 'sticker-badge';
                        sticker.textContent = stickerText;
                        if (item.value === '6mes') {
                            sticker.classList.add('badge-popular');
                        } else if (item.value === '12mes') {
                            sticker.classList.add('badge-vyhodne');
                        }
                        label.appendChild(sticker);
                    }

                    dobaContainer.appendChild(label);
                    if (item.value === '3mes') {
                        dobaContainer.appendChild(document.createElement('br'));
                    }
                });
            } else {
                dobaContainer.textContent = "Žiadne možnosti.";
            }
            if (typeof updateVisibility === "function") {
                updateVisibility();
            }
        });
}

// Функция для отображения информации о sklade (plocha, poschodie) и фотографиях
function showSkladInfo() {
    const cislo = document.querySelector('#id_cislo_skladu');
    const skladInfoSpan = document.getElementById('sklad_info_span');
    const skladFotoMain = document.getElementById('sklad_foto_main');
    const skladFotoExtra1 = document.getElementById('sklad_foto_extra1');
    const skladFotoExtra2 = document.getElementById('sklad_foto_extra2');

    const cVal = cislo.value;
    if (!cVal) {
        skladInfoSpan.textContent = '';
        skladFotoMain.src = '';
        skladFotoExtra1.src = '';
        skladFotoExtra2.src = '';
        return;
    }
    fetch(`/ajax/get_sklad_info/?cislo_skladu=${cVal}`)
        .then(r => r.json())
        .then(info => {
            if (info && info.plocha && info.poschodie) {
                skladInfoSpan.textContent = `Plocha: ${info.plocha} m², Poschodie: ${info.poschodie}`;
            } else {
                skladInfoSpan.textContent = '';
            }
            skladFotoMain.src = info.foto_main || '';
            skladFotoExtra1.src = info.foto_extra1 || '';
            skladFotoExtra2.src = info.foto_extra2 || '';
        })
        .catch(err => {
            skladInfoSpan.textContent = '';
            skladFotoMain.src = '';
            skladFotoExtra1.src = '';
            skladFotoExtra2.src = '';
        });
}

// Первичная инициализация и обработчики событий для динамической подгрузки данных
document.addEventListener('DOMContentLoaded', function() {
    const typSkladu = document.querySelector('#id_typ_skladu');
    const lokalita = document.querySelector('#id_lokalita');
    const velkost  = document.querySelector('#id_velkost_skladu');

    // Если тип skladu уже выбран – сразу загружаем lokalita и последующие поля
    if (typSkladu && typSkladu.value) {
        loadLokalita(true);
    }

    // При изменении типа skladu загружаем lokalita
    if (typSkladu) {
        typSkladu.addEventListener('change', function() {
            loadLokalita(true);
        });
    }

    // При изменении lokalita загружаем velkost
    if (lokalita) {
        lokalita.addEventListener('change', function() {
            loadVelkost(true);
        });
    }

    // При изменении veľkosť skladu загружаем číslo skladu
    if (velkost) {
        velkost.addEventListener('change', function() {
            loadCislo(true);
        });
    }

    // --- Инициализация выпадающих списков для поля Krajina ---
    const countrySelectFyz = document.getElementById('id_krajina');
    const countrySelectPrav = document.getElementById('id_sidlo_krajina');

    const countriesAll = [
        "Slovensko", "Afganistan", "Albánsko", "Aljaška", "Alžírsko", "Andora", "Angola", "Anguila", "Antigua a Barbuda",
        "Argentína", "Arménsko", "Aruba", "Ascension", "Austrália", "Austrálske externé územia", "Azerbajdžan", "Azorské ostrovy",
        "Bahamy", "Bahrajn", "Bangladéš", "Barbados", "Belgicko", "Belize", "Benin", "Bermudy", "Bhután", "Bielorusko", "Bolívia",
        "Bosna a Hercegovina", "Botswana", "Brazília", "Brunei", "Bulharsko", "Burkina Faso", "Burundi", "Cyprus", "Čad", "Česká republika",
        "Čierna Hora", "Čína", "Dánsko", "Demokratická rep. Kongo", "Diego Garcia", "Dominika", "Dominikánska republika", "Džibuti",
        "Egypt", "Ekvádor", "Eritrea", "Estónsko", "Etiópia", "Faerské ostrovy", "Falklandy - Malvíny", "Fidži", "Filipíny", "Fínsko",
        "Francúzsko", "Gabun", "Gambia", "Ghana", "Gibraltar", "Grécko", "Grenada", "Grónsko", "Gruzínsko", "Guadeloupe", "Guam",
        "Guatemala", "Guinea - Bissau", "Guinea - republika", "Guyana - Francúzska", "Guyana - republika", "Haiti", "Holandské Antily",
        "Holandsko", "Honduras", "Hongkong", "Chile", "Chorvátsko", "India", "Indonézia", "Irak", "Irán", "Írsko", "Island", "Izrael",
        "Jamajka", "Japonsko", "Jemen", "Jordánsko", "JAR - Juhoafr. Rep.", "Juhoslávia (Srbsko)", "Kajmanské ostrovy", "Kambodža",
        "Kamerun", "Kanada", "Kapverdy", "Katar", "Kazachstan", "Keňa", "Kirgizstan", "Kiribati", "Kolumbia", "Komory a Mayotte",
        "Kongo", "Kórea - Južná", "Kórea - Severná - KĽDR", "Kookove ostrovy", "Kostarika", "Kuba", "Kuvajt", "Laos", "Lesotho",
        "Libanon", "Libéria", "Líbya", "Lichtenštajnsko", "Litva", "Lotyšsko", "Luxembursko", "Macao", "Macedónia", "Madagaskar",
        "Maďarsko", "Madeira", "Malajzia", "Malawi", "Maledivy", "Mali", "Malta", "Mariany - Severné", "Maroko", "Marshallove ostrovy",
        "Martinik", "Mauretánia", "Maurícius", "Mexiko", "Mikronézia", "Moldavsko", "Monako", "Mongolsko", "Montserrat", "Mozambik",
        "Myanmar", "Namíbia", "Nauru", "Nemecko", "Nepál", "Niger", "Nigéria", "Nikaragua", "Niue", "Nórsko", "Nová Kaledónia",
        "Nový Zéland", "Omán", "Pakistan", "Palau", "Palestína", "Panama", "Panenské ostrovy - GB", "Panenské ostrovy - USA",
        "Papua - Nová Guinea", "Paraguay", "Peru", "Pobrežie slonoviny", "Polynézia - FR", "Poľsko", "Portoriko",
        "Portugalsko (Azory a Madeira)", "Rakúsko", "Reunion", "Rovníková Guinea", "Rumunsko", "Rusko", "Rwanda",
        "SAE - Spoj. Arab. Emiráty", "Salvador", "Samoa - USA", "Samoa - západná", "San Marino", "Saudská Arábia",
        "Senegal", "Seyschely", "Sierra Leone", "Singapur", "Slovinsko", "Somálsko", "Srbsko (Juhoslávia)",
        "Srí Lanka (Cejlón)", "Stredoafr. Rep.", "Sudán", "Surinam", "Svätá Helena", "Svätá Lucia", "Svätý Krištof a Nevis",
        "Svätý Peter a Michal", "Svätý Tomáš a Princov ostrov", "Svätý Vincent a Grenadíny", "Svazijsko", "Sýria",
        "Šalamúnove ostrovy", "Španielsko", "Švajčiarsko", "ŠVÉDSKO", "Tadžikistan", "Tahiti", "Taliansko", "Tanzánia",
        "Thajsko", "Tchaj-wan", "Togo", "Tokelau", "Tonga", "Trinidad a Tobago", "Tunis", "Turecko", "Turkmenistan",
        "Turky", "Tuvalu", "Uganda", "Ukrajina", "Uruguay", "USA", "Uzbekistan", "Vanuatu", "Vatikán",
        "Veľká Británia a Sev. Írsko", "Venezuela", "Vietnam", "Wallis a Futuna", "Zambia", "Zimbabwe"
    ];

    function fillCountrySelect(selectEl, selectedVal) {
        if (!selectEl) return;
        selectEl.innerHTML = '';
        countriesAll.forEach(country => {
            const opt = document.createElement('option');
            opt.value = country;
            opt.textContent = country;
            if (country === selectedVal) {
                opt.selected = true;
            }
            selectEl.appendChild(opt);
        });
    }

    if (countrySelectFyz) {
        fillCountrySelect(countrySelectFyz, "Slovensko");
    }
    if (countrySelectPrav) {
        fillCountrySelect(countrySelectPrav, "Slovensko");
    }
});

// ------------------------------
// Дополнительная логика для автоматического выбора "Dostupné sekcie" в карточке клиента
// ------------------------------
document.addEventListener('DOMContentLoaded', function() {
    // Обработчик отправки формы
    const rentForm = document.getElementById('rent_form');
    rentForm.addEventListener('submit', function() {
        // Получаем значение поля "Právne postavenie nájomcu"
        const pravneVal = document.getElementById('id_pravne_postavenie_najomcu').value;
        // Получаем селект "available" (не выбранные опции) и "chosen" (выбранные опции) из виджета
        const availableSelect = document.getElementById('id_dostupne_sekcie_from');
        const chosenSelect = document.getElementById('id_dostupne_sekcie_to');
        
        // Очищаем список выбранных опций
        while (chosenSelect.options.length > 0) {
            chosenSelect.remove(0);
        }
        
        // Определяем, какая опция должна быть выбрана:
        // Если "Fyzická osoba" – опция с value="6"
        // Если "Právnická osoba (bez DPH)" или "Právnická osoba (platca DPH)" (или любое значение, содержащее "Právnická osoba") – опция с value="7"
        let targetValue = "";
        if (pravneVal === "Fyzická osoba") {
            targetValue = "6";
        } else if (pravneVal === "Právnická osoba (bez DPH)" ||
                   pravneVal === "Právnická osoba (platca DPH)" ||
                   pravneVal.indexOf("Právnická osoba") !== -1) {
            targetValue = "7";
        }
        
        // Если целевое значение определено, ищем соответствующую опцию в availableSelect и перемещаем её в выбранные
        if (targetValue) {
            for (let i = 0; i < availableSelect.options.length; i++) {
                if (availableSelect.options[i].value === targetValue) {
                    const opt = availableSelect.options[i].cloneNode(true);
                    chosenSelect.appendChild(opt);
                    break;
                }
            }
        }
    });
});
