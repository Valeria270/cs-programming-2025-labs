evaluations = [
    {"name": "Agent Cole", "score": 78},
    {"name": "Dr. Weiss", "score": 92},
    {"name": "Technician Moore", "score": 61},
    {"name": "Researcher Lin", "score": 88}
]
best_employee = max(evaluations, key=lambda emp: emp["score"])
print("Сотрудник с наивысшей психологической оценкой:")
print(f"Имя: {best_employee['name']}")
print(f"Балл: {best_employee['score']}")
print(f"\n{best_employee['name']} - {best_employee['score']} баллов")