staff_shifts = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
]
total_costs = list(map(lambda x: x["shift_cost"] * x["shifts"], staff_shifts))

print("Расчет общей стоимости работы:")
for emp, cost in zip(staff_shifts, total_costs):
    print(f"{emp['name']}: {cost} кредитов")
max_cost = max(total_costs)
print(f"\nМаксимальная стоимость: {max_cost} кредитов")