def main():
    try:
        a, b, c = map(float, input("Введите три числа через пробел: ").split())
        
        smallest = a 
        
        if b < smallest:
            smallest = b
        
        if c < smallest:
            smallest = c
        
        print(f"Наименьшее число: {smallest}")
        
    except ValueError:
        print("Ошибка: пожалуйста, введите три числовых значения через пробел")

if __name__ == "__main__":
    main()