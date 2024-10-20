# OROPO_lab2
Выполнение 2 лаб работы по предмету  основы разработки открытого программного обеспечения

# Установа 
## БИЛД
```bash
docker build -t viktest .
```
## ЗАПУСК
```bash
docker run -v ${PWD}/output:/app/output --rm viktest
```
## УДАЛЕНИЕ ПОСЛЕ ТЕСТОВ
```bash
docker images
docker rmi viktest
docker images
```
# Либо воруем с докерхаба
```bash
docker pull vikkto/opencv-face-detector:latest
```
Результат будет в output (прокидываем volume) и в выводе консоли
