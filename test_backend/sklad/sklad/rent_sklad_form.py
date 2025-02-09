# rent_sklad_form.py

from django import forms
from django.utils import timezone
from datetime import date, timedelta
import re
import random
from .forms import NoValidateChoiceField
from .models import Users, Warhouses

class WarehouseRentalForm(forms.Form):
    # Поля skladu
    typ_skladu = NoValidateChoiceField(choices=[], required=True)
    lokalita = NoValidateChoiceField(choices=[], required=True)
    prenajat_sklad_od = forms.DateField(required=True)
    velkost_skladu = NoValidateChoiceField(choices=[], required=True)
    cislo_skladu = NoValidateChoiceField(choices=[], required=False)
    doba_prenajmu = NoValidateChoiceField(choices=[], required=False)

    # Fyzická osoba
    pravne_postavenie_najomcu = forms.ChoiceField(choices=[], required=False)
    meno_a_priezvisko = forms.CharField(required=False)
    datum_narodenia = forms.DateField(required=False)

    # Адрес (Fyzická osoba)
    ulica = forms.CharField(label="Ulica", required=False)
    cislo_domu = forms.CharField(label="Číslo domu", required=False)
    psc = forms.CharField(label="PSČ", required=False)
    mesto = forms.CharField(label="Mesto", required=False)
    krajina = forms.CharField(label="Krajina", required=False)

    # Právnická osoba
    nazov = forms.CharField(required=False)
    zastupeny = forms.CharField(required=False)
    sidlo_ulica = forms.CharField(label="Sidlo ulica", required=False)
    sidlo_cislo_domu = forms.CharField(label="Sidlo číslo domu", required=False)
    sidlo_psc = forms.CharField(label="Sidlo PSČ", required=False)
    sidlo_mesto = forms.CharField(label="Sidlo mesto", required=False)
    sidlo_krajina = forms.CharField(label="Sidlo krajina", required=False)

    ico = forms.CharField(required=False)
    dic = forms.CharField(required=False)
    ic_dph = forms.CharField(required=False)

    # Общее
    cislo_pre_komunikaciu = forms.CharField(required=False)  # Без автоплагинов
    email = forms.EmailField(required=False)
    heslo = forms.CharField(required=False, widget=forms.PasswordInput)
    suhlas_kaucia = forms.BooleanField(required=False)
    suhlas_zmluva = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Динамический список типов skladu
        available_typy = (
            Warhouses.objects
            .filter(stav_vsetci="Voľné")
            .values_list('typ_skladu', flat=True)
            .distinct()
        )
        typy_choices = [(val, val) for val in available_typy]
        self.fields['typ_skladu'].choices = typy_choices
        if typy_choices:
            self.fields['typ_skladu'].initial = typy_choices[0][0]

        # Právne postavenie nájomcu
        self.fields['pravne_postavenie_najomcu'].choices = [
            ('Fyzická osoba', 'Fyzická osoba'),
            ('Právnická osoba (bez DPH)', 'Právnická osoba (bez DPH)'),
            ('Právnická osoba (platca DPH)', 'Právnická osoba (platca DPH)'),
        ]

    def clean(self):
        cleaned_data = super().clean()
        prenajat_datum = cleaned_data.get('prenajat_sklad_od')
        if prenajat_datum:
            today = date.today()
            if prenajat_datum < today or prenajat_datum > today + timedelta(days=14):
                self.add_error('prenajat_sklad_od', "Dátum musí byť od dnešného dňa až do 14 dní vopred.")

        meno = cleaned_data.get('meno_a_priezvisko')
        if meno:
            pattern_meno = r'^[A-Za-z-]+(?:\s[A-Za-z-]+){1,3}$'
            if not re.match(pattern_meno, meno):
                self.add_error('meno_a_priezvisko', "Meno a priezvisko musí obsahovať 2 až 4 slová, len písmená a pomlčky.")

        # IČO
        ico_val = cleaned_data.get('ico')
        if ico_val and not re.match(r'^\d{8}$', ico_val):
            self.add_error('ico', "IČO musí mať presne 8 číslic.")

        # DIČ
        dic_val = cleaned_data.get('dic')
        if dic_val and not re.match(r'^\d{10}$', dic_val):
            self.add_error('dic', "DIČ musí mať presne 10 číslic.")

        # IČ DPH
        ic_dph_val = cleaned_data.get('ic_dph')
        if ic_dph_val and not re.match(r'^[A-Za-z]{2}\d{10}$', ic_dph_val):
            self.add_error('ic_dph', "IČ DPH musí mať formát XX**********, kde XX sú písmená a potom 10 číslic.")

        # Дата narodenia
        datum_nar = cleaned_data.get('datum_narodenia')
        if datum_nar:
            age = date.today().year - datum_nar.year
            if age < 18 or age > 90:
                self.add_error('datum_narodenia', "Vek musí byť od 18 do 90 rokov.")

        # Пароль
        heslo_val = cleaned_data.get('heslo')
        if heslo_val:
            if not (
                re.search(r'[A-Z]', heslo_val) and
                re.search(r'[a-z]', heslo_val) and
                re.search(r'\d', heslo_val) and
                re.search(r'\W', heslo_val)
            ):
                self.add_error('heslo', "Heslo musí obsahovať veľké písmeno, malé písmeno, číslicu a špeciálny znak.")

        # Галочки
        if not cleaned_data.get('suhlas_kaucia'):
            self.add_error('suhlas_kaucia', "Musíte súhlasiť s kauciou.")
        if not cleaned_data.get('suhlas_zmluva'):
            self.add_error('suhlas_zmluva', "Musíte súhlasiť so zmluvou.")

        # Телефон (2 часть)
        phone_val = cleaned_data.get('cislo_pre_komunikaciu', '').strip()
        if not phone_val:
            self.add_error('cislo_pre_komunikaciu', "Telefónne číslo musí byť zadané.")
        elif phone_val.startswith('0'):
            self.add_error('cislo_pre_komunikaciu', "Telefónne číslo nemôže začínať číslom 0.")

        return cleaned_data

    def save(self):
        cd = self.cleaned_data
        cislo = cd['cislo_skladu']

        # Обновляем sklad (Voľné -> Prenajaté)
        try:
            sklad_obj = Warhouses.objects.get(id_skladu=cislo, stav_vsetci="Voľné")
            sklad_obj.stav_vsetci = "Prenajaté"
            sklad_obj.save()
        except Warhouses.DoesNotExist:
            pass

        # Создаём пользователя
        from .models import Users, Sekcia
        user = Users()
        user.email = cd['email']
        user.heslo = cd['heslo']
        user.set_password(cd['heslo'])

        pravne_val = cd['pravne_postavenie_najomcu']
        if pravne_val == "Fyzická osoba":
            user.meno_nazov = cd['meno_a_priezvisko']
            # Адрес для Fyzická
            parts = []
            if cd.get('ulica'):
                parts.append(cd['ulica'])
            if cd.get('cislo_domu'):
                parts.append(cd['cislo_domu'])
            if cd.get('psc') and cd.get('mesto'):
                parts.append(f"{cd['psc']} {cd['mesto']}")
            elif cd.get('psc'):
                parts.append(cd['psc'])
            elif cd.get('mesto'):
                parts.append(cd['mesto'])
            if cd.get('krajina'):
                parts.append(cd['krajina'])
            user.adresa_bydliska_sidlo = ', '.join(parts)
        else:
            # Právnická osoba
            user.meno_nazov = cd['nazov']
            sidlo_parts = []
            if cd.get('sidlo_ulica'):
                sidlo_parts.append(cd['sidlo_ulica'])
            if cd.get('sidlo_cislo_domu'):
                sidlo_parts.append(cd['sidlo_cislo_domu'])
            if cd.get('sidlo_psc') and cd.get('sidlo_mesto'):
                sidlo_parts.append(f"{cd['sidlo_psc']} {cd['sidlo_mesto']}")
            elif cd.get('sidlo_psc'):
                sidlo_parts.append(cd['sidlo_psc'])
            elif cd.get('sidlo_mesto'):
                sidlo_parts.append(cd['sidlo_mesto'])
            if cd.get('sidlo_krajina'):
                sidlo_parts.append(cd['sidlo_krajina'])
            user.adresa_bydliska_sidlo = ', '.join(sidlo_parts)

        user.zastupeny = cd.get('zastupeny', '')
        user.datum_narodenia = cd.get('datum_narodenia')
        user.tel_cislo = cd.get('cislo_pre_komunikaciu', '')

        if pravne_val.startswith("Právnická osoba"):
            user.ico = cd.get('ico', '')
            user.dic = cd.get('dic', '')
            if pravne_val == "Právnická osoba (platca DPH)":
                user.ic_dph = cd.get('ic_dph', '')
            else:
                user.ic_dph = None

        user.typ_pouzivatela = pravne_val
        user.is_active = True
        user.is_staff = False
        user.stav_prenajmu = "aktívný, pripojený"
        user.preferovany_jazyk = "SK"

        # Присваиваем доступ к G, K, N и т.д.
        letters = list(cislo)
        user.povoleny_pristup_arealu_g = "Áno" if "G" in letters else "Nie"
        user.povoleny_pristup_arealu_k = "Áno" if "K" in letters else "Nie"
        user.povoleny_pristup_arealu_n = "Áno" if "N" in letters else "Nie"
        user.povoleny_pristup_arealu_d = "Áno" if "D" in letters else "Nie"
        user.povoleny_pristup_arealu_t = "Áno" if "T" in letters else "Nie"
        if "H" in letters:
            user.povoleny_pristup_arealu_h = "Áno"
            import random
            code_digits = ''.join(str(random.randint(0, 9)) for _ in range(7))
            user.pristupovy_kod_arealu_h = code_digits + '#'
        else:
            user.povoleny_pristup_arealu_h = "Nie"
            user.pristupovy_kod_arealu_h = "Nie"

        now_str = timezone.now().strftime("%d%m%Y%H%M%S")
        user.zmluva_aktualna = f"{cislo}{now_str}"
        user.datum_uzavretia_zmluvy_aktualna = cd['prenajat_sklad_od']
        user.id_skladu_zmluva_aktualna = cislo

        user.save()

        # Новая логика: автоматический выбор dostupne sekcie в зависимости от právneho postavenia
        try:
            if pravne_val == "Fyzická osoba":
                sekcia = Sekcia.objects.get(pk=6)
            else:
                sekcia = Sekcia.objects.get(pk=7)
            user.dostupne_sekcie.set([sekcia])
        except Sekcia.DoesNotExist:
            pass

        return user
