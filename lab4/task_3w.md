try:
    age = input("Введите возраст собаки (в годах): ")
    dog_age = float(age)
    
    if dog_age < 1:
        print("Ошибка: возраст должен быть не меньше 1")
    elif dog_age > 22:
        print("Ошибка: возраст должен быть не больше 22")
    else:
        if dog_age <= 2:
            human_age = dog_age * 10.5
        else:
            human_age = 2 * 10.5 + (dog_age - 2) * 4
        
        print(f"Возраст собаки в человеческих годах: {human_age}")

except ValueError:
    print("Ошибка: введено не число")