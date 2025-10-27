while True:  
    try:  
        num = int(input("Введите число от 1 до 9: "))  
        if 1 <= num <= 9:  
            break  
        else:  
            print("Число должно быть от 1 до 9!")  
    except ValueError:  
        print("Пожалуйста, введите целое число!")
print(f"\nТаблица умножения для числа {num}:")  
for i in range(1, 11):  
    result = num * i  
    print(f"{num} × {i} = {result}")       