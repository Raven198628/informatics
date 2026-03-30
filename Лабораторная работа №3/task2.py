def find_common_participants(group1, group2, separator): # TODO Напишите функцию find_common_participants
    separator = ","
    list1 = group1.split(separator)
    list2 = group2.split(separator)

    common = []
    for name in list1:
        if name in list2:
            common.append(name)

    return sorted(common)


participants_first_group = "Ивнов|Петров|Сидоров"  # TODO Напишите функцию find_common_participants
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, "|")
print(result)



participants_first_group = "Иванов|Петров|Сидоров"  # TODO Провеьте работу функции с разделителем отличным от запятой
participants_second_group = "Петров|Сидоров|Смирнов"

