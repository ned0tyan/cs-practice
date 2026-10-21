#Сколько раз встречается каждое значение.
def count_items(values: list) -> dict[str, int]:
    result = {}

    for value in values:
        result[value] = result.get(value, 0) + 1
        
    return result

#Уникальные значения по возрастанию.
def unique_sorted(values: list) -> list:
    return sorted(set(values))

#Значения, которые есть в обоих списках, по возрастанию.
def common(first: list, second: list) -> list:
    return sorted(set(first) & set(second))

#Значения, которые есть в первом списке и отсутствуют во втором, по возрастанию.
def only_in_first(first: list, second: list) -> list:
    return sorted(set(first) - set(second))
