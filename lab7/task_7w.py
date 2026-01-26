incidents = [
    {"id": 101, "staff": 4},
    {"id": 102, "staff": 12},
    {"id": 103, "staff": 7},
    {"id": 104, "staff": 20}
]
sorted_incidents = sorted(incidents, key=lambda x: x["staff"], reverse=True)
print("Все инциденты, отсортированные по количеству персонала (по убыванию):")
for incident in sorted_incidents:
    print(f"Инцидент {incident['id']}: {incident['staff']} человек")
top_three = sorted_incidents[:3]
print("\nТри наиболее ресурсоемких инцидента:")
for incident in top_three:
    print(f"Инцидент {incident['id']}: {incident['staff']} человек")
print("\nСписок трех наиболее ресурсоемких инцидентов:")
print(top_three)