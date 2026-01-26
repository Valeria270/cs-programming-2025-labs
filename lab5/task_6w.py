def list_to_dict(lst):
    return {item: item for item in lst}

my_list = ['a', 1, 3.14, ('x', 'y'), True]
result = list_to_dict(my_list)
print(result)