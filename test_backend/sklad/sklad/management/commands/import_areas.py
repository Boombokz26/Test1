import pandas as pd
from django.core.management.base import BaseCommand
from sklad.models import Areas, Vybavenie  # Предположим, что `Vybavenie` — это модель для дополнительных объектов

class Command(BaseCommand):
    help = 'Import data from Areas.xlsx to Areas model'

    def handle(self, *args, **kwargs):
        # Шаг 1: Загрузка данных из Excel
        file_path = '/app/sklad/import_data/Areas.xlsx'
        data = pd.read_excel(file_path)

        # Шаг 2: Перенос данных в модель Areas
        for index, row in data.iterrows():
            area = Areas(
                ID_arealu=row['ID areálu'],
                adresa_zmluva=row['Adresa areálu (pre zmluvu)'],
                adresa_formular=row['Adresa areálu (pre formular)'],
                pristup=row['Prístup k areálu'],
                tel_cislo_brany=row['Tel. číslo brány na prístup do areálu'],
                poistenie=row['Základné poistenie skladov'],
                osvetlenie=row['Osvetlenie areálu'],
                poznamka=row['Poznámka']
            )
            area.save()

            # Добавление значений в поле ManyToMany
            if 'Ďalšie vybavenie' in row and pd.notna(row['Ďalšie vybavenie']):
                dalsie_vybavenie_values = row['Ďalšie vybavenie'].split(',')
                vybavenie_objects = []

                for value in dalsie_vybavenie_values:
                    vybavenie = Vybavenie.objects.filter(nazov=value.strip()).first()
                    if vybavenie:
                        vybavenie_objects.append(vybavenie)

                area.dalsie_vybavenie.set(vybavenie_objects)

        self.stdout.write(self.style.SUCCESS("Данные успешно загружены в модель Areas."))
