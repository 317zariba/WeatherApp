# ---- Базовый образ ----
FROM python:3.12-slim

# ---- Рабочая директория ----
WORKDIR /app

# ---- Устанавливаем зависимости ----
# Сначала копируем requirements.txt, если он есть
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# ---- Копируем всё приложение ----
COPY . .

# ---- Устанавливаем переменные окружения ----
# (чтобы Python не кешировал и Django не спрашивал ввод)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# ---- Выполняем миграции и собираем статику при старте ----
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
