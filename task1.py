numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
i = 0
summa = 0
for x in numbers:
    if numbers[i] is not None:
        summa = summa + numbers[i]
    i += 1
i = 0
for x in numbers:
    if numbers[i] is None:
        numbers[i] = summa / len(numbers)
    i += 1
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
