import json
import os


def task() -> float:
    filename = [f for f in os.listdir('.') if f.endswith('.json')][0]  # Получаем список файлов в текущей папке
    with open(filename, 'r', encoding='utf-8') as file:  # Открываем найденный файл
        data = json.load(file)  # Преобразуем JSON в пайтон

    total = sum(item['score'] * item['weight'] for item in data)  # Вычисляем сумму произведений
    return round(total, 3)  # Округляем до тысячных результат и возвращаем


print(task())