try:
    number = int(input("Введите число: "))
    
    if number < 2:
        print(f"{number} - не является простым числом (простые числа больше 1)")
    elif number == 2:
        print(f"{number} - простое число")
    elif number % 2 == 0:
        print(f"{number} - составное число")
    else:
        is_prime = True
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(f"{number} - простое число")
        else:
            print(f"{number} - составное число")

except ValueError:
    print("Ошибка: введите целое число")
except Exception as e:
    print(f"Произошла ошибка: {e}")