# Generated by Django 4.2.16 on 2024-12-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0003_users_groups_users_is_active_users_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warhouses',
            name='datum_dostupnosti',
            field=models.DateField(blank=True, null=True, verbose_name='Dátum dostupnosti skladu pre všetky kategórie'),
        ),
        migrations.AlterField(
            model_name='warhouses',
            name='datum_druha_skupina',
            field=models.DateField(blank=True, null=True, verbose_name='Dátum oznámenia druhej čakacej skupiny'),
        ),
        migrations.AlterField(
            model_name='warhouses',
            name='datum_druheho_oznamenia',
            field=models.DateField(blank=True, null=True, verbose_name='Dátum druhého oznámenia o predĺžení nájmu'),
        ),
        migrations.AlterField(
            model_name='warhouses',
            name='datum_prva_skupina',
            field=models.DateField(blank=True, null=True, verbose_name='Dátum oznámenia prvej čakacej skupiny'),
        ),
        migrations.AlterField(
            model_name='warhouses',
            name='datum_prveho_oznamenia',
            field=models.DateField(blank=True, null=True, verbose_name='Dátum prvého oznámenia o predĺžení nájmu'),
        ),
        migrations.AlterField(
            model_name='warhouses',
            name='datum_tretieho_oznamenia',
            field=models.DateField(blank=True, null=True, verbose_name='Dátum tretieho oznámenia o predĺžení nájmu'),
        ),
        migrations.AlterField(
            model_name='warhouses',
            name='datum_ukoncenia_najmu',
            field=models.DateField(blank=True, null=True, verbose_name='Dátum ukončenia nájmu'),
        ),
    ]
