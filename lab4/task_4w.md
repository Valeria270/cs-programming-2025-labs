number = input("Введите число: ")
if not number.isdigit():
    print("Ошибка: введите целое положительное число")
else:
    num = int(number)
    last_digit = num % 10
    is_even = last_digit % 2 == 0
    digit_sum = sum(int(digit) for digit in number)
    divisible_by_3 = digit_sum % 3 == 0
    if is_even and divisible_by_3:
        print(f"Число {num} делится на 6")
    else:
        print(f"Число {num} не делится на 6")
        if not is_even:
            print("- Последняя цифра нечетная")
        if not divisible_by_3:
            print("- Сумма цифр не делится на 3")