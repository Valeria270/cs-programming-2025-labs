def main():
    year = input("Введите год: ")
    
    if not year.isdigit() or int(year) <= 0:
        print("Ошибка: введите положительное целое число")
        return
    
    year = int(year)
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        result = "високосный"
    else:
        result = "невисокосный"
    
    print(f"{year} - {result} год")

if __name__ == "__main__":
    main()