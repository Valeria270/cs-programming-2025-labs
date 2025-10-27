number = int(input("Введите число для вычисления факториала: "))
factorial = 1 
if number < 0:  
    print("Факториал не определен для отрицательных чисел")  
else:  
for i in range(1, number + 1):  
        factorial *= i  
    print(f"Факториал числа {number} равен {factorial}")