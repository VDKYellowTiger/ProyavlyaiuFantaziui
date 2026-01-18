import cv2
import numpy as np
import os
import random

def load_image():
    path = "shuka.jpg"

    if not os.path.exists(path):
        print("Файл shuka.jpg не найден в папке проекта!")
        exit()

    image = cv2.imread(path)

    if image is None:
        print("Файл найден, но это не изображение.")
        exit()

    return image, path

def show_info(image):
    height, width, depth = image.shape
    print("Параметры изображения:")
    print("Высота:", height)
    print("Ширина:", width)
    print("Глубина:", depth)
    print("Тип данных:", image.dtype)

def main_menu():
    print("\nВыберите действие:")
    print("1 – Применить эффект")
    print("2 – Сохранить изображение")
    return input("Ваш выбор: ")

def effects_menu():
    print("\nВыберите эффект:")
    print("1 – Черно-белое изображение")
    print("2 – Отразить по вертикали")
    print("3 – Отразить по горизонтали")
    print("4 – Закрасить случайный квадрат")
    print("5 – Добавить шум")
    print("6 – Изменить яркость")
    print("7 – Размытие (blur)")
    print("8 – Изменить контраст")
    return input("Ваш выбор: ")

def to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def flip_vertical(image):
    return cv2.flip(image, 1)

def flip_horizontal(image):
    return cv2.flip(image, 0)

def random_square(image):
    colors = {
        "красный": (0, 0, 255),
        "зеленый": (0, 255, 0),
        "синий": (255, 0, 0)
    }

    print("Доступные цвета:", list(colors.keys()))
    color_name = input("Выберите цвет: ")

    if color_name not in colors:
        print("Такого цвета нет")
        return image

    h, w, _ = image.shape
    size = random.randint(20, 100)

    x = random.randint(0, w - size)
    y = random.randint(0, h - size)

    image[y:y + size, x:x + size] = colors[color_name]

    return image

def add_noise(image):
    h, w, d = image.shape

    count = int(h * w * 0.1)

    for i in range(count):
        x = random.randint(0, w - 1)
        y = random.randint(0, h - 1)

        image[y, x] = [
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        ]

    return image

def change_brightness(image):
    value = int(input("Введите значение яркости (-100...100): "))
    return cv2.convertScaleAbs(image, alpha=1, beta=value)

def blur_image(image):
    return cv2.GaussianBlur(image, (15, 15), 0)

def change_contrast(image):
    value = float(input("Введите коэффициент контраста (например 1.5): "))
    return cv2.convertScaleAbs(image, alpha=value, beta=0)

def save_image(image):
    while True:
        name = input("Введите имя для сохранения (например result.png): ")

        try:
            cv2.imwrite(name, image)
            full_path = os.path.abspath(name)
            print("Изображение успешно сохранено:", full_path)
            break
        except:
            print("Некорректное имя файла. Попробуйте снова.")

def main():
    image, path = load_image()

    show_info(image)

    while True:
        choice = main_menu()

        if choice == "1":
            effect = effects_menu()

            if effect == "1":
                image = to_gray(image)
            elif effect == "2":
                image = flip_vertical(image)
            elif effect == "3":
                image = flip_horizontal(image)
            elif effect == "4":
                image = random_square(image)
            elif effect == "5":
                image = add_noise(image)
            elif effect == "6":
                image = change_brightness(image)
            elif effect == "7":
                image = blur_image(image)
            elif effect == "8":
                image = change_contrast(image)
            else:
                print("Неверный выбор")

        elif choice == "2":
            save_image(image)
            break

        else:
            print("Неверный пункт меню")

if __name__ == "__main__":
    main()