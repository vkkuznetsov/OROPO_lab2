import cv2

def detect_faces(image_path):
    # Загружаем классификатор лиц (используем Haar каскады)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Читаем изображение
    image = cv2.imread(image_path)
    # Переводим в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Находим лица
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Печатаем результат
    print(f"Найдено {len(faces)} лиц")

if __name__ == "__main__":
    detect_faces('path_to_image.jpg')  # Укажите путь к изображению
