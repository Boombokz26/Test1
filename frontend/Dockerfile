# Используем базовый образ php:8.1-apache
FROM php:8.1-apache

# Настраиваем ServerName, чтобы убрать предупреждение в логах
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Обновляем систему и устанавливаем нужные пакеты (libpq-dev для PostgreSQL)
RUN apt-get update && apt-get install -y \
    libicu-dev \
    libpq-dev \
    libzip-dev \
    zip \
    unzip \
 && docker-php-ext-install pgsql pdo_pgsql \
 && docker-php-ext-enable pgsql pdo_pgsql \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Назначаем рабочую директорию
WORKDIR /var/www/html

# Копируем всё из текущего контекста в /var/www/html контейнера
COPY . /var/www/html/

RUN rm -f /var/www/html/index.php

# Открываем порт 80 (Apache по умолчанию)
EXPOSE 80

# Запускаем Apache
CMD ["apache2-foreground"]
