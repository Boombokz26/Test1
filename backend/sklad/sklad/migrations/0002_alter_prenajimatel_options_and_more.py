# Generated by Django 4.2.16 on 2024-12-01 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prenajimatel',
            options={'verbose_name': 'Prenajímateľ', 'verbose_name_plural': 'Prenajímatelia'},
        ),
        migrations.AlterModelOptions(
            name='rozsirenepoistenie',
            options={'verbose_name': 'Rozšírené poistenie', 'verbose_name_plural': 'Rozšírené poistenia'},
        ),
        migrations.AlterModelOptions(
            name='sekcia',
            options={'verbose_name': 'Sekcia', 'verbose_name_plural': 'Sekcie'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Používateľ', 'verbose_name_plural': 'Používatelia'},
        ),
        migrations.AlterModelOptions(
            name='vybavenie',
            options={'verbose_name': 'Vybavenie', 'verbose_name_plural': 'Vybavenia'},
        ),
        migrations.AlterModelOptions(
            name='warhouses',
            options={'verbose_name': 'Sklad', 'verbose_name_plural': 'Sklady'},
        ),
    ]
