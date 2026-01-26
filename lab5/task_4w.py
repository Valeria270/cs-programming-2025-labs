def sort_tuple_if_all_numbers(t):
    for element in t:
        if not isinstance(element, (int, float)):
            return t

    return tuple(sorted(t))

tuple1 = (5, 2, 8, 1, 3)
print(f"Исходный: {tuple1}")
print(f"Результат: {sort_tuple_if_all_numbers(tuple1)}")