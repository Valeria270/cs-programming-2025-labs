protocols = [
    ("Lockdown", 5),
    ("Evacuation", 4),
    ("Data Wipe", 3),
    ("Routine Scan", 1)
]
formatted_protocols = list(
    map(lambda p: f"Protocol {p[0]} - Criticality {p[1]}", protocols)
)
print("Список протоколов безопасности:")
for protocol in formatted_protocols:
    print(protocol)