hour=int(input("Введите час (0-23): "))
if hour < 0 or hour > 23:
    print("Ошибка: час должен быть в диапазоне от 0 до 23")
else:
    if hour <= 5:
        period = "ночь"
    elif hour <= 11:
        period = "утро"
    elif hour <= 17:
        period = "день"
    else:
        period = "вечер"

    print(f"Сейчас {period}")