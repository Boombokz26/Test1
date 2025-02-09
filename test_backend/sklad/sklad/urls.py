from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    rent_warehouse, home, get_lokalita, get_velkost_skladu, get_cislo_skladu,
    get_doba_prenajmu, validate_date_range, validate_birth_date_range,
    login_view, logout_view, moj_ucet, get_sklad_info
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('rent/', rent_warehouse, name='rent_warehouse'),

    # AJAX endpoints
    path('ajax/lokalita/', get_lokalita, name='get_lokalita'),
    path('ajax/velkost/', get_velkost_skladu, name='get_velkost_skladu'),
    path('ajax/cislo_skladu/', get_cislo_skladu, name='get_cislo_skladu'),
    path('ajax/doba_prenajmu/', get_doba_prenajmu, name='get_doba_prenajmu'),
    path('ajax/get_sklad_info/', get_sklad_info, name='get_sklad_info'),

    # Валидация дат
    path('validate-date-range/', validate_date_range, name='validate_date_range'),
    path('validate-birth-date-range/', validate_birth_date_range, name='validate_birth_date_range'),

    # Авторизация
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('moj-ucet/', moj_ucet, name='moj_ucet'),
]

# При DEBUG = True Django может раздавать и статику, и медиа
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Если используете поля ImageField/FileField и храните файлы в MEDIA_ROOT
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
