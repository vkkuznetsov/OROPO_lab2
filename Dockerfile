# Используем базовый образ Python
FROM python:3.11

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Копируем файлы проекта в контейнер
COPY . /app

# Переходим в директорию с приложением
WORKDIR /app

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем скрипт
CMD ["python", "detect_faces.py"]
