def add_numbers_to_string(input_string):  
    result = ""  
    for index, char in enumerate(input_string, start=1):  
        result += char + str(index)  
    return result  