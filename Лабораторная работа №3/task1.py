def find_item_index(list, item): # TODO Напишите функцию для поиска индекса товара
    for i in range(len(list)):
        if list[i] == item:
            return i + 1
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['яблоко', 'банан', 'персик']:
    index_item = find_item_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")


def find_item_index(list, item): #TODO Напишите функцию для поиска индекса товара
    for i in range(len(list)):
        if list[i] == item:
            return i + 1
        return None

