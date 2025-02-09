from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class Areas(models.Model):
    ID_arealu = models.CharField(
        max_length=1,
        choices=[
            ('G', 'G'),
            ('K', 'K'),
            ('D', 'D'),
            ('N', 'N'),
            ('T', 'T'),
            ('H', 'H')
        ],
        verbose_name="ID areálu"
    )
    adresa_zmluva = models.CharField(
        max_length=255,
        choices=[
            ('Gessayova 3, 851 03 Petržalka, Bratislava', 'Gessayova 3, 851 03 Petržalka, Bratislava'),
            ('Kaukazská 2, 851 01 Petržalka, Bratislava', 'Kaukazská 2, 851 01 Petržalka, Bratislava'),
            ('Polianky 15, 841 01 Dúbravka, Bratislava', 'Polianky 15, 841 01 Dúbravka, Bratislava'),
            ('Bratislavská 15, 949 01 Nitra', 'Bratislavská 15, 949 01 Nitra'),
            ('Tomášikova 50D, 831 04, Bratislava', 'Tomášikova 50D, 831 04, Bratislava'),
            ('Holíčska 7, 851 05, Petržalka, Bratislava', 'Holíčska 7, 851 05, Petržalka, Bratislava')
        ],
        verbose_name="Adresa areálu (pre zmluvu)"
    )
    adresa_formular = models.CharField(
        max_length=255,
        choices=[
            ('Gessayova 3, Petržalka, Bratislava', 'Gessayova 3, Petržalka, Bratislava'),
            ('Kaukazská 2, Petržalka, Bratislava', 'Kaukazská 2, Petržalka, Bratislava'),
            ('Polianky 15, Dúbravka, Bratislava', 'Polianky 15, Dúbravka, Bratislava'),
            ('Bratislavská 15, Nitra', 'Bratislavská 15, Nitra'),
            ('Tomášikova 50D, Bratislava', 'Tomášikova 50D, Bratislava'),
            ('Holíčska 7, Petržalka, Bratislava', 'Holíčska 7, Petržalka, Bratislava')
        ],
        verbose_name="Adresa areálu (pre formular)"
    )
    pristup = models.CharField(
        max_length=10,
        choices=[
            ('GSM', 'GSM'),
            ('Kód', 'Kód'),
            ('Kluč', 'Kluč')
        ],
        verbose_name="Prístup k areálu"
    )
    tel_cislo_brany = models.CharField(
        max_length=15,
        verbose_name="Tel. číslo brány na prístup do areálu"
    )
    dalsie_vybavenie = models.ManyToManyField(
        'Vybavenie',
        verbose_name="Ďalšie vybavenie",
        blank=True
    )
    poistenie = models.CharField(
        max_length=20,
        choices=[
            ('Do 2000€', 'Do 2000€'),
            ('-', '-')
        ],
        verbose_name="Základné poistenie skladov"
    )
    osvetlenie = models.CharField(
        max_length=3,
        choices=[
            ('Áno', 'Áno'),
            ('Nie', 'Nie')
        ],
        verbose_name="Osvetlenie areálu"
    )
    poznamka = models.TextField(
        max_length=1000,
        blank=True,
        verbose_name="Poznámka"
    )

    def __str__(self):
        return self.ID_arealu

    class Meta:
        verbose_name = "Areál"
        verbose_name_plural = "Areály"

class Vybavenie(models.Model):
    nazov = models.CharField(max_length=255, verbose_name="Názov vybavenia")

    class Meta:
        verbose_name = "Vybavenie"
        verbose_name_plural = "Vybavenia"

    def __str__(self):
        return self.nazov

