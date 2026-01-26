personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]
result = list(map(
    lambda p: {
        "name": p["name"],
        "clearance": p["clearance"],
        "category": (
            "Restricted" if p["clearance"] == 1 else
            "Confidential" if 2 <= p["clearance"] <= 3 else
            "Top Secret"
        )
    },
    personnel
))
print("Список персонала с категориями допуска:")
for person in result:
    print(f"{person['name']} - Уровень {person['clearance']} - {person['category']}")