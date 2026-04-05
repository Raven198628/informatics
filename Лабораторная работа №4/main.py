# TODO ИМПОРТИРОВАТЬ НЕОБХОДИМЫЕ МОДУЛИ
import csv  # Модуль для работы csv
import json  # Модуль для работы json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"  # Имена входного и выходного файла


def task() -> None:
    # TODO СЧИТАТЬ СОДЕРЖИМОЕ CSV ФАЙЛА
    data = []
    with open(INPUT_FILENAME, 'r', encoding="utf-8") as f:  # Отркиываем csv файл для чтения в текстовом режимое с кодировкой UTF-8
        reader = csv.DictReader(f, delimiter=',')  # Создаем диктридер который  испульзует первую строку как заголовки столбцов, возвращает каждую следующую строку как словарь
        for row in reader:
            data.append(row)

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding="utf-8") as j_f:  # Открываем JSON файл для записи с кодировкой UTF-8
        json.dump(data, j_f, indent=4, ensure_ascii=False)  # Сериализуем Пайтон объект в JSON формат, задаем отступ в 4 пробела и сохраняем символы


if __name__ == '__main__':   # Нужно для проверки
    task()  # Выполняем конвертацию CSV в JSON

    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:  # Октрываем и выиводим содержимаое JSON
        for line in output_f:
            print(line, end="")  # Выводим построчно