class Warhouses(models.Model):
    adresa_zmluva = models.CharField(
        max_length=255,
        choices=[
            ('Gessayova 3, 851 03 Petržalka, Bratislava', 'Gessayova 3, 851 03 Petržalka, Bratislava'),
            ('Kaukazská 2, 851 01 Petržalka, Bratislava', 'Kaukazská 2, 851 01 Petržalka, Bratislava'),
            ('Polianky 15, 841 01 Dúbravka, Bratislava', 'Polianky 15, 841 01 Dúbravka, Bratislava'),
            ('Bratislavská 15, 949 01 Nitra', 'Bratislavská 15, 949 01 Nitra'),
            ('Tomášikova 50D, 831 04, Bratislava', 'Tomášikova 50D, 831 04, Bratislava'),
            ('Holíčska 7, 851 05, Petržalka, Bratislava', 'Holíčska 7, 851 05, Petržalka, Bratislava')
        ],
        verbose_name="Adresa areálu (pre zmluvu)"
    )
    adresa_formular = models.CharField(
        max_length=255,
        choices=[
            ('Gessayova 3, Petržalka, Bratislava', 'Gessayova 3, Petržalka, Bratislava'),
            ('Kaukazská 2, Petržalka, Bratislava', 'Kaukazská 2, Petržalka, Bratislava'),
            ('Polianky 15, Dúbravka, Bratislava', 'Polianky 15, Dúbravka, Bratislava'),
            ('Bratislavská 15, Nitra', 'Bratislavská 15, Nitra'),
            ('Tomášikova 50D, Bratislava', 'Tomášikova 50D, Bratislava'),
            ('Holíčska 7, Petržalka, Bratislava', 'Holíčska 7, Petržalka, Bratislava')
        ],
        verbose_name="Adresa areálu (pre formular)"
    )
    typ_skladu = models.CharField(
        max_length=20,
        choices=[
            ('Externý (Kontajnery)', 'Externý (Kontajnery)'),
            ('Interný (Kobky)', 'Interný (Kobky)')
        ],
        verbose_name="Typ skladu"
    )
    cislo_skladu = models.CharField(max_length=100, verbose_name="Číslo skladu")
    id_skladu = models.CharField(
        max_length=20,
        verbose_name="ID skladu"
    )
    poschodie = models.CharField(
        max_length=50,
        choices=[
            ('Prízemie', 'Prízemie'),
            ('1 nadzemné poschodie', '1 nadzemné poschodie'),
            ('Prízemie (na terase)', 'Prízemie (na terase)')
        ],
        verbose_name="Poschodie"
    )
    cena_bez_dph_mesiac = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Cena bez DPH (1 krát za mesiac)"
    )
    cena_bez_dph_polrok = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Cena bez DPH (1 krát za polroka)"
    )
    cena_bez_dph_rok = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Cena bez DPH (1 krát za rok)"
    )
    cena_s_dph_mesiac = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Cena s DPH (1 krát za mesiac)"
    )
    cena_s_dph_polrok = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Cena s DPH (1 krát za polroka)"
    )
    cena_s_dph_rok = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Cena s DPH (1 krát za rok)"
    )
    dph_mesiac = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="DPH (1 krát za mesiac)"
    )
    dph_polrok = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="DPH (1 krát za polroka)"
    )
    dph_rok = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="DPH (1 krát za rok)"
    )
    kaucia_mesiac = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Kaucia pre prenájom skladov (1 krát za mesiac)"
    )
    kaucia_polrok = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Kaucia pre prenájom skladov (1 krát za polroka)"
    )
    kaucia_rok = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Kaucia pre prenájom skladov (1 krát za rok)"
    )
    poistenie = models.CharField(
        max_length=20,
        choices=[
            ('Do 2000€', 'Do 2000€'),
            ('-', '-')
        ],
        verbose_name="Základné poistenie skladov"
    )
    rozsirene_poistenie = models.ManyToManyField(
        'RozsirenePoistenie',
        verbose_name="Rozšírené možnosti poistenia",
        blank=True
    )
    doplatok_poistenie_5000 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Doplatok mesačne k cene za predĺžené poistenie Do 5000€"
    )
    doplatok_poistenie_7000 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Mesačný príplatok k cene predĺženého poistenia Do 7000€"
    )
    doplatok_poistenie_10000 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Doplatok mesačne k cene za predĺžené poistenie Do 10000€"
    )
    dlzka_skladu = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Dĺžka skladu (m.)"
    )
    sirka_skladu = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Šírka skladu (m.)"
    )
    vyska_skladu = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Výška skladu (m.)"
    )
    sirka_dveri = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Šírka dverí (m.)"
    )
    vyska_dveri = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Výška dverí (m.)"
    )
    skladova_plocha = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Skladová plocha (m²)"
    )
    objem_skladu = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Objem skladu (m³)"
    )

    velkostna_skupina = models.CharField(
        max_length=20,
        choices=[
            ('do 3 m²', 'do 3 m²'),
            ('od 3 m² do 5 m²', 'od 3 m² do 5 m²'),
            ('od 5 m² do 7 m²', 'od 5 m² do 7 m²'),
            ('od 7 m² do 15 m²', 'od 7 m² do 15 m²'),
            ('od 15 m²', 'od 15 m²')
        ],
        verbose_name="Veľkostná skupina skladu"
    )
    pristup_autom = models.CharField(
        max_length=50,
        choices=[
            ('Áno (rovno do skladu)', 'Áno (rovno do skladu)'),
            ('Áno (do areálu)', 'Áno (do areálu)'),
            ('Vonkajšie parkovisko', 'Vonkajšie parkovisko')
        ],
        verbose_name="Prístup autom"
    )
    vykurovanie = models.CharField(
        max_length=5,
        choices=[
            ('Nie', 'Nie'),
            ('Áno', 'Áno')
        ],
        verbose_name="Vykurovanie skladu"
    )
    pristup = models.CharField(
        max_length=20,
        choices=[
            ('Kluč', 'Kluč'),
            ('GSM', 'GSM'),
            ('Kód', 'Kód'),
            ('Aplikácia', 'Aplikácia')
        ],
        verbose_name="Prístup k skladu"
    )
    dvoje_dvere = models.CharField(
        max_length=3,
        choices=[
            ('Áno', 'Áno'),
            ('Nie', 'Nie')
        ],
        verbose_name="Dvoje dvere"
    )
    poznamka = models.TextField(
        max_length=1000,
        verbose_name="Poznámka"
    )
    stav_vsetci = models.CharField(
        max_length=20,
        choices=[
            ('Voľné', 'Voľné'),
            ('Prenajaté', 'Prenajaté'),
            ('Rezervované', 'Rezervované'),
            ('Nedostupný', 'Nedostupný')
        ],
        verbose_name="Stav prenájmu skladu (všetci)"
    )
    stav_prva_skupina = models.CharField(
        max_length=20,
        choices=[
            ('Voľné', 'Voľné'),
            ('Prenajaté', 'Prenajaté'),
            ('Rezervované', 'Rezervované'),
            ('Nedostupný', 'Nedostupný')
        ],
        verbose_name="Stav prenájmu skladu (prvá skupina čakajúcich)"
    )
    stav_dalsia_skupina = models.CharField(
        max_length=20,
        choices=[
            ('Voľné', 'Voľné'),
            ('Prenajaté', 'Prenajaté'),
            ('Rezervované', 'Rezervované'),
            ('Nedostupný', 'Nedostupný')
        ],
        verbose_name="Stav prenájmu skladu (ďalšia skupina čakajúcich)"
    )
    datum_ukoncenia_najmu = models.DateField(null=True, blank=True, verbose_name="Dátum ukončenia nájmu")
    datum_dostupnosti = models.DateField(null=True, blank=True, verbose_name="Dátum dostupnosti skladu pre všetky kategórie")
    datum_prveho_oznamenia = models.DateField(null=True, blank=True, verbose_name="Dátum prvého oznámenia o predĺžení nájmu")
    datum_druheho_oznamenia = models.DateField(null=True, blank=True, verbose_name="Dátum druhého oznámenia o predĺžení nájmu")
    datum_tretieho_oznamenia = models.DateField(null=True, blank=True, verbose_name="Dátum tretieho oznámenia o predĺžení nájmu")
    datum_prva_skupina = models.DateField(null=True, blank=True, verbose_name="Dátum oznámenia prvej čakacej skupiny")
    datum_druha_skupina = models.DateField(null=True, blank=True, verbose_name="Dátum oznámenia druhej čakacej skupiny")
    cislo_aktualne = models.CharField(
        max_length=20,
        verbose_name="Číslo Zmluvy (Aktuálne)"
    )
    cislo_predchadzajuce_1 = models.CharField(
        max_length=20,
        verbose_name="Číslo zmluvy (predchádzajúca 1)"
    )
    cislo_predchadzajuce_2 = models.CharField(
        max_length=20,
        verbose_name="Číslo zmluvy (predchádzajúce 2)"
    )
    cislo_predchadzajuce_3 = models.CharField(
        max_length=20,
        verbose_name="Číslo zmluvy (predchádzajúce 3)"
    )
    cislo_predchadzajuce_4 = models.CharField(
        max_length=20,
        verbose_name="Číslo zmluvy (predchádzajúce 4)"
    )
    cislo_predchadzajuce_5 = models.CharField(
        max_length=20,
        verbose_name="Číslo zmluvy (predchádzajúce 5)"
    )
    hlavne_foto = models.URLField(
        verbose_name="Hlavné foto skladu"
    )
    foto_dalsie_1 = models.URLField(
        verbose_name="Foto skladu ďalšie 1"
    )
    foto_dalsie_2 = models.URLField(
        verbose_name="Foto skladu ďalšie 2"
    )

    class Meta:
        verbose_name = "Sklad"
        verbose_name_plural = "Sklady"

