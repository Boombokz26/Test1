import pandas as pd
from django.core.management.base import BaseCommand
from sklad.models import Warhouses, RozsirenePoistenie
from datetime import datetime

def parse_date(value):
    if isinstance(value, str) and value.strip():
        try:
            # Обработка формата dd.mm.yyyy
            return datetime.strptime(value, '%d.%m.%Y').date()
        except ValueError:
            return None
    return None

class Command(BaseCommand):
    help = 'Import warehouses data from Warehouses.xlsx into the database.'

    def handle(self, *args, **kwargs):
        file_path = '/app/sklad/import_data/Warehouses.xlsx'

        try:
            data = pd.read_excel(file_path)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
            return

        for index, row in data.iterrows():
            self.stdout.write(f'Processing row {index + 1}: {row.to_dict()}')
            warehouse = Warhouses(
                adresa_zmluva=row['Adresa areálu (pre zmluvu)'],
                adresa_formular=row['Adresa areálu (pre formular)'],
                typ_skladu=row['Typ skladu'],
                cislo_skladu=row['Číslo skladu'],
                id_skladu=row['ID skladu'],
                poschodie=row['Poschodie'],
                cena_bez_dph_mesiac=row['Cena bez DPH\n(1 krát za mesiac)'],
                cena_bez_dph_polrok=row['Cena bez DPH\n(1 krát za polroka)'],
                cena_bez_dph_rok=row['Cena bez DPH\n(1 krát za rok)'],
                cena_s_dph_mesiac=row['Cena s DPH\n(1 krát za mesiac)'],
                cena_s_dph_polrok=row['Cena s DPH\n(1 krát za polroka)'],
                cena_s_dph_rok=row['Cena s DPH\n(1 krát za rok)'],
                dph_mesiac=row['DPH\n(1 krát za mesiac)'],
                dph_polrok=row['DPH\n(1 krát za polroka)'],
                dph_rok=row['DPH\n(1 krát za rok)'],
                kaucia_mesiac=row['Kaucia pre\nprenájom skladov \n(1 krát za mesiac)'],
                kaucia_polrok=row['Kaucia pre\nprenájom skladov\n(1 krát za polroka)'],
                kaucia_rok=row['Kaucia pre\nprenájom skladov\n(1 krát za rok)'],
                poistenie=row['Základné poistenie skladov'],
                doplatok_poistenie_5000=row['Doplatok mesačne k cene za predĺžené poistenie Do 5000€'],
                doplatok_poistenie_7000=row['Mesačný príplatok k cene predĺženého poistenia Do 7000€'],
                doplatok_poistenie_10000=row['Doplatok mesačne k cene za predĺžené poistenie Do 10000€'],
                dlzka_skladu=row['Dĺžka skladu\n(m.)'],
                sirka_skladu=row['Šírka skladu\n(m.)'],
                vyska_skladu=row['Výška skladu\n(m.)'],
                sirka_dveri=row['Šírka dverí (m.)'],
                vyska_dveri=row['Výška dverí (m.)'],
                skladova_plocha=row['Skladová plocha (m²)'],
                objem_skladu=row['Objem skladu\n(m³)'],
                velkostna_skupina=row['Veľkostná skupina skladu'],
                pristup_autom=row['Prístup autom'],
                vykurovanie=row['Vykurovanie skladu'],
                pristup=row['Prístup k skladu'],
                dvoje_dvere=row['Dvoje dvere'],
                poznamka=row['Poznámka'],
                stav_vsetci=row['Stav prenájmu skladu (všetci)'],
                stav_prva_skupina=row['Stav prenájmu skladu (prvá skupina čakajúcich)'],
                stav_dalsia_skupina=row['Stav prenájmu skladu (ďalšia skupina čakajúcich)'],
                datum_ukoncenia_najmu=parse_date(row['Dátum ukončenia nájmu']) or None,
                datum_dostupnosti=parse_date(row['Dátum dostupnosti skladu pre všetky kategórie']) or None,
                datum_prveho_oznamenia=parse_date(row['Dátum prvého oznámenia o predĺžení nájmu']) or None,
                datum_druheho_oznamenia=parse_date(row['Dátum druhého oznámenia o predĺžení nájmu']) or None,
                datum_tretieho_oznamenia=parse_date(row['Dátum tretieho oznámenia o predĺžení nájmu']) or None,
                datum_prva_skupina=parse_date(row['Dátum oznámenia prvej čakacej skupiny']) or None,
                datum_druha_skupina=parse_date(row['Dátum oznámenia druhej čakacej skupiny']) or None,
                cislo_aktualne=row['Číslo Zmluvy (Aktuálne)'],
                cislo_predchadzajuce_1=row['Číslo zmluvy (predchádzajúca 1)'],
                cislo_predchadzajuce_2=row['Číslo zmluvy (predchádzajúce 2)'],
                cislo_predchadzajuce_3=row['Číslo zmluvy (predchádzajúce 3)'],
                cislo_predchadzajuce_4=row['Číslo zmluvy (predchádzajúce 4)'],
                cislo_predchadzajuce_5=row['Číslo zmluvy (predchádzajúce 5)'],
                hlavne_foto=row['Hlavné foto skladu'],
                foto_dalsie_1=row['Foto skladu ďalšie 1'],
                foto_dalsie_2=row['Foto skladu ďalšie 2']
            )

            warehouse.save()
            
        self.stdout.write(self.style.SUCCESS('Warehouse data successfully imported.'))
