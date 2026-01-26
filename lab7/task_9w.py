shifts = [6, 12, 8, 24, 10, 4]
valid_shifts = list(
    filter(lambda hours: 8 <= hours <= 12, shifts)
)
print("Все смены:", shifts)
print("\nСмены от 8 до 12 часов включительно:")
for shift in valid_shifts:
    print(f"- {shift} часов")
print("\nСписок подходящих смен:", valid_shifts)
print(f"\nВсего смен: {len(shifts)}")
print(f"Подходящих смен: {len(valid_shifts)}")
print(f"Неподходящих смен: {len(shifts) - len(valid_shifts)}")