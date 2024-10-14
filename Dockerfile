# Используем slim образ Python
FROM python:3.11-slim

# Устанавливаем зависимости для OpenCV
RUN apt-get update && \
    apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Устанавливаем необходимые Python пакеты
RUN pip install --no-cache-dir opencv-python

# Копируем приложение в контейнер
COPY . /app
WORKDIR /app

# Команда для запуска приложения
CMD ["python", "detect_faces.py"]
