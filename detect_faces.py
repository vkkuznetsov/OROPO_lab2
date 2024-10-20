import cv2
import glob
import os


def detect_faces(image_path):
    # Загружаем классификатор лиц (используем Haar каскады)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Читаем изображение
    image = cv2.imread(image_path)
    # Проверяем, удалось ли загрузить изображение
    if image is None:
        print(f"Не удалось загрузить изображение: {image_path}")
        return

    # Применяем увеличение контраста
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # Находим лица с настроенными параметрами
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7, minSize=(100, 100))

    # Печатаем результат
    print(f"Файл: {os.path.basename(image_path)} - Найдено {len(faces)} лиц")

    # Сохраняем обработанные лица
    for (x, y, w, h) in faces:
        face = image[y:y + h, x:x + w]
        output_path = f'output/face_{os.path.basename(image_path).split(".")[0]}_{len(faces)}.jpg'
        cv2.imwrite(output_path, face)
        print(f"Сохранено: {output_path}")


if __name__ == "__main__":
    # Используем glob для поиска всех файлов с изображениями в ./photos/
    image_paths = glob.glob('./photos/*')

    # Проходим по каждому изображению
    for image_path in image_paths:
        detect_faces(image_path)
