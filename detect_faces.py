#!/usr/bin/env python3

import cv2
import glob
import os
import sys


def detect_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, minSize=(50, 50))
    print(f"Файл: {os.path.basename(image_path)} - Найдено {len(faces)} лиц")

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 15)

    output_path = f'output/detected_{os.path.basename(image_path)}'
    cv2.imwrite(output_path, image)
    print(f"Сохранено: {output_path}")


if __name__ == "__main__":
    if not os.path.exists('output'):
        os.makedirs('output')

    if len(sys.argv) > 1:
        image_paths = [sys.argv[1]]
    else:
        image_paths = glob.glob('./photos/*')

    for image_path in image_paths:
        detect_faces(image_path)