class RozsirenePoistenie(models.Model):
    nazov = models.CharField(max_length=255, verbose_name="Názov poistenia")

    class Meta:
        verbose_name = "Rozšírené poistenie"
        verbose_name_plural = "Rozšírené poistenia"

    def __str__(self):
        return self.nazov

class UsersManager(BaseUserManager):
    def create_user(self, email, heslo=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(heslo)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, heslo=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('datum_narodenia', '2000-01-01')  # Указать дату по умолчанию
        return self.create_user(email, heslo, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    id_pouzivatela = models.AutoField(primary_key=True, verbose_name="ID používateľa")
    email = models.EmailField(max_length=255, unique=True, verbose_name="Email")
    heslo = models.CharField(max_length=255, verbose_name="Heslo")
    tel_cislo = models.CharField(max_length=15, verbose_name="Tel. čislo")
    povoleny_pristup_arealu_g = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: G"
    )
    povoleny_pristup_arealu_k = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: K"
    )
    povoleny_pristup_arealu_n = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: N"
    )
    povoleny_pristup_arealu_d = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: D"
    )
    povoleny_pristup_arealu_t = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: T"
    )
    povoleny_pristup_arealu_h = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: H"
    )
    pristupovy_kod_arealu_h = models.CharField(max_length=255, verbose_name="Prístupový kód do areálu, id: H")
    typ_pouzivatela = models.CharField(
        max_length=50,
        choices=[
            ('Vlastník', 'Vlastník'), ('Investor', 'Investor'), ('Vedúci', 'Vedúci'), ('Účtovník', 'Účtovník'),
            ('Správca', 'Správca'), ('Fyzická osoba', 'Fyzická osoba'),
            ('Právnická osoba (bez DPH)', 'Právnická osoba (bez DPH)'), ('Právnická osoba (platca DPH)', 'Právnická osoba (platca DPH)')
        ],
        verbose_name="Typ používateľa"
    )
    dostupne_sekcie = models.ManyToManyField(
        'Sekcia',
        verbose_name="Dostupné sekcie",
        blank=True
    )
    preferovany_jazyk = models.CharField(
        max_length=5,
        choices=[('SK', 'SK'), ('RU', 'RU'), ('EN', 'EN')],
        verbose_name="Preferovaný jazyk"
    )
    meno_nazov = models.CharField(max_length=255, null=True, verbose_name="Meno / Nazov")
    zastupeny = models.CharField(max_length=255, null=True, verbose_name="Zastúpený", blank=True)
    datum_narodenia = models.DateField(null=True, verbose_name="Dátum narodenia")
    adresa_bydliska_sidlo = models.CharField(max_length=255, null=True, verbose_name="Adresa bydliska / sídlo")
    ico = models.CharField(max_length=8, null=True, verbose_name="IČO")
    dic = models.CharField(max_length=10, null=True, verbose_name="DIČ")
    ic_dph = models.CharField(max_length=20, null=True, verbose_name="IČ DPH")
    tel_cislo_2 = models.CharField(max_length=15, verbose_name="Tel. číslo 2", blank=True, null=True,)
    povoleny_pristup_arealu_g_tel_2 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: G pre tel 2"
    )
    povoleny_pristup_arealu_k_tel_2 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: K pre tel 2"
    )
    povoleny_pristup_arealu_n_tel_2 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: N pre tel 2"
    )
    povoleny_pristup_arealu_d_tel_2 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: D pre tel 2"
    )
    povoleny_pristup_arealu_t_tel_2 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: T pre tel 2"
    )

    tel_cislo_3 = models.CharField(max_length=15, verbose_name="Tel. číslo 3")
    povoleny_pristup_arealu_g_tel_3 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: G pre tel 3"
    )
    povoleny_pristup_arealu_k_tel_3 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: K pre tel 3"
    )
    povoleny_pristup_arealu_n_tel_3 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: N pre tel 3"
    )
    povoleny_pristup_arealu_d_tel_3 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: D pre tel 3"
    )
    povoleny_pristup_arealu_t_tel_3 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: T pre tel 3"
    )

    tel_cislo_4 = models.CharField(max_length=15, verbose_name="Tel. číslo 4")
    povoleny_pristup_arealu_g_tel_4 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: G pre tel 4"
    )
    povoleny_pristup_arealu_k_tel_4 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: K pre tel 4"
    )
    povoleny_pristup_arealu_n_tel_4 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: N pre tel 4"
    )
    povoleny_pristup_arealu_d_tel_4 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: D pre tel 4"
    )
    povoleny_pristup_arealu_t_tel_4 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: T pre tel 4"
    )

    tel_cislo_5 = models.CharField(max_length=15, verbose_name="Tel. číslo 5")
    povoleny_pristup_arealu_g_tel_5 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: G pre tel 5"
    )
    povoleny_pristup_arealu_k_tel_5 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: K pre tel 5"
    )
    povoleny_pristup_arealu_n_tel_5 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: N pre tel 5"
    )
    povoleny_pristup_arealu_d_tel_5 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: D pre tel 5"
    )
    povoleny_pristup_arealu_t_tel_5 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: T pre tel 5"
    )

    tel_cislo_6 = models.CharField(max_length=15, verbose_name="Tel. číslo 6")
    povoleny_pristup_arealu_g_tel_6 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: G pre tel 6"
    )
    povoleny_pristup_arealu_k_tel_6 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: K pre tel 6"
    )
    povoleny_pristup_arealu_n_tel_6 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: N pre tel 6"
    )
    povoleny_pristup_arealu_d_tel_6 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: D pre tel 6"
    )
    povoleny_pristup_arealu_t_tel_6 = models.CharField(
        max_length=15,
        choices=[('Áno', 'Áno'), ('Nie', 'Nie'), ('Pozastavený', 'Pozastavený')],
        verbose_name="Povolený prístup do areálu id: T pre tel 6"
    )
    email_2 = models.EmailField(max_length=255, verbose_name="E-mail 2", blank=True)
    email_3 = models.EmailField(max_length=255, verbose_name="E-mail 3", blank=True)
    email_4 = models.EmailField(max_length=255, verbose_name="E-mail 4", blank=True)
    swift = models.CharField(max_length=10, verbose_name="SWIFT", blank=True)
    iban = models.CharField(max_length=34, verbose_name="IBAN", blank=True)
    cislo_karty = models.CharField(max_length=19, verbose_name="Číslo karty", blank=True)
    stav_prenajmu = models.CharField(
        max_length=50,
        choices=[
            ('-', '-'), ('aktívný, pripojený', 'aktívný, pripojený'), ('ukončený', 'ukončený'),
            ('aktívny, odpojený', 'aktívny, odpojený'), ('nový', 'nový'), ('zmluvný', 'zmluvný'),
            ('black list', 'black list')
        ],
        verbose_name="Stav prenájmu"
    )
    zmluva_aktualna = models.CharField(verbose_name="Zmluva (aktuálna)", blank=True)
    zmluva_aktualna_2 = models.CharField(verbose_name="Zmluva (aktuálna) 2", blank=True)
    zmluva_aktualna_3 = models.CharField(verbose_name="Zmluva (aktuálna) 3", blank=True)
    zmluva_aktualna_4 = models.CharField(verbose_name="Zmluva (aktuálna) 4", blank=True)
    zmluva_minula_1 = models.CharField(verbose_name="Zmluva (minula) 1", blank=True)
    zmluva_minula_2 = models.CharField(verbose_name="Zmluva (minula) 2", blank=True)
    zmluva_minula_3 = models.CharField(verbose_name="Zmluva (minula) 3", blank=True)
    zmluva_minula_4 = models.CharField(verbose_name="Zmluva (minula) 4", blank=True)
    zmluva_minula_5 = models.CharField(verbose_name="Zmluva (minula) 5", blank=True)
    id_skladu_zmluva_aktualna = models.CharField(max_length=255, verbose_name="id skladu Zmluva (aktuálna)", blank=True)
    id_skladu_2_zmluva_aktualna_2 = models.CharField(max_length=255, verbose_name="id skladu 2 Zmluva (aktuálna) 2", blank=True)
    id_skladu_3_zmluva_aktualna_3 = models.CharField(max_length=255, verbose_name="id skladu 3 Zmluva (aktuálna) 3", blank=True)
    id_skladu_4_zmluva_aktualna_4 = models.CharField(max_length=255, verbose_name="id skladu 4 Zmluva (aktuálna) 4", blank=True)
    id_skladu_5_zmluva_minula_1 = models.CharField(max_length=255, verbose_name="id skladu 5 Zmluva (minula) 1", blank=True)
    id_skladu_6_zmluva_minula_2 = models.CharField(max_length=255, verbose_name="id skladu 6 Zmluva (minula) 2", blank=True)
    id_skladu_7_zmluva_minula_3 = models.CharField(max_length=255, verbose_name="id skladu 7 Zmluva (minula) 3", blank=True)
    id_skladu_8_zmluva_minula_4 = models.CharField(max_length=255, verbose_name="id skladu 8 Zmluva (minula) 4", blank=True)
    id_skladu_9_zmluva_minula_5 = models.CharField(max_length=255, verbose_name="id skladu 9 Zmluva (minula) 5", blank=True)
    zdroj_navstevnosti = models.CharField(
        max_length=50,
        choices=[
            ('Bazoš', 'Bazoš'), ('Facebook', 'Facebook'), ('Google', 'Google'), ('Iné', 'Iné'),
            ('Instagram', 'Instagram'), ('Náš klient', 'Náš klient'), ('Od známych', 'Od známych'),
            ('Vonkajšia reklama', 'Vonkajšia reklama')
        ],
        verbose_name="Zdroj návštevnosti"
    )
    datum_uzavretia_zmluvy_aktualna = models.DateField(verbose_name="Dátum uzavretia zmluvy Zmluva (aktuálna)", blank=True, null=True)
    datum_uzavretia_zmluvy_aktualna_2 = models.DateField(verbose_name="Dátum uzavretia zmluvy Zmluva (aktuálna) 2", blank=True, null=True)
    datum_uzavretia_zmluvy_aktualna_3 = models.DateField(verbose_name="Dátum uzavretia zmluvy Zmluva (aktuálna) 3", blank=True, null=True)
    datum_uzavretia_zmluvy_aktualna_4 = models.DateField(verbose_name="Dátum uzavretia zmluvy Zmluva (aktuálna) 4", blank=True, null=True)
    datum_uzavretia_zmluvy_minula_1 = models.DateField(verbose_name="Dátum uzavretia zmluvy Zmluva (minula) 1", blank=True, null=True)
    datum_uzavretia_zmluvy_minula_2 = models.DateField(verbose_name="Dátum uzavretia zmluvy Zmluva (minula) 2", blank=True, null=True)
    datum_uzavretia_zmluvy_minula_3 = models.DateField(verbose_name="Dátum uzavretia zmluvy Zmluva (minula) 3", blank=True, null=True)
    datum_uzavretia_zmluvy_minula_4 = models.DateField(verbose_name="Dátum uzavretia zmluvy Zmluva (minula) 4", blank=True, null=True)
    datum_uzavretia_zmluvy_minula_5 = models.DateField(verbose_name="Dátum uzavretia zmluvy Zmluva (minula) 5", blank=True, null=True)
    sposob_platby = models.CharField(
        max_length=50,
        choices=[
            ('-', '-'), ('Online platba', 'Online platba'), ('Online platba (predplatné)', 'Online platba (predplatné)'),
            ('Hotovosť', 'Hotovosť'), ('Prevodom na účet', 'Prevodom na účet')
        ],
        verbose_name="Spôsob platby"
    )
    poznamka = models.TextField(verbose_name="Poznámka", blank=True)
    prenajimatel = models.ManyToManyField(
        'Prenajimatel',
        verbose_name="Prenajímateľ",
        blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsersManager()

    USERNAME_FIELD = 'email'  # Используем email как имя пользователя для логина
    REQUIRED_FIELDS = ['heslo', 'tel_cislo', 'meno_nazov']  # Обязательные поля, кроме USERNAME_FIELD

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Používateľ"
        verbose_name_plural = "Používatelia"

class Sekcia(models.Model):
    nazov = models.CharField(max_length=255, verbose_name="Názov sekcie")

    class Meta:
        verbose_name = "Sekcia"
        verbose_name_plural = "Sekcie"

    def __str__(self):
        return self.nazov
class Prenajimatel(models.Model):
    nazov = models.CharField(max_length=255, verbose_name="Názov prenajímateľa")

    class Meta:
        verbose_name = "Prenajímateľ"
        verbose_name_plural = "Prenajímatelia"

    def __str__(self):
        return self.nazov
