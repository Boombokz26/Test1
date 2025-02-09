// static/js/phone.js

document.addEventListener('DOMContentLoaded', function() {
    const phoneCodeSelect = document.getElementById('phone_code');
    const phoneRestInput  = document.getElementById('phone_rest');
    const phoneErrorSpan  = document.getElementById('phone_error');
    const finalPhoneHidden = document.getElementById('id_cislo_pre_komunikaciu');

    const countryToDialMap = {
        "Afganistan": "+93",
        "Albánsko": "+355",
        "Aljaška": "+1907",
        "Alžírsko": "+213",
        "Andora": "+376",
        "Angola": "+244",
        "Anguila": "+1264",
        "Antigua a Barbuda": "+1268",
        "Argentína": "+54",
        "Arménsko": "+374",
        "Aruba": "+297",
        "Ascension": "+247",
        "Austrália": "+61",
        "Austrálske externé územia": "+672",
        "Azerbajdžan": "+994",
        "Azorské ostrovy": "+351",
        "Bahamy": "+1242",
        "Bahrajn": "+973",
        "Bangladéš": "+880",
        "Barbados": "+1246",
        "Belgicko": "+32",
        "Belize": "+501",
        "Benin": "+229",
        "Bermudy": "+1441",
        "Bhután": "+975",
        "Bielorusko": "+375",
        "Bolívia": "+591",
        "Bosna a Hercegovina": "+387",
        "Botswana": "+267",
        "Brazília": "+55",
        "Brunei": "+673",
        "Bulharsko": "+359",
        "Burkina Faso": "+226",
        "Burundi": "+257",
        "Cyprus": "+357",
        "Čad": "+235",
        "Česká republika": "+420",
        "Čierna Hora": "+381",
        "Čína": "+86",
        "Dánsko": "+45",
        "Demokratická rep. Kongo": "+243",
        "Diego Garcia": "+246",
        "Dominika": "+1767",
        "Dominikánska republika": "+1809",
        "Džibuti": "+253",
        "Egypt": "+20",
        "Ekvádor": "+593",
        "Eritrea": "+291",
        "Estónsko": "+372",
        "Etiópia": "+251",
        "Faerské ostrovy": "+298",
        "Falklandy - Malvíny": "+500",
        "Fidži": "+679",
        "Filipíny": "+63",
        "Fínsko": "+358",
        "Francúzsko": "+33",
        "Gabun": "+241",
        "Gambia": "+220",
        "Ghana": "+233",
        "Gibraltar": "+350",
        "Grécko": "+30",
        "Grenada": "+1473",
        "Grónsko": "+299",
        "Gruzínsko": "+995",
        "Guadeloupe": "+590",
        "Guam": "+671",
        "Guatemala": "+502",
        "Guinea - Bissau": "+245",
        "Guinea - republika": "+224",
        "Guyana - Francúzska": "+594",
        "Guyana - republika": "+592",
        "Haiti": "+509",
        "Holandské Antily": "+599",
        "Holandsko": "+31",
        "Honduras": "+504",
        "Hongkong": "+852",
        "Chile": "+56",
        "Chorvátsko": "+385",
        "India": "+91",
        "Indonézia": "+62",
        "Irak": "+964",
        "Irán": "+98",
        "Írsko": "+353",
        "Island": "+354",
        "Izrael": "+972",
        "Jamajka": "+1876",
        "Japonsko": "+81",
        "Jemen": "+967",
        "Jordánsko": "+962",
        "JAR - Juhoafr. Rep.": "+27",
        "Juhoslávia (Srbsko)": "+381",
        "Kajmanské ostrovy": "+1345",
        "Kambodža": "+855",
        "Kamerun": "+237",
        "Kanada": "+1",
        "Kapverdy": "+238",
        "Katar": "+974",
        "Kazachstan": "+7",
        "Keňa": "+254",
        "Kirgizstan": "+996",
        "Kiribati": "+686",
        "Kolumbia": "+57",
        "Komory a Mayotte": "+269",
        "Kongo": "+242",
        "Kórea - Južná": "+82",
        "Kórea - Severná - KĽDR": "+850",
        "Kookove ostrovy": "+682",
        "Kostarika": "+506",
        "Kuba": "+53",
        "Kuvajt": "+965",
        "Laos": "+856",
        "Lesotho": "+266",
        "Libanon": "+961",
        "Libéria": "+231",
        "Líbya": "+218",
        "Lichtenštajnsko": "+423",
        "Litva": "+370",
        "Lotyšsko": "+371",
        "Luxembursko": "+352",
        "Macao": "+853",
        "Macedónia": "+389",
        "Madagaskar": "+261",
        "Maďarsko": "+36",
        "Madeira": "+351",
        "Malajzia": "+60",
        "Malawi": "+265",
        "Maledivy": "+960",
        "Mali": "+223",
        "Malta": "+356",
        "Mariany - Severné": "+1670",
        "Maroko": "+212",
        "Marshallove ostrovy": "+692",
        "Martinik": "+596",
        "Mauretánia": "+222",
        "Maurícius": "+230",
        "Mexiko": "+52",
        "Mikronézia": "+691",
        "Moldavsko": "+373",
        "Monako": "+377",
        "Mongolsko": "+976",
        "Montserrat": "+1664",
        "Mozambik": "+258",
        "Myanmar": "+95",
        "Namíbia": "+264",
        "Nauru": "+674",
        "Nemecko": "+49",
        "Nepál": "+977",
        "Niger": "+227",
        "Nigéria": "+234",
        "Nikaragua": "+505",
        "Niue": "+683",
        "Nórsko": "+47",
        "Nová Kaledónia": "+687",
        "Nový Zéland": "+64",
        "Omán": "+968",
        "Pakistan": "+92",
        "Palau": "+680",
        "Palestína": "+970",
        "Panama": "+507",
        "Panenské ostrovy - GB": "+1284",
        "Panenské ostrovy - USA": "+1340",
        "Papua - Nová Guinea": "+675",
        "Paraguay": "+595",
        "Peru": "+51",
        "Pobrežie slonoviny": "+225",
        "Polynézia - FR": "+689",
        "Poľsko": "+48",
        "Portoriko": "+1787",
        "Portugalsko (Azory a Madeira)": "+351",
        "Rakúsko": "+43",
        "Reunion": "+262",
        "Rovníková Guinea": "+240",
        "Rumunsko": "+40",
        "Rusko": "+7",
        "Rwanda": "+250",
        "SAE - Spoj. Arab. Emiráty": "+971",
        "Salvador": "+503",
        "Samoa - USA": "+684",
        "Samoa - západná": "+685",
        "San Marino": "+378",
        "Saudská Arábia": "+966",
        "Senegal": "+221",
        "Seyschely": "+248",
        "Sierra Leone": "+232",
        "Singapur": "+65",
        "Slovinsko": "+386",
        "Somálsko": "+252",
        "Srbsko (Juhoslávia)": "+381",
        "Srí Lanka (Cejlón)": "+94",
        "Stredoafr. Rep.": "+236",
        "Sudán": "+249",
        "Surinam": "+597",
        "Svätá Helena": "+290",
        "Svätá Lucia": "+1758",
        "Svätý Krištof a Nevis": "+1869",
        "Svätý Peter a Michal": "+508",
        "Svätý Tomáš a Princov ostrov": "+239",
        "Svätý Vincent a Grenadíny": "+1809",
        "Svazijsko": "+268",
        "Sýria": "+963",
        "Šalamúnove ostrovy": "+677",
        "Španielsko": "+34",
        "Švajčiarsko": "+41",
        "ŠVÉDSKO": "+46",
        "Tadžikistan": "+992",
        "Tahiti": "+689",
        "Taliansko": "+39",
        "Tanzánia": "+255",
        "Thajsko": "+66",
        "Tchaj-wan": "+886",
        "Togo": "+228",
        "Tokelau": "+690",
        "Tonga": "+676",
        "Trinidad a Tobago": "+1868",
        "Tunis": "+216",
        "Turecko": "+90",
        "Turkmenistan": "+993",
        "Turky": "+1649",
        "Tuvalu": "+688",
        "Uganda": "+256",
        "Ukrajina": "+380",
        "Uruguay": "+598",
        "USA": "+1",
        "Uzbekistan": "+998",
        "Vanuatu": "+678",
        "Vatikán": "+39",
        "Veľká Británia a Sev. Írsko": "+44",
        "Venezuela": "+58",
        "Vietnam": "+84",
        "Wallis a Futuna": "+681",
        "Zambia": "+260",
        "Zimbabwe": "+263",
        "Slovensko": "+421"
    };

    if (phoneCodeSelect) {
        const sortedCountries = Object.keys(countryToDialMap).sort();
        sortedCountries.forEach(function(country) {
            const code = countryToDialMap[country];
            const opt = document.createElement('option');
            opt.value = code;
            opt.textContent = code;
            phoneCodeSelect.appendChild(opt);
        });
    }

    function restorePhone() {
        if (!finalPhoneHidden) return;
        const existing = finalPhoneHidden.value;
        if (!existing) {
            phoneCodeSelect.value = "+421";
            phoneRestInput.value = "";
            return;
        }
        let matched = false;
        for (let i = 0; i < phoneCodeSelect.options.length; i++) {
            const code = phoneCodeSelect.options[i].value;
            if (existing.startsWith(code)) {
                phoneCodeSelect.value = code;
                phoneRestInput.value = existing.substring(code.length);
                matched = true;
                break;
            }
        }
        if (!matched) {
            phoneCodeSelect.value = "+421";
            phoneRestInput.value = existing;
        }
    }
    restorePhone();

    function syncPhoneField() {
        finalPhoneHidden.value = phoneCodeSelect.value.trim() + phoneRestInput.value.trim();
    }

    function validatePhoneRest() {
        const val = phoneRestInput.value.trim();
        if (!val) {
            phoneErrorSpan.textContent = "Telefónne číslo musí byť zadané";
            phoneErrorSpan.classList.add('active');
            phoneRestInput.classList.add('invalid-input');
        } else if (val.startsWith('0')) {
            phoneErrorSpan.textContent = "Telefónne číslo nemôže začínať číslom 0";
            phoneErrorSpan.classList.add('active');
            phoneRestInput.classList.add('invalid-input');
        } else {
            phoneErrorSpan.textContent = "";
            phoneErrorSpan.classList.remove('active');
            phoneRestInput.classList.remove('invalid-input');
        }
    }

    if (phoneCodeSelect) {
        phoneCodeSelect.addEventListener('change', function() {
            syncPhoneField();
            validatePhoneRest();
            if (typeof window.checkStep3Validity === 'function') {
                window.checkStep3Validity();
            }
        });
    }
    if (phoneRestInput) {
        phoneRestInput.addEventListener('input', function() {
            syncPhoneField();
            validatePhoneRest();
            if (typeof window.checkStep3Validity === 'function') {
                window.checkStep3Validity();
            }
        });
        phoneRestInput.addEventListener('blur', function() {
            syncPhoneField();
            validatePhoneRest();
            if (typeof window.checkStep3Validity === 'function') {
                window.checkStep3Validity();
            }
        });
    }

    const countryFieldFyz = document.getElementById('id_krajina');
    if (countryFieldFyz) {
        countryFieldFyz.addEventListener('change', function() {
            autoSetPhoneCodeByCountry();
        });
    }
    const countryFieldPrav = document.getElementById('id_sidlo_krajina');
    if (countryFieldPrav) {
        countryFieldPrav.addEventListener('change', function() {
            autoSetPhoneCodeByCountry();
        });
    }

    function autoSetPhoneCodeByCountry() {
        const pravneSelect = document.getElementById('id_pravne_postavenie_najomcu');
        let selectedCountry = "";
        if (pravneSelect) {
            const pravneVal = pravneSelect.value;
            if (pravneVal === "Fyzická osoba") {
                const countryField = document.getElementById('id_krajina');
                if (countryField) {
                    selectedCountry = countryField.value;
                }
            } else if (pravneVal === "Právnická osoba (bez DPH)" || pravneVal === "Právnická osoba (platca DPH)") {
                const countryField = document.getElementById('id_sidlo_krajina');
                if (countryField) {
                    selectedCountry = countryField.value;
                }
            }
        }
        if (selectedCountry && countryToDialMap[selectedCountry]) {
            phoneCodeSelect.value = countryToDialMap[selectedCountry];
            syncPhoneField();
            validatePhoneRest();
        }
    }
    window.autoSetPhoneCodeByCountry = autoSetPhoneCodeByCountry;
});
