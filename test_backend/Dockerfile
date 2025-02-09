# Используем базовый образ Python 3.9
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл requirements.txt в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из папки backend в контейнер
COPY . /app/

# Перемещаем рабочую директорию к проекту Django
WORKDIR /app/sklad

# Задаем команду по умолчанию для запуска
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
