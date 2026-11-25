FROM python:3.12-slim

# Забороняємо Python створювати .pyc-файли
ENV PYTHONDONTWRITEBYTECODE=1

# Логи Python одразу виводяться в консоль контейнера
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Встановлюємо системні залежності
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Спочатку копіюємо залежності для кешування Docker layer
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Копіюємо код застосунку
COPY . .

# Каталог для SQLite, який буде підключено як volume
RUN mkdir -p /app/data /app/media /app/log /app/staticfiles

EXPOSE 8000

ENTRYPOINT ["sh", "/app/docker-entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]