from django.shortcuts import render, redirect
from .rent_sklad_form import WarehouseRentalForm
from django.http import JsonResponse
from .models import Warhouses
from django.views.decorators.csrf import csrf_exempt
from datetime import date, timedelta
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm

def home(request):
    return render(request, 'home.html')

def rent_warehouse(request):
    if request.method == 'POST':
        form = WarehouseRentalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://top-sklad.sk')
        else:
            return render(request, 'rent_warehouse.html', {'form': form})
    else:
        form = WarehouseRentalForm()
        return render(request, 'rent_warehouse.html', {'form': form})

@csrf_exempt
def get_lokalita(request):
    """
    Возвращает список локалит (adresa_formular), где stav_vsetci="Voľné",
    фильтруя по типу склада (typ_skladu).
    """
    typ_skladu = request.GET.get('typ_skladu')
    lokalita_values = (
        Warhouses.objects
        .filter(stav_vsetci="Voľné", typ_skladu=typ_skladu)
        .values_list('adresa_formular', flat=True)
        .distinct()
    )
    return JsonResponse(list(lokalita_values), safe=False)

@csrf_exempt
def get_velkost_skladu(request):
    """
    Возвращает список velkostna_skupina, фильтруя по typ_skladu и adresa_formular.
    """
    typ_skladu = request.GET.get('typ_skladu')
    lokalita = request.GET.get('lokalita')
    velkost_values = (
        Warhouses.objects
        .filter(stav_vsetci="Voľné", typ_skladu=typ_skladu, adresa_formular=lokalita)
        .values_list('velkostna_skupina', flat=True)
        .distinct()
    )
    return JsonResponse(list(velkost_values), safe=False)

@csrf_exempt
def get_cislo_skladu(request):
    """
    Возвращает список id_skladu, фильтруя по typ_skladu, lokalita, velkost_skladu.
    """
    typ_skladu = request.GET.get('typ_skladu')
    lokalita = request.GET.get('lokalita')
    velkost = request.GET.get('velkost_skladu')
    cisla_values = (
        Warhouses.objects
        .filter(
            stav_vsetci="Voľné",
            typ_skladu=typ_skladu,
            adresa_formular=lokalita,
            velkostna_skupina=velkost
        )
        .values_list('id_skladu', flat=True)
        .distinct()
    )
    return JsonResponse(list(cisla_values), safe=False)

@csrf_exempt
def get_doba_prenajmu(request):
    """
    Возвращает варианты doba_prenajmu для выбранного cislo_skladu.
    Пример: 1 mesiac, 3 mesiace, 6 mesiacov, 12 mesiacov.
    """
    cislo = request.GET.get('cislo_skladu')
    from decimal import Decimal
    try:
        sklad_obj = Warhouses.objects.get(id_skladu=cislo, stav_vsetci="Voľné")
        X = sklad_obj.cena_bez_dph_mesiac
        XX = X
        XXX = sklad_obj.cena_bez_dph_polrok
        XXXX = sklad_obj.cena_bez_dph_rok

        Y = X
        YY = 3 * XX
        YYY = 6 * XXX
        YYYY = 12 * XXXX

        doba_options = [
            {'value': '1mes', 'text': f"1 mesiac za {X} € / mes. ({Y} € okamžite + kaucia za 1 mes.)"},
            {'value': '3mes', 'text': f"3 mesiace za {XX} € / mes. - ({YY} € okamžite + kaucia za 1 mes.)"},
            {'value': '6mes', 'text': f"6 mesiacov za {XXX} € / mes. - ({YYY} € okamžite + kaucia za 1 mes.)"},
            {'value': '12mes','text': f"12 mesiacov za {XXXX} € / mes. - ({YYYY} € okamžite + kaucia za 1 mes.)"}
        ]
        return JsonResponse(doba_options, safe=False)
    except Warhouses.DoesNotExist:
        return JsonResponse([], safe=False)

@csrf_exempt
def get_sklad_info(request):
    """
    Возвращает информацию о складе (plocha, poschodie, пути к фото) для выбранного cislo_skladu.
    """
    cislo_skladu = request.GET.get('cislo_skladu')
    try:
        obj = Warhouses.objects.get(id_skladu=cislo_skladu, stav_vsetci="Voľné")
        data = {
            "plocha": obj.skladova_plocha,
            "poschodie": obj.poschodie,
            "foto_main": obj.hlavne_foto,
            "foto_extra1": obj.foto_dalsie_1,
            "foto_extra2": obj.foto_dalsie_2,
        }
    except Warhouses.DoesNotExist:
        data = {}
    return JsonResponse(data)

@csrf_exempt
def validate_date_range(request):
    """
    Для prenajat_sklad_od: min=сегодня, max=сегодня+14
    """
    today = date.today()
    min_date = today
    max_date = today + timedelta(days=14)
    return JsonResponse({
        'min_date': min_date.isoformat(),
        'max_date': max_date.isoformat(),
    })

@csrf_exempt
def validate_birth_date_range(request):
    """
    Для dátum_narodenia: 18..90 лет
    """
    today = date.today()
    max_date = today.replace(year=today.year - 18)
    min_date = today.replace(year=today.year - 90)
    return JsonResponse({
        'min_date': min_date.isoformat(),
        'max_date': max_date.isoformat(),
    })

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            heslo = form.cleaned_data['heslo']
            user = authenticate(request, username=email, password=heslo)
            if user is not None:
                login(request, user)
                return redirect('moj_ucet')
            else:
                error = "Nesprávne prihlasovacie údaje."
                return render(request, 'login.html', {'form': form, 'error': error})
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def moj_ucet(request):
    return render(request, 'moj_ucet.html')
