from django.contrib import admin
from .models import Areas, Warhouses, Users, RozsirenePoistenie, Vybavenie, Sekcia, Prenajimatel
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from .forms import CustomUserCreationForm

admin.site.register(Areas)
admin.site.register(RozsirenePoistenie)
admin.site.register(Vybavenie)
admin.site.register(Sekcia)
admin.site.register(Prenajimatel)

class CustomUserAdmin(UserAdmin):
    model = Users
    add_form = CustomUserCreationForm  # Используем нашу кастомную форму для создания пользователя
    
    list_display = ('email', 'meno_nazov', 'stav_prenajmu')
    list_filter = ('typ_pouzivatela', 'stav_prenajmu')
    search_fields = ('email', 'meno_nazov')
    ordering = ('email',)
    filter_horizontal = ('dostupne_sekcie', 'prenajimatel',)

    # Убираем 'id_pouzivatela' из fieldsets, так как он не предусмотрен в форме
    fieldsets = (
        (_('Používateľské info'), {
            'fields': (
                'email',
                'heslo',  # Поле пароля
                'tel_cislo',
                'typ_pouzivatela',
                'dostupne_sekcie',
                'stav_prenajmu',
                'preferovany_jazyk',
                'is_active',
                'is_staff'
            )
        }),
        (_('Zákaznícke info'), {
            'fields': (
                'meno_nazov',
                'zastupeny',
                'datum_narodenia',
                'povoleny_pristup_arealu_g',
                'povoleny_pristup_arealu_k',
                'povoleny_pristup_arealu_n',
                'povoleny_pristup_arealu_d',
                'povoleny_pristup_arealu_t',
                'povoleny_pristup_arealu_h',
                'pristupovy_kod_arealu_h',
                'tel_cislo_2',
                'povoleny_pristup_arealu_g_tel_2',
                'povoleny_pristup_arealu_k_tel_2',
                'povoleny_pristup_arealu_n_tel_2',
                'povoleny_pristup_arealu_d_tel_2',
                'povoleny_pristup_arealu_t_tel_2',
                'tel_cislo_3',
                'povoleny_pristup_arealu_g_tel_3',
                'povoleny_pristup_arealu_k_tel_3',
                'povoleny_pristup_arealu_n_tel_3',
                'povoleny_pristup_arealu_d_tel_3',
                'povoleny_pristup_arealu_t_tel_3',
                'tel_cislo_4',
                'povoleny_pristup_arealu_g_tel_4',
                'povoleny_pristup_arealu_k_tel_4',
                'povoleny_pristup_arealu_n_tel_4',
                'povoleny_pristup_arealu_d_tel_4',
                'povoleny_pristup_arealu_t_tel_4',
                'tel_cislo_5',
                'povoleny_pristup_arealu_g_tel_5',
                'povoleny_pristup_arealu_k_tel_5',
                'povoleny_pristup_arealu_n_tel_5',
                'povoleny_pristup_arealu_d_tel_5',
                'povoleny_pristup_arealu_t_tel_5',
                'tel_cislo_6',
                'povoleny_pristup_arealu_g_tel_6',
                'povoleny_pristup_arealu_k_tel_6',
                'povoleny_pristup_arealu_n_tel_6',
                'povoleny_pristup_arealu_d_tel_6',
                'povoleny_pristup_arealu_t_tel_6',
                'email_2',
                'email_3',
                'email_4'
            )
        }),
        (_('Fakturačné údaje'), {
            'fields': (
                'adresa_bydliska_sidlo',
                'ico',
                'dic',
                'ic_dph',
                'swift',
                'iban',
                'cislo_karty',
                'sposob_platby',
                'prenajimatel'
            )
        }),
        (_('Objednávkové info'), {
            'fields': (
                'zmluva_aktualna',
                'zmluva_aktualna_2',
                'zmluva_aktualna_3',
                'zmluva_aktualna_4',
                'zmluva_minula_1',
                'zmluva_minula_2',
                'zmluva_minula_3',
                'zmluva_minula_4',
                'zmluva_minula_5',
                'id_skladu_zmluva_aktualna',
                'id_skladu_2_zmluva_aktualna_2',
                'id_skladu_3_zmluva_aktualna_3',
                'id_skladu_4_zmluva_aktualna_4',
                'id_skladu_5_zmluva_minula_1',
                'id_skladu_6_zmluva_minula_2',
                'id_skladu_7_zmluva_minula_3',
                'id_skladu_8_zmluva_minula_4',
                'id_skladu_9_zmluva_minula_5',
                'datum_uzavretia_zmluvy_aktualna',
                'datum_uzavretia_zmluvy_aktualna_2',
                'datum_uzavretia_zmluvy_aktualna_3',
                'datum_uzavretia_zmluvy_aktualna_4',
                'datum_uzavretia_zmluvy_minula_1',
                'datum_uzavretia_zmluvy_minula_2',
                'datum_uzavretia_zmluvy_minula_3',
                'datum_uzavretia_zmluvy_minula_4',
                'datum_uzavretia_zmluvy_minula_5'
            )
        }),
        (_('Other Info'), {
            'fields': (
                'poznamka',
                'zdroj_navstevnosti'
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'heslo', 'tel_cislo', 'meno_nazov', 'typ_pouzivatela', 
                'stav_prenajmu', 'is_staff', 'is_superuser'
            )
        }),
    )

class CustomWarhouseAdmin(admin.ModelAdmin):
    model = Warhouses
    list_display = ('id_skladu', 'adresa_formular', 'stav_vsetci_colored', 'cena_bez_dph_mesiac', 'cena_bez_dph_polrok', 'cena_bez_dph_rok')
    list_filter = ('typ_skladu', 'adresa_formular', 'stav_vsetci')
    search_fields = ('id_skladu', 'adresa_formular')
    ordering = ('id_skladu',)

    def stav_vsetci_colored(self, obj):
        if obj.stav_vsetci == "Prenajaté":
            return format_html('<span style="color:red;">{}</span>', obj.stav_vsetci)
        elif obj.stav_vsetci == "Voľné":
            return format_html('<span style="color:green;">{}</span>', obj.stav_vsetci)
        return obj.stav_vsetci

    stav_vsetci_colored.short_description = "Stav"

admin.site.register(Warhouses, CustomWarhouseAdmin)
admin.site.register(Users, CustomUserAdmin)
