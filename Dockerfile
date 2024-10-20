FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    dos2unix

COPY . /app

WORKDIR /app

RUN dos2unix detect_faces.py

RUN pip install -r requirements.txt
# сиашмодим екзекьюшен на файл
RUN chmod +x /app/detect_faces.py
# не самый лучший способ но терпимый
ENV PATH="/app:${PATH}"

# Запускаем скрипта с указанием аргумента
CMD ["detect_faces.py", "/app/photos/br1.jpg"]
# закоменить сверху и раскоментить снизу чтобы проверить дефолтный путь до photos
# CMD ["detect_faces.py"]